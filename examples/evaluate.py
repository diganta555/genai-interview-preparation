import argparse, json, time
from pathlib import Path
from examples.core import OfflineRAG, demo_documents, retrieval_metrics
DEFAULT = Path(__file__).resolve().parents[1]/'data'/'eval.jsonl'
def run(path=DEFAULT):
    rag = OfflineRAG(demo_documents())
    results = []
    for line in Path(path).read_text().splitlines():
        case = json.loads(line)
        start = time.perf_counter()
        answer = rag.answer(case['tenant'],case['question'])
        hits = rag.retrieve(case['tenant'],case['question'])
        available = {r.id for _,r in hits}
        results.append({'id':case['id'],
            'abstention_pass':answer['abstained']==case['expect_abstain'],
            'citation_availability_pass':all(c['chunk_id'] in available for c in answer['citations']),
            **retrieval_metrics([r.source_id for _,r in hits],set(case['relevant_sources'])),
            'latency_ms':(time.perf_counter()-start)*1000,
            'semantic_review':'not performed', 'answer':answer})
    return results
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run()
    print(json.dumps(result,indent=2))
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
