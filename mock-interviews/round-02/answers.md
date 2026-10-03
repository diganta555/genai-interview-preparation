# Round 2 answer key

Open only after answering each question.

## 1. You are about to deploy fundamentals and data structures. What design and acceptance checks do you require?

**Expected answer:** Use lists for ordered chunks, dictionaries for records keyed by ID, sets for deduplication, and tuples for immutable coordinates. Avoid mutable default arguments: a default list is shared between calls. Shallow copying a dictionary does not copy nested lists. Understand truthiness, comprehensions, slicing, scope, and equality versus identity before writing pipelines. Use bounded asynchronous I/O for independent requests, a shared client, explicit timeouts, and a retry budget. Keep CPU-heavy parsing out of the event loop and respect provider request and token quotas.

**Deep follow-up:** With concurrency 10 and no other bottleneck, 100 five-second requests take roughly 50 seconds rather than 500. Little’s law relates in-flight requests to arrival rate and mean service time. Quotas and tail latency constrain useful concurrency. A semaphore limits active calls but a queue is also needed to bound queued memory. A document ID plus ingestion version makes retried writes idempotent. Measure queue delay separately from provider duration.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Fundamentals and data structures; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy api architecture. What design and acceptance checks do you require?

**Expected answer:** Separate transport validation, authorization, application logic, retrieval, model adapters, and persistence. Keep external provider schemas behind adapters. FastAPI and Pydantic fit request contracts; async dependencies need nonblocking libraries. Share clients through application lifecycle management. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for API architecture; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy sql fundamentals. What design and acceptance checks do you require?

**Expected answer:** Understand SELECT, WHERE, JOIN, GROUP BY, HAVING, ORDER BY, indexes, transactions, and query plans. Parameters represent values, not arbitrary table names. Relational constraints preserve consistency. Learn NULL behavior and duplicate joins before trusting analytical totals. Clarify purchase and date semantics, produce a constrained read-only aggregate query, parameterize tenant, cutoff, and threshold, execute with least privilege and limits, then explain the returned result.

**Deep follow-up:** Use GROUP BY customer and HAVING SUM of eligible amounts above the threshold. Define six calendar months versus a fixed number of days and account for refunds and currency. The authenticated identity supplies tenant scope. A typed query plan is often safer than arbitrary generated SQL. The model summarizes returned rows; it must not invent customers absent from the result. Validate SQL structure and enforce permissions in the database.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for SQL fundamentals; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy oop and dependency injection. What design and acceptance checks do you require?

**Expected answer:** A provider interface separates business logic from one vendor SDK. Prefer small objects with explicit collaborators: Retriever receives an Embedder and a Store. Composition makes tests simpler than deep inheritance. Inject a fake model in tests so tests do not depend on bills, network availability, or model nondeterminism. Use bounded asynchronous I/O for independent requests, a shared client, explicit timeouts, and a retry budget. Keep CPU-heavy parsing out of the event loop and respect provider request and token quotas.

**Deep follow-up:** With concurrency 10 and no other bottleneck, 100 five-second requests take roughly 50 seconds rather than 500. Little’s law relates in-flight requests to arrival rate and mean service time. Quotas and tail latency constrain useful concurrency. A semaphore limits active calls but a queue is also needed to bound queued memory. A document ID plus ingestion version makes retried writes idempotent. Measure queue delay separately from provider duration.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for OOP and dependency injection; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy authentication and rate limiting. What design and acceptance checks do you require?

**Expected answer:** Use a real identity provider and derive tenant and role from verified identity. Limit by user, tenant, and workflow cost, with shared state for multi-replica services. Protect both requests per second and token budgets. A local API key is only a development control. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Authentication and rate limiting; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy postgresql and mysql. What design and acceptance checks do you require?

**Expected answer:** Both are relational databases with transactions and query planning, but dialects, extensions, and date semantics differ. Generate SQL for one explicit dialect. Test against realistic schema and data. Do not assume a query written for PostgreSQL runs unchanged on MySQL. Clarify purchase and date semantics, produce a constrained read-only aggregate query, parameterize tenant, cutoff, and threshold, execute with least privilege and limits, then explain the returned result.

**Deep follow-up:** Use GROUP BY customer and HAVING SUM of eligible amounts above the threshold. Define six calendar months versus a fixed number of days and account for refunds and currency. The authenticated identity supplies tenant scope. A typed query plan is often safer than arbitrary generated SQL. The model summarizes returned rows; it must not invent customers absent from the result. Validate SQL structure and enforce permissions in the database.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for PostgreSQL and MySQL; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy decorators. What design and acceptance checks do you require?

