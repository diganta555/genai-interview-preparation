# Coding challenge workbook

Solve before consulting the referenced teaching primitive. References are partial examples; production challenges require additional implementation and tests.

## 01. Cosine similarity

**Difficulty:** Easy

**Requirements and test cases:** O(d); reject unequal dimensions, zero and nonfinite vectors.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [vectors.py](../examples/vectors.py)

## 02. Stable deduplication

**Difficulty:** Easy

**Requirements and test cases:** Preserve first occurrence order; test duplicate IDs with conflicting content.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [core.py](../examples/core.py)

## 03. Overlapping chunks

**Difficulty:** Easy

**Requirements and test cases:** Retain offsets; require overlap < size; test empty and short documents.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [core.py](../examples/core.py)

## 04. Confusion matrix metrics

**Difficulty:** Easy

**Requirements and test cases:** Define zero-denominator behavior; demonstrate imbalance.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [metrics.py](../examples/metrics.py)

## 05. Recall@k

**Difficulty:** Easy

**Requirements and test cases:** Deduplicate ranked IDs; define behavior when no gold labels exist.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [core.py](../examples/core.py)

## 06. Reciprocal rank

**Difficulty:** Easy

**Requirements and test cases:** Distinguish cutoff-based reciprocal rank from unrestricted MRR.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [core.py](../examples/core.py)

## 07. Fictional cost calculator

**Difficulty:** Easy

**Requirements and test cases:** Use Decimal and reject negative usage; no live price assumptions.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [cost.py](../examples/cost.py)

## 08. Tool allowlist

**Difficulty:** Easy

**Requirements and test cases:** Reject unknown names and preserve call IDs.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [tools.py](../examples/tools.py)

## 09. Versioned source replacement

**Difficulty:** Medium

**Requirements and test cases:** Validate all records before replacing; remove orphaned chunks.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [core.py](../examples/core.py)

## 10. Tenant-aware top-k

**Difficulty:** Medium

**Requirements and test cases:** Filter before ranking; test identical IDs in two tenants.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [core.py](../examples/core.py)

## 11. Reciprocal rank fusion

**Difficulty:** Medium

**Requirements and test cases:** Combine ranks rather than uncalibrated scores; deduplicate each list.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [hybrid.py](../examples/hybrid.py)

## 12. Provider interface

**Difficulty:** Medium

**Requirements and test cases:** Normalize outputs, usage, errors and capabilities; inject a fake.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [live_models.py](../examples/live_models.py)

## 13. Strict tool arguments

**Difficulty:** Medium

**Requirements and test cases:** Reject extra fields and fabricated IDs; test number limits.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [core.py](../examples/core.py)

## 14. Read-only SQL aggregate

**Difficulty:** Medium

**Requirements and test cases:** Parameterize tenant and dates; test join and currency semantics.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [sql.py](../examples/sql.py)

## 15. Scoped memory expiry

**Difficulty:** Medium

**Requirements and test cases:** Inject time for deterministic tests; test tenant isolation.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [memory.py](../examples/memory.py)

## 16. Citation validation

**Difficulty:** Medium

**Requirements and test cases:** Check ID availability; document that entailment is a separate check.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [evaluate.py](../examples/evaluate.py)

## 17. Prompt version hash

**Difficulty:** Medium

**Requirements and test cases:** Use canonical serialization; include output schema revision.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [prompts.py](../examples/prompts.py)

## 18. Evaluation JSONL runner

**Difficulty:** Medium

**Requirements and test cases:** Keep per-case outcomes and configuration; fail on invalid cases.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [evaluate.py](../examples/evaluate.py)

## 19. Bounded asynchronous map

**Difficulty:** Hard

**Requirements and test cases:** Bound active calls and queue size; preserve failures and ordering.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [async_batch.py](../examples/async_batch.py)

## 20. Cancellation propagation

**Difficulty:** Hard

