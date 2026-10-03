# Round 8 answer key

Open only after answering each question.

## 1. You are about to deploy requirements. What design and acceptance checks do you require?

**Expected answer:** Clarify user roles, document types, actions, languages, freshness, citations, and allowed mistakes. Functional requirements describe behavior; non-functional requirements describe latency, availability, security, and cost. Explicit assumptions are better than invented scale. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Requirements; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy apis and contracts. What design and acceptance checks do you require?

**Expected answer:** Define ingestion jobs, status endpoints, queries, conversation IDs, and response evidence. Use pagination, idempotency keys, and structured error codes. Streaming requires an event contract. Version external contracts and keep internal provider details out of product APIs. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for APIs and contracts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy database and search. What design and acceptance checks do you require?

**Expected answer:** Relational tables hold users, ACLs, source versions, jobs, and audit records. Object storage holds originals. Vector indexes hold derived search representations. Do not make a vector database the only authoritative record of documents or permissions. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Database and search; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy caching and queues. What design and acceptance checks do you require?

**Expected answer:** Cache safe repeat operations with tenant and version scope. Queue slow ingestion and long-running workflows. Use deduplication, backpressure, retries, dead-letter handling, and status tracking. Define how partial completion becomes visible. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Caching and queues; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy model layer. What design and acceptance checks do you require?

**Expected answer:** Use provider adapters with capability checks, budgets, and controlled fallback. Track model and prompt configuration. A fallback may not support tools or structured output. Preserve response semantics and do not quietly degrade permissions. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Model layer; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy scaling. What design and acceptance checks do you require?

**Expected answer:** Size active users and request rate rather than registered users alone. Estimate vector count, token volume, concurrency, and worker throughput. Horizontal API scaling does not remove provider quotas. Use load balancing and separate ingestion from latency-sensitive queries. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Scaling; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy reliability. What design and acceptance checks do you require?

**Expected answer:** Set total and stage deadlines, classify retryable failures, and stop cascades with circuit breakers and admission control. Define degraded modes and escalation. Cache outages, DB failures, and ambiguous tool outcomes need different handling. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Reliability; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy security and observability. What design and acceptance checks do you require?

**Expected answer:** Authorize retrieval and tools using authenticated identities. Protect PII in traces, use secrets management, and audit actions. Observe quality alongside latency and errors. An available service giving unsupported or unauthorized answers is still failing its purpose. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Security and observability; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy cost and trade-offs. What design and acceptance checks do you require?

**Expected answer:** Compare cost per completed task and operations overhead. Discuss managed versus self-hosted search, model size, reranking, chunk count, and caching. Explain why a simpler baseline may be sufficient. State what evidence would trigger a design change. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Cost and trade-offs; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy eight designs. What design and acceptance checks do you require?

**Expected answer:** The separate system-design directory contains worked designs for a chat service, enterprise RAG, support automation, PDF QA, coding assistance, SQL copilot, document intelligence, and multi-agent research. Each changes requirements and failure boundaries rather than only swapping the product name. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Eight designs; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. After a release, requirements behaves differently on the same user requests. How would you investigate?

**Expected answer:** Clarify user roles, document types, actions, languages, freshness, citations, and allowed mistakes. Functional requirements describe behavior; non-functional requirements describe latency, availability, security, and cost. Explicit assumptions are better than invented scale. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Requirements; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. After a release, apis and contracts behaves differently on the same user requests. How would you investigate?

**Expected answer:** Define ingestion jobs, status endpoints, queries, conversation IDs, and response evidence. Use pagination, idempotency keys, and structured error codes. Streaming requires an event contract. Version external contracts and keep internal provider details out of product APIs. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for APIs and contracts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. After a release, database and search behaves differently on the same user requests. How would you investigate?

**Expected answer:** Relational tables hold users, ACLs, source versions, jobs, and audit records. Object storage holds originals. Vector indexes hold derived search representations. Do not make a vector database the only authoritative record of documents or permissions. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Database and search; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. After a release, caching and queues behaves differently on the same user requests. How would you investigate?

**Expected answer:** Cache safe repeat operations with tenant and version scope. Queue slow ingestion and long-running workflows. Use deduplication, backpressure, retries, dead-letter handling, and status tracking. Define how partial completion becomes visible. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Caching and queues; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. After a release, model layer behaves differently on the same user requests. How would you investigate?

**Expected answer:** Use provider adapters with capability checks, budgets, and controlled fallback. Track model and prompt configuration. A fallback may not support tools or structured output. Preserve response semantics and do not quietly degrade permissions. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Model layer; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. After a release, scaling behaves differently on the same user requests. How would you investigate?

**Expected answer:** Size active users and request rate rather than registered users alone. Estimate vector count, token volume, concurrency, and worker throughput. Horizontal API scaling does not remove provider quotas. Use load balancing and separate ingestion from latency-sensitive queries. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Scaling; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. After a release, reliability behaves differently on the same user requests. How would you investigate?

**Expected answer:** Set total and stage deadlines, classify retryable failures, and stop cascades with circuit breakers and admission control. Define degraded modes and escalation. Cache outages, DB failures, and ambiguous tool outcomes need different handling. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Reliability; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. After a release, security and observability behaves differently on the same user requests. How would you investigate?

**Expected answer:** Authorize retrieval and tools using authenticated identities. Protect PII in traces, use secrets management, and audit actions. Observe quality alongside latency and errors. An available service giving unsupported or unauthorized answers is still failing its purpose. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Security and observability; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. After a release, cost and trade-offs behaves differently on the same user requests. How would you investigate?

**Expected answer:** Compare cost per completed task and operations overhead. Discuss managed versus self-hosted search, model size, reranking, chunk count, and caching. Explain why a simpler baseline may be sufficient. State what evidence would trigger a design change. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Cost and trade-offs; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. After a release, eight designs behaves differently on the same user requests. How would you investigate?

**Expected answer:** The separate system-design directory contains worked designs for a chat service, enterprise RAG, support automation, PDF QA, coding assistance, SQL copilot, document intelligence, and multi-agent research. Each changes requirements and failure boundaries rather than only swapping the product name. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Eight designs; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