**Expected answer:** A decorator wraps a function to add behavior such as tracing or timing. Preserve names and documentation with functools.wraps. An async decorator must await the wrapped coroutine. Retrying through a decorator is only safe when the operation is retryable; repeating a payment tool can charge twice. Use bounded asynchronous I/O for independent requests, a shared client, explicit timeouts, and a retry budget. Keep CPU-heavy parsing out of the event loop and respect provider request and token quotas.

**Deep follow-up:** With concurrency 10 and no other bottleneck, 100 five-second requests take roughly 50 seconds rather than 500. Little’s law relates in-flight requests to arrival rate and mean service time. Quotas and tail latency constrain useful concurrency. A semaphore limits active calls but a queue is also needed to bound queued memory. A document ID plus ingestion version makes retried writes idempotent. Measure queue delay separately from provider duration.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Decorators; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy retries and timeouts. What design and acceptance checks do you require?

**Expected answer:** Set connect, read, total stage, and request deadlines. Respect provider retry hints and use exponential backoff with jitter. Retry transient failures only within a total budget. Never allow nested retry layers to multiply unnoticed. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Retries and timeouts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy redis. What design and acceptance checks do you require?

**Expected answer:** Redis is useful for caches, counters, queues in suitable designs, and session data. Define expiry and memory policy. A cache hit is valid only for the correct authorization and data version. Redis should not replace a transactional ledger simply because it is fast. Clarify purchase and date semantics, produce a constrained read-only aggregate query, parameterize tenant, cutoff, and threshold, execute with least privilege and limits, then explain the returned result.

**Deep follow-up:** Use GROUP BY customer and HAVING SUM of eligible amounts above the threshold. Define six calendar months versus a fixed number of days and account for refunds and currency. The authenticated identity supplies tenant scope. A typed query plan is often safer than arbitrary generated SQL. The model summarizes returned rows; it must not invent customers absent from the result. Validate SQL structure and enforce permissions in the database.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Redis; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy iterators and generators. What design and acceptance checks do you require?

**Expected answer:** An iterator produces values on demand; a generator implements this with yield. Stream document records rather than loading a huge corpus into RAM. A generator is usually consumed once. Streaming parsing reduces memory, but embedding APIs still need bounded batches and backpressure. Use bounded asynchronous I/O for independent requests, a shared client, explicit timeouts, and a retry budget. Keep CPU-heavy parsing out of the event loop and respect provider request and token quotas.

**Deep follow-up:** With concurrency 10 and no other bottleneck, 100 five-second requests take roughly 50 seconds rather than 500. Little’s law relates in-flight requests to arrival rate and mean service time. Quotas and tail latency constrain useful concurrency. A semaphore limits active calls but a queue is also needed to bound queued memory. A document ID plus ingestion version makes retried writes idempotent. Measure queue delay separately from provider duration.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Iterators and generators; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy circuit breakers. What design and acceptance checks do you require?

**Expected answer:** Open a breaker after a measured failure threshold, then probe recovery cautiously. Breakers reduce calls to an unhealthy dependency but must not permanently block a recovered service. Separate circuit state by dependency and failure class. Test transitions and half-open behavior. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Circuit breakers; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. You are about to deploy text-to-sql. What design and acceptance checks do you require?

**Expected answer:** Translate a question into a constrained logical plan or SQL proposal using authorized schema information. Validate before execution. Ask clarification when the business term is ambiguous. Record the question, approved plan, and result provenance. Clarify purchase and date semantics, produce a constrained read-only aggregate query, parameterize tenant, cutoff, and threshold, execute with least privilege and limits, then explain the returned result.

**Deep follow-up:** Use GROUP BY customer and HAVING SUM of eligible amounts above the threshold. Define six calendar months versus a fixed number of days and account for refunds and currency. The authenticated identity supplies tenant scope. A typed query plan is often safer than arbitrary generated SQL. The model summarizes returned rows; it must not invent customers absent from the result. Validate SQL structure and enforce permissions in the database.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Text-to-SQL; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. You are about to deploy context managers. What design and acceptance checks do you require?

**Expected answer:** with and async with express resource lifetime. Close files, HTTP clients, database sessions, and transactions even when exceptions happen. Open a shared HTTP client during application startup instead of constructing one per request. A transaction context should roll back when a write fails. Use bounded asynchronous I/O for independent requests, a shared client, explicit timeouts, and a retry budget. Keep CPU-heavy parsing out of the event loop and respect provider request and token quotas.

**Deep follow-up:** With concurrency 10 and no other bottleneck, 100 five-second requests take roughly 50 seconds rather than 500. Little’s law relates in-flight requests to arrival rate and mean service time. Quotas and tail latency constrain useful concurrency. A semaphore limits active calls but a queue is also needed to bound queued memory. A document ID plus ingestion version makes retried writes idempotent. Measure queue delay separately from provider duration.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Context managers; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. You are about to deploy queues and backpressure. What design and acceptance checks do you require?

