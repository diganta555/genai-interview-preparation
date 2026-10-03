"""Offline teaching primitives. Lexical vectors and extractive answers are NOT LLMs."""
from __future__ import annotations
import asyncio
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal
import hashlib
import json
import math
import re
import time
from typing import Awaitable, Callable, Iterable, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def cosine(a: list[float], b: list[float]) -> float:
    if not a or len(a) != len(b):
        raise ValueError('vectors must have equal nonzero dimensions')
    if not all(math.isfinite(v) for v in a + b):
        raise ValueError('vectors must be finite')
    na, nb = math.hypot(*a), math.hypot(*b)
    if na == 0 or nb == 0:
        raise ValueError('zero-vector cosine is undefined')
    return max(-1.0, min(1.0, sum((x / na) * (y / nb) for x, y in zip(a, b))))

def chunks(text: str, size: int = 120, overlap: int = 20) -> list[tuple[int, str]]:
    """Character-window baseline, retaining source offsets; NOT token-aware."""
    if not 0 <= overlap < size:
        raise ValueError('require 0 <= overlap < size')
    result = []
    start = 0
    while start < len(text):
        result.append((start, text[start:start + size]))
        if start + size >= len(text):
            break
        start += size - overlap
    return result

def tokens(text: str) -> list[str]:
    return re.findall(r'\w+', text.lower())

class LexicalEncoder:
    """Fixed-vocabulary bag-of-words baseline. No learned semantic embeddings."""
    def __init__(self, texts: Iterable[str]):
        self.vocabulary = sorted({word for text in texts for word in tokens(text)})
        self.revision = hashlib.sha256('\n'.join(self.vocabulary).encode()).hexdigest()[:12]
    def encode(self, text: str) -> list[float]:
        counts = Counter(tokens(text))
        return [float(counts[word]) for word in self.vocabulary]

@dataclass(frozen=True)
class Record:
    id: str
    tenant: str
    source_id: str
    version: str
    text: str
    vector: tuple[float, ...]
    offset: int = 0

class VectorStore:
    """In-memory exact index with explicit tenant filtering; resets on restart."""
    def __init__(self, dimension: int):
        if dimension <= 0:
            raise ValueError('dimension must be positive')
        self.dimension = dimension
        self._records: dict[tuple[str, str], Record] = {}
    def _validate(self, record: Record) -> None:
        if not record.id or not record.tenant or not record.source_id or not record.version:
            raise ValueError('missing identity or version')
        if len(record.vector) != self.dimension or not all(math.isfinite(x) for x in record.vector):
            raise ValueError('invalid vector')
        if math.hypot(*record.vector) == 0:
            raise ValueError('cannot index zero vector')
    def upsert(self, record: Record) -> None:
        self._validate(record)
        self._records[(record.tenant, record.id)] = record
    def replace_source(self, tenant: str, source_id: str, records: list[Record]) -> None:
        """Validate all before replacing; empty records delete a source in this lab."""
        seen = set()
        for record in records:
            self._validate(record)
            if record.tenant != tenant or record.source_id != source_id or record.id in seen:
                raise ValueError('replacement scope mismatch or duplicate ID')
            seen.add(record.id)
        updated = {key: value for key, value in self._records.items()
                   if not (value.tenant == tenant and value.source_id == source_id)}
        updated.update({(r.tenant, r.id): r for r in records})
        self._records = updated
    def delete(self, tenant: str, record_id: str) -> bool:
        return self._records.pop((tenant, record_id), None) is not None
    def records(self, tenant: str) -> list[Record]:
        return [r for r in self._records.values() if r.tenant == tenant]
    def search(self, tenant: str, query: list[float], k: int = 3) -> list[tuple[float, Record]]:
        if not tenant or k <= 0:
            raise ValueError('tenant and positive k required')
        cosine(query, query)  # validate even for an empty store
        if len(query) != self.dimension:
            raise ValueError('dimension mismatch')
        ranked = [(cosine(query, list(r.vector)), r) for r in self.records(tenant)]
        return sorted(ranked, key=lambda item: (-item[0], item[1].id))[:k]