**Requirements and test cases:** Cancel a parent and verify workers stop and clean up.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [core.py](../examples/core.py)

## 21. Transient retry budget

**Difficulty:** Hard

**Requirements and test cases:** Retry only classified safe failures within total time.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [reliability.py](../examples/reliability.py)

## 22. No-progress loop detection

**Difficulty:** Hard

**Requirements and test cases:** Canonicalize tool inputs and define progress; stop on repeated failure.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [tool_loop.py](../examples/tool_loop.py)

## 23. Approval workflow

**Difficulty:** Hard

**Requirements and test cases:** Resume authorized thread; keep side effects after approval.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [langgraph_example.py](../examples/langgraph_example.py)

## 24. Index migration

**Difficulty:** Hard

**Requirements and test cases:** Build shadow index, benchmark, switch alias, and roll back.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [hybrid.py](../examples/hybrid.py)

## 25. Context packing

**Difficulty:** Hard

**Requirements and test cases:** Budget tokenizer tokens; preserve source IDs and critical spans.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [rag.py](../examples/rag.py)

## 26. Semantic cache guard

**Difficulty:** Hard

**Requirements and test cases:** Reject reuse with different amounts, dates, identity or ACL version.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [router.py](../examples/router.py)

## 27. Source freshness

**Difficulty:** Hard

**Requirements and test cases:** Simulate permission revocation independently of source update.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [security.py](../examples/security.py)

## 28. Parallel evidence merge

**Difficulty:** Hard

**Requirements and test cases:** Handle worker failure and conflict without dropping provenance.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [multi_agent.py](../examples/multi_agent.py)

## 29. Streaming event contract

**Difficulty:** Production

**Requirements and test cases:** Start/token/error/done events; cancellation and no false success.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [trace.py](../examples/trace.py)

## 30. Distributed rate limiting

**Difficulty:** Production

**Requirements and test cases:** Atomic shared counters; request and token budgets; test replicas.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [capacity.py](../examples/capacity.py)

## 31. Circuit breaker

**Difficulty:** Production

**Requirements and test cases:** Closed/open/half-open transitions with injected time and dependency errors.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [reliability.py](../examples/reliability.py)

## 32. Idempotent side effects

**Difficulty:** Production

**Requirements and test cases:** Operation IDs, replay, ambiguous timeouts, and reconciliation.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [tool_loop.py](../examples/tool_loop.py)

## 33. Queue worker

**Difficulty:** Production

**Requirements and test cases:** Lease, retry, deduplication, dead-letter status, and shutdown.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [async_batch.py](../examples/async_batch.py)

## 34. Secure URL fetcher

**Difficulty:** Production

**Requirements and test cases:** Validate DNS, redirects, private IPs, protocol, time and response size.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [security.py](../examples/security.py)

## 35. Document parser isolation

**Difficulty:** Production

**Requirements and test cases:** Size/time/page caps; no execution of embedded content.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [dataset.py](../examples/dataset.py)

## 36. Observability redaction

**Difficulty:** Production

**Requirements and test cases:** Trace useful metadata without leaking raw sensitive inputs.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [trace.py](../examples/trace.py)

## 37. Model rollout evaluation

**Difficulty:** Production

**Requirements and test cases:** Paired offline tests plus online slices and rollback.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [evaluate.py](../examples/evaluate.py)

## 38. Persistent tenant API

**Difficulty:** Production

**Requirements and test cases:** Verify authentication, ACLs, persistence and restart behavior.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [rag.py](../examples/rag.py)

## 39. Failure-aware model router

**Difficulty:** Production

**Requirements and test cases:** Capability checks and quality gates before fallback.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [router.py](../examples/router.py)

## 40. Backup recovery drill

**Difficulty:** Production

**Requirements and test cases:** Restore source metadata and index; verify source and ACL versions.

**Explain:** input contract, complexity, failure behavior, permissions, and one limitation.

**Reference primitive:** [deployment_check.py](../examples/deployment_check.py)