**Expected answer:** Queue slow work with job IDs and status. Bound queue depth and reject or defer excess load. Use idempotent workers, leases, retries, and dead-letter inspection. A growing queue is latency debt, not proof that the service is healthy. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Queues and backpressure; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. You are about to deploy sql agents. What design and acceptance checks do you require?

**Expected answer:** Agents may inspect schema and repair invalid queries, but must remain bounded. A syntax error can be repairable; a forbidden query is not an invitation to bypass controls. Use read-only roles, timeouts, row caps, and allowed schema. No model approval can raise privileges. Clarify purchase and date semantics, produce a constrained read-only aggregate query, parameterize tenant, cutoff, and threshold, execute with least privilege and limits, then explain the returned result.

**Deep follow-up:** Use GROUP BY customer and HAVING SUM of eligible amounts above the threshold. Define six calendar months versus a fixed number of days and account for refunds and currency. The authenticated identity supplies tenant scope. A typed query plan is often safer than arbitrary generated SQL. The model summarizes returned rows; it must not invent customers absent from the result. Validate SQL structure and enforce permissions in the database.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for SQL agents; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. You are about to deploy async and concurrency. What design and acceptance checks do you require?

**Expected answer:** async/await lets one thread serve other work while waiting for compatible nonblocking I/O. It does not make CPU-heavy tokenization parallel. Limit concurrent model calls with a semaphore and bound the producer queue. Cancellation should stop outstanding work and release resources; gather with return_exceptions changes how errors propagate. Use bounded asynchronous I/O for independent requests, a shared client, explicit timeouts, and a retry budget. Keep CPU-heavy parsing out of the event loop and respect provider request and token quotas.

**Deep follow-up:** With concurrency 10 and no other bottleneck, 100 five-second requests take roughly 50 seconds rather than 500. Little’s law relates in-flight requests to arrival rate and mean service time. Quotas and tail latency constrain useful concurrency. A semaphore limits active calls but a queue is also needed to bound queued memory. A document ID plus ingestion version makes retried writes idempotent. Measure queue delay separately from provider duration.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Async and concurrency; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. You are about to deploy caching. What design and acceptance checks do you require?

**Expected answer:** Use versioned, authorization-scoped keys and explicit invalidation. Separate source caches, embedding caches, and answer caches. Do not reuse personalized results across users. Cache failures should have a defined fail-open or fail-closed policy based on data sensitivity. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Caching; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. You are about to deploy injection prevention. What design and acceptance checks do you require?

**Expected answer:** Use parameterized values and whitelist identifiers or structured operations. General SQL proposals need proper parsing and allow rules plus database permissions. Do not concatenate user text. Multiple statements, functions, comments, and nested expressions defeat naive string checks. Clarify purchase and date semantics, produce a constrained read-only aggregate query, parameterize tenant, cutoff, and threshold, execute with least privilege and limits, then explain the returned result.

**Deep follow-up:** Use GROUP BY customer and HAVING SUM of eligible amounts above the threshold. Define six calendar months versus a fixed number of days and account for refunds and currency. The authenticated identity supplies tenant scope. A typed query plan is often safer than arbitrary generated SQL. The model summarizes returned rows; it must not invent customers absent from the result. Validate SQL structure and enforce permissions in the database.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Injection prevention; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. You are about to deploy threading and multiprocessing. What design and acceptance checks do you require?

**Expected answer:** Threads can isolate blocking I/O libraries; processes can parallelize CPU work on conventional GIL-enabled CPython. Serialization and process startup cost matter for small jobs. Some numerical libraries release the GIL. Know which runtime you use rather than treating every Python implementation as identical. Use bounded asynchronous I/O for independent requests, a shared client, explicit timeouts, and a retry budget. Keep CPU-heavy parsing out of the event loop and respect provider request and token quotas.

**Deep follow-up:** With concurrency 10 and no other bottleneck, 100 five-second requests take roughly 50 seconds rather than 500. Little’s law relates in-flight requests to arrival rate and mean service time. Quotas and tail latency constrain useful concurrency. A semaphore limits active calls but a queue is also needed to bound queued memory. A document ID plus ingestion version makes retried writes idempotent. Measure queue delay separately from provider duration.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Threading and multiprocessing; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. You are about to deploy streaming and disconnects. What design and acceptance checks do you require?

**Expected answer:** Define start, token, error, and completion events. Propagate cancellation so disconnected clients do not continue costly work unnecessarily. Set buffer limits. A partial answer must not be reported as a completed successful result. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Streaming and disconnects; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