class OfflineRAG:
    """Lexical retrieval + extractive fixture answering; not a semantic LLM demo."""
    def __init__(self, documents: list[dict[str, str]]):
        self.encoder = LexicalEncoder(doc['text'] for doc in documents)
        self.store = VectorStore(len(self.encoder.vocabulary))
        for doc in documents:
            self.ingest(doc['tenant'], doc['id'], doc['version'], doc['text'])
    def ingest(self, tenant: str, source_id: str, version: str, text: str) -> None:
        records = []
        for offset, chunk in chunks(text):
            vector = self.encoder.encode(chunk)
            if not any(vector):
                continue
            record_id = hashlib.sha256(f'{tenant}|{source_id}|{version}|{offset}'.encode()).hexdigest()[:20]
            records.append(Record(record_id, tenant, source_id, version, chunk, tuple(vector), offset))
        self.store.replace_source(tenant, source_id, records)
    def retrieve(self, tenant: str, question: str, k: int = 3) -> list[tuple[float, Record]]:
        query = self.encoder.encode(question)
        if not any(query):
            return []
        return [(score, record) for score, record in self.store.search(tenant, query, k) if score > 0]
    def answer(self, tenant: str, question: str) -> dict:
        hits = self.retrieve(tenant, question)
        if not hits:
            return {'answer': 'No matching evidence found.', 'citations': [], 'abstained': True,
                    'mode': 'offline-lexical-extractive'}
        score, record = hits[0]
        return {'answer': record.text, 'abstained': False, 'mode': 'offline-lexical-extractive',
                'citations': [{'chunk_id': record.id, 'source_id': record.source_id,
                               'version': record.version, 'offset': record.offset, 'score': score}]}

@dataclass(frozen=True)
class Outcome:
    item: object
    value: object = None
    error: str | None = None

async def bounded_map(items: Iterable[T], fn: Callable[[T], Awaitable[U]],
                      concurrency: int = 5, timeout: float = 1.0) -> list[Outcome]:
    """A fixed worker pool: active calls AND queued tasks stay bounded.

    Result storage is O(N); use an async output sink for an unbounded corpus.
    Errors are returned by type only; cancellation propagates.
    """
    if concurrency <= 0 or timeout <= 0:
        raise ValueError('positive concurrency and timeout required')
    queue: asyncio.Queue = asyncio.Queue(maxsize=concurrency)
    results: dict[int, Outcome] = {}
    sentinel = object()
    async def producer():
        for index, item in enumerate(items):
            await queue.put((index, item))
        for _ in range(concurrency):
            await queue.put(sentinel)
    async def worker():
        while True:
            entry = await queue.get()
            try:
                if entry is sentinel:
                    return
                index, item = entry
                try:
                    async with asyncio.timeout(timeout):
                        value = await fn(item)
                    results[index] = Outcome(item, value=value)
                except Exception as exc:
                    results[index] = Outcome(item, error=type(exc).__name__)
            finally:
                queue.task_done()
    async with asyncio.TaskGroup() as group:
        group.create_task(producer())
        for _ in range(concurrency):
            group.create_task(worker())
    return [results[index] for index in sorted(results)]

class TransientError(Exception):
    pass

async def retry_read(fn: Callable[[], Awaitable[T]], attempts: int = 3,
                     deadline: float = 2.0) -> T:
    """Only TransientError is retryable. Read-only/idempotent operation contract."""
    if attempts <= 0 or deadline <= 0:
        raise ValueError('positive retry limits required')
    async with asyncio.timeout(deadline):
        for attempt in range(attempts):
            try:
                return await fn()
            except TransientError:
                if attempt + 1 == attempts:
                    raise
                await asyncio.sleep(min(0.05 * 2 ** attempt, 0.25))
    raise RuntimeError('unreachable')

def classification_metrics(tp: int, fp: int, fn: int, tn: int) -> dict[str, float]:
    if min(tp, fp, fn, tn) < 0:
        raise ValueError('counts must be nonnegative')
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    total = tp + fp + fn + tn
    return {'precision': precision, 'recall': recall, 'f1': f1,
            'accuracy': (tp + tn) / total if total else 0.0}

def retrieval_metrics(ranked: list[str], relevant: set[str], k: int = 3) -> dict[str, float]:
    if k <= 0:
        raise ValueError('positive k required')
    ranked = list(dict.fromkeys(ranked))[:k]
    recall = len(set(ranked) & relevant) / len(relevant) if relevant else 0.0
    rr = next((1 / (i + 1) for i, x in enumerate(ranked) if x in relevant), 0.0)
    return {'recall_at_k': recall, 'reciprocal_rank_at_k': rr}

def rrf(rankings: list[list[str]], constant: int = 60) -> list[tuple[str, float]]:
    if constant <= 0:
        raise ValueError('positive fusion constant required')
    scores: Counter = Counter()
    for ranking in rankings:
        for rank, doc_id in enumerate(dict.fromkeys(ranking), 1):
            scores[doc_id] += 1 / (constant + rank)
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))

