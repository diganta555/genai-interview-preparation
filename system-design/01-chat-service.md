# Design: ChatGPT-Like Chat Service

## Users and problem

Users need streaming conversation, history, account isolation, and optional tools.

## Functional requirements

Provide message submission, stream events, history, cancellation, and deletion. Clarify peak QPS, context limits, regions, and whether uploads or tools are in scope.

## Non-functional requirements and sizing

Agree on latency, availability, quality, security, data residency, retention, freshness, and budget. Example assumptions for practice: 100 requests/s, five seconds mean service time, and 3000 input plus 500 output tokens per request. These are fictional sizing inputs, not measured traffic. They imply around 500 in-flight calls and 21 million tokens per minute before retries. Adjust for actual workload and provider quotas.

## Architecture

Stateless API authenticates a user and validates ownership, loads bounded history, invokes a configured model, and streams start/token/error/done events. Persist final status independently from the stream socket. Tools, if supported, execute behind caller-bound authorization.

## APIs

POST /conversations; POST /conversations/{id}/messages; GET /conversations/{id}; DELETE /conversations/{id}. Return request IDs, structured errors, and explicit queued/partial/completed status. Use pagination and idempotency where appropriate. Streaming has start, token, error, and done semantics.

## Database schema

users; conversations(owner_id, tenant_id); messages(conversation_id, role, content_ref, created_at); runs(status, model_config, usage). Add keys, tenant-aware indexes, version records, created/updated timestamps, and retention metadata. Keep secrets outside application records and source payloads.

## Vector database, cache, and queues

Cache static prompt fragments or eligible exact responses only; conversational personalized answers are rarely globally cacheable. Store durable conversations in PostgreSQL and optional fast session state in Redis. Vector search is optional, not mandatory for basic chat.

## Model layer

Use configured adapters with task capabilities, allowed providers, token and time budgets, usage capture, and validated fallback. A provider switch needs regression and contract tests. Do not assume structured outputs, tool calls, and streaming behave identically across models.

## Observability and evaluation

Trace API, queue, retrieval, model, tool, and persistence stages. Use safe metadata with redaction. Track success, p95, errors, quota pressure, cost per task, and relevant semantic metrics. Compare changes on held-out cases and critical slices; test hard invariants separately from judge or human review.

## Security

Verify identity, enforce resource and operation permissions in code, constrain tool capabilities and egress, validate outputs, and minimize sensitive context. Treat uploaded and retrieved content as untrusted. Bind approvals to immutable concrete requests where actions require them.

## Scaling

Separate asynchronous processing from interactive APIs, horizontally scale stateless workers, coordinate shared rate limits, and benchmark search plus ingestion together. Provider quotas can dominate even when API replicas are idle. Estimate chunks, vectors, metadata, replicas, cache, and index overhead rather than only document count.

## Failure handling

Conversation history can exceed context or expose one user’s messages to another. A disconnect may leave generation running. Use ownership checks, context packing, cancellation propagation, and safe partial-run records. Add total deadlines, cancellation, bounded retries for safe transient failures, and explicit escalation or degraded status. Reconcile ambiguous side effects and test restart and restore.

## Cost considerations

Measure input/output, embeddings, reranking, tool calls, storage, infrastructure, and operational effort. Remove duplication before introducing more model stages. Routing and caching require quality and permission gates. Use real current rate assumptions only when planning deployment.

## Trade-offs to defend

Explain why the selected control flow, data store, model, and search strategy fit requirements. Compare a simpler baseline. Identify the metric and workload that would justify replacing a component.

## Interview follow-up

What changes at ten times load, during an upstream outage, after a permission revocation, or during model/index migration? Describe a concrete failure path and how you know recovery succeeded.
