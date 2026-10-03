# Design: Multi-Agent Research System

## Users and problem

Researchers want independent collection, synthesis, and source verification.

## Functional requirements

Bound source and worker budgets, preserve provenance, manage partial failures, detect contradictory claims, and compare with a single-workflow baseline.

## Non-functional requirements and sizing

Agree on latency, availability, quality, security, data residency, retention, freshness, and budget. Example assumptions for practice: 100 requests/s, five seconds mean service time, and 3000 input plus 500 output tokens per request. These are fictional sizing inputs, not measured traffic. They imply around 500 in-flight calls and 21 million tokens per minute before retries. Adjust for actual workload and provider quotas.

## Architecture

A supervisor assigns scoped tasks to independent collectors. A deterministic merge deduplicates sources, a synthesis stage creates claim candidates, and checking uses original source spans. Final output identifies unsupported or unresolved claims.

## APIs

POST /research/tasks; GET /research/tasks/{id}/workers; GET /research/tasks/{id}/report. Return request IDs, structured errors, and explicit queued/partial/completed status. Use pagination and idempotency where appropriate. Streaming has start, token, error, and done semantics.

## Database schema

tasks(principal, budget, status); worker_runs(role, version, usage, status); sources(url, checksum, fetched_at); claims(text, evidence_spans, support_status). Add keys, tenant-aware indexes, version records, created/updated timestamps, and retention metadata. Keep secrets outside application records and source payloads.

## Vector database, cache, and queues

Queue long tasks and store evidence artifacts with immutable IDs. Shared state uses explicit contracts and conflict rules. Cache source fetches by URL/checksum and permitted scope. Parallelism reduces elapsed time but increases concurrent provider demand.

## Model layer

Use configured adapters with task capabilities, allowed providers, token and time budgets, usage capture, and validated fallback. A provider switch needs regression and contract tests. Do not assume structured outputs, tool calls, and streaming behave identically across models.

## Observability and evaluation

Trace API, queue, retrieval, model, tool, and persistence stages. Use safe metadata with redaction. Track success, p95, errors, quota pressure, cost per task, and relevant semantic metrics. Compare changes on held-out cases and critical slices; test hard invariants separately from judge or human review.

## Security

Verify identity, enforce resource and operation permissions in code, constrain tool capabilities and egress, validate outputs, and minimize sensitive context. Treat uploaded and retrieved content as untrusted. Bind approvals to immutable concrete requests where actions require them.

## Scaling

Separate asynchronous processing from interactive APIs, horizontally scale stateless workers, coordinate shared rate limits, and benchmark search plus ingestion together. Provider quotas can dominate even when API replicas are idle. Estimate chunks, vectors, metadata, replicas, cache, and index overhead rather than only document count.

## Failure handling

Agents may share one erroneous summary, delegate cyclically, or consume all budget before verification. Require original-source checking, allocation limits, no-progress detection, and reserved synthesis/verification budget. Add total deadlines, cancellation, bounded retries for safe transient failures, and explicit escalation or degraded status. Reconcile ambiguous side effects and test restart and restore.

## Cost considerations

Measure input/output, embeddings, reranking, tool calls, storage, infrastructure, and operational effort. Remove duplication before introducing more model stages. Routing and caching require quality and permission gates. Use real current rate assumptions only when planning deployment.

## Trade-offs to defend

Explain why the selected control flow, data store, model, and search strategy fit requirements. Compare a simpler baseline. Identify the metric and workload that would justify replacing a component.

## Interview follow-up

What changes at ten times load, during an upstream outage, after a permission revocation, or during model/index migration? Describe a concrete failure path and how you know recovery succeeded.