def calculate(operation: str, a: float, b: float) -> float:
    if not math.isfinite(a) or not math.isfinite(b) or max(abs(a), abs(b)) > 1e12:
        raise ValueError('invalid operands')
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError('division by zero')
        result = a / b
    else:
        raise ValueError('unknown operation')
    if not math.isfinite(result):
        raise ValueError('nonfinite result')
    return result

@dataclass(frozen=True)
class Identity:
    tenant: str
    role: str

def execute_tool(proposal: dict, identity: Identity) -> dict:
    """Static allowlist. Identity is trusted caller context, not model arguments."""
    if set(proposal) != {'id', 'name', 'arguments'}:
        raise ValueError('invalid proposal fields')
    if not isinstance(proposal['id'], str) or not proposal['id']:
        raise ValueError('missing call ID')
    name, args = proposal['name'], proposal['arguments']
    if not isinstance(args, dict):
        raise ValueError('arguments must be an object')
    if name == 'calculator':
        if set(args) != {'operation', 'a', 'b'}:
            raise ValueError('invalid calculator fields')
        if type(args['a']) not in (int, float) or type(args['b']) not in (int, float):
            raise ValueError('operands must be JSON numbers, not booleans or strings')
        result = calculate(args['operation'], float(args['a']), float(args['b']))
    elif name == 'employee':
        if identity.role != 'hr' or identity.tenant != 'demo':
            raise PermissionError('employee access denied')
        if args != {'employee_id': 'E1'}:
            raise ValueError('unknown employee or forbidden fields')
        result = {'name': 'Synthetic Employee', 'team': 'Engineering'}
    else:
        raise PermissionError('tool not allowed')
    return {'tool_call_id': proposal['id'], 'result': result}

def execute_plan(proposals: list[dict], identity: Identity, limit: int = 3) -> dict:
    if limit <= 0:
        raise ValueError('positive limit required')
    seen: set[str] = set()
    results = []
    for proposal in proposals:
        if len(results) >= limit:
            return {'results': results, 'stop_reason': 'budget'}
        fingerprint = json.dumps({k: proposal[k] for k in ('name', 'arguments')}, sort_keys=True)
        if fingerprint in seen:
            return {'results': results, 'stop_reason': 'no_progress'}
        seen.add(fingerprint)
        try:
            results.append(execute_tool(proposal, identity))
        except (ValueError, PermissionError, TypeError) as exc:
            return {'results': results, 'stop_reason': type(exc).__name__}
    return {'results': results, 'stop_reason': 'completed'}

def fictional_cost(input_tokens: int, output_tokens: int, input_rate: str = '2',
                    output_rate: str = '8') -> Decimal:
    """Fictional currency units per million tokens, NOT current vendor prices."""
    if min(input_tokens, output_tokens) < 0:
        raise ValueError('negative token usage')
    ir, ore = Decimal(input_rate), Decimal(output_rate)
    if not ir.is_finite() or not ore.is_finite() or min(ir, ore) < 0:
        raise ValueError('invalid rate')
    return (Decimal(input_tokens) * ir + Decimal(output_tokens) * ore) / Decimal(1_000_000)

def cache_key(identity: Identity, question: str, index_version: str,
              prompt_version: str, model: str, acl_version: str) -> str:
    data = [identity.tenant, identity.role, question, index_version,
            prompt_version, model, acl_version]
    return hashlib.sha256(json.dumps(data, ensure_ascii=False).encode()).hexdigest()

class PreferenceMemory:
    def __init__(self):
        self._data: dict[tuple[str, str, str], tuple[str, float]] = {}
    def put(self, tenant: str, user: str, key: str, value: str, ttl: float,
            now: float | None = None) -> None:
        if ttl <= 0:
            raise ValueError('positive ttl required')
        self._data[(tenant, user, key)] = (value, (time.time() if now is None else now) + ttl)
    def get(self, tenant: str, user: str, key: str, now: float | None = None) -> str | None:
        item = self._data.get((tenant, user, key))
        if item and item[1] > (time.time() if now is None else now):
            return item[0]
        self._data.pop((tenant, user, key), None)
        return None
    def delete(self, tenant: str, user: str, key: str) -> None:
        self._data.pop((tenant, user, key), None)

def demo_documents() -> list[dict[str, str]]:
    return [
        {'tenant': 'demo', 'id': 'refund-policy', 'version': 'v1',
         'text': 'Refunds are available within 14 days with a receipt.'},
        {'tenant': 'demo', 'id': 'delivery-policy', 'version': 'v1',
         'text': 'Delivery normally takes three business days.'},
        {'tenant': 'other', 'id': 'private-policy', 'version': 'v1',
         'text': 'Private refunds policy for another tenant is confidential.'},
    ]
