# Round 9 answer key

Open only after answering each question.

## 1. You are about to deploy authentication and authorization. What design and acceptance checks do you require?

**Expected answer:** Authentication establishes identity; authorization decides permitted actions and data. Verify tokens through a trusted identity provider with issuer, audience, signature, and expiry checks. Never trust a tenant header supplied by the user as proof of membership. Treat PDF text as untrusted evidence. Restrict tools, filesystem scope, egress, and caller permissions in code. The answer generator should have no capability to upload confidential files merely because text requests it.

**Deep follow-up:** Classify data sources by trust and design capability boundaries accordingly. Retrieval applies ACLs, tool execution authorizes each operation, and outbound network access follows an allowlist. Do not include secrets in the model context. Bind approvals to exact requests. Test indirect injection end to end with a malicious source and verify no unauthorized action occurs, regardless of whether the model verbally resists or complies.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Authentication and authorization; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy cost accounting. What design and acceptance checks do you require?

**Expected answer:** Break spend into model input, output, embeddings, reranking, tools, storage, and infrastructure. Include failed requests and retries. Attribute by tenant and workflow. Use current provider rate cards at deployment time; lab prices are fictional assumptions. Create a stage-level baseline, remove waste, test cheaper routing and permission-scoped caching, then roll out gradually under quality and latency gates. Target ₹2 lakh savings but validate it on representative traffic.

**Deep follow-up:** First separate traffic volume changes from cost-per-task changes. Estimate opportunities from cache-eligible requests, output length, oversized model use, duplicated context, and retry frequency. Experiment one change at a time and compare held-out critical slices. Savings compound differently than adding percentages: a 20% reduction followed by another 25% reduction yields 40% total. Monitor human escalation and failed-task costs before reporting business impact.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Cost accounting; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy api architecture. What design and acceptance checks do you require?

**Expected answer:** Separate transport validation, authorization, application logic, retrieval, model adapters, and persistence. Keep external provider schemas behind adapters. FastAPI and Pydantic fit request contracts; async dependencies need nonblocking libraries. Share clients through application lifecycle management. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for API architecture; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy docker images. What design and acceptance checks do you require?

**Expected answer:** Build from a supported base, install explicit dependencies, copy only needed files, and run as a non-root user. Keep secrets out of build arguments and image layers. Use .dockerignore. Pin resolved packages and production image digests after testing. Check the service hostname, internal port, network, readiness, credentials, and logs. Inside an API container, localhost is the API container, not the PostgreSQL service.

**Deep follow-up:** Use the Compose service name such as postgres and the database’s container port, not the host-mapped port. Verify startup order does not hide readiness races. Check environment precedence, credentials, and persisted volume initialization. A changed password variable does not necessarily change an already initialized database password. Add bounded connection retry and distinguish credential failures from transient startup failures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Docker images; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy s3. What design and acceptance checks do you require?

**Expected answer:** Store original documents and versioned derived artifacts in object storage. Use least-privilege access, encryption, retention, and controlled upload paths. Presigned URLs are temporary access grants and must be scoped and protected. Events can trigger asynchronous ingestion. Give each teammate their own authorized SSO or federated identity with temporary credentials, or expose a company-authenticated model gateway whose workload role invokes Bedrock. Enforce least privilege, quotas, and audit logs.

**Deep follow-up:** Local SDK calls can use the standard AWS credential chain after SSO login under an approved profile. Production uses a task, instance, or workload role. If only a small component needs model access, a central gateway can narrow model IDs, token budgets, and data policy while clients authenticate through company identity. The gateway is a service with availability and rate-limit responsibilities; it should not become an unauthenticated key-sharing proxy.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for S3; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy prompt injection and indirect injection. What design and acceptance checks do you require?

**Expected answer:** A user or retrieved source may instruct the model to ignore policy or exfiltrate data. Treat documents, webpages, memory, and tool output as untrusted. Delimiters help readability but cannot enforce isolation. Restrict permissions even if the model follows malicious instructions. Treat PDF text as untrusted evidence. Restrict tools, filesystem scope, egress, and caller permissions in code. The answer generator should have no capability to upload confidential files merely because text requests it.

**Deep follow-up:** Classify data sources by trust and design capability boundaries accordingly. Retrieval applies ACLs, tool execution authorizes each operation, and outbound network access follows an allowlist. Do not include secrets in the model context. Bind approvals to exact requests. Test indirect injection end to end with a malicious source and verify no unauthorized action occurs, regardless of whether the model verbally resists or complies.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Prompt injection and indirect injection; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy model routing. What design and acceptance checks do you require?

**Expected answer:** Route easy tasks to cheaper suitable models and hard tasks to stronger ones when measured quality justifies it. Use observable features or a calibrated classifier. A complexity estimate is not proof of quality. Keep fallback and escalation policies explicit. Create a stage-level baseline, remove waste, test cheaper routing and permission-scoped caching, then roll out gradually under quality and latency gates. Target ₹2 lakh savings but validate it on representative traffic.

**Deep follow-up:** First separate traffic volume changes from cost-per-task changes. Estimate opportunities from cache-eligible requests, output length, oversized model use, duplicated context, and retry frequency. Experiment one change at a time and compare held-out critical slices. Savings compound differently than adding percentages: a 20% reduction followed by another 25% reduction yields 40% total. Monitor human escalation and failed-task costs before reporting business impact.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Model routing; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy authentication and rate limiting. What design and acceptance checks do you require?

**Expected answer:** Use a real identity provider and derive tenant and role from verified identity. Limit by user, tenant, and workflow cost, with shared state for multi-replica services. Protect both requests per second and token budgets. A local API key is only a development control. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Authentication and rate limiting; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy compose services. What design and acceptance checks do you require?

**Expected answer:** Define API, frontend, PostgreSQL, Redis, and Qdrant as separate services in the included local stack. Use internal service names rather than localhost between containers. Local ports bind to loopback to reduce accidental exposure. Dependencies being started does not prove the application is ready. Check the service hostname, internal port, network, readiness, credentials, and logs. Inside an API container, localhost is the API container, not the PostgreSQL service.

**Deep follow-up:** Use the Compose service name such as postgres and the database’s container port, not the host-mapped port. Verify startup order does not hide readiness races. Check environment precedence, credentials, and persisted volume initialization. A changed password variable does not necessarily change an already initialized database password. Add bounded connection retry and distinguish credential failures from transient startup failures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Compose services; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy ec2. What design and acceptance checks do you require?

**Expected answer:** EC2 offers virtual machines, useful for custom serving or specialized infrastructure. You own patching, scaling, availability, and GPU utilization. Attach instance roles for AWS access instead of embedding static keys. Model self-hosting needs realistic memory and throughput benchmarks. Give each teammate their own authorized SSO or federated identity with temporary credentials, or expose a company-authenticated model gateway whose workload role invokes Bedrock. Enforce least privilege, quotas, and audit logs.

**Deep follow-up:** Local SDK calls can use the standard AWS credential chain after SSO login under an approved profile. Production uses a task, instance, or workload role. If only a small component needs model access, a central gateway can narrow model IDs, token budgets, and data policy while clients authenticate through company identity. The gateway is a service with availability and rate-limit responsibilities; it should not become an unauthenticated key-sharing proxy.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for EC2; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy jailbreaks. What design and acceptance checks do you require?

**Expected answer:** Jailbreaks attempt to defeat behavioral restrictions. Test multiple languages, encodings, role-play, and long-context attacks. Detection will be imperfect. Design so a compromised answer generator cannot obtain forbidden data or perform unauthorized actions. Treat PDF text as untrusted evidence. Restrict tools, filesystem scope, egress, and caller permissions in code. The answer generator should have no capability to upload confidential files merely because text requests it.

**Deep follow-up:** Classify data sources by trust and design capability boundaries accordingly. Retrieval applies ACLs, tool execution authorizes each operation, and outbound network access follows an allowlist. Do not include secrets in the model context. Bind approvals to exact requests. Test indirect injection end to end with a malicious source and verify no unauthorized action occurs, regardless of whether the model verbally resists or complies.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Jailbreaks; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. You are about to deploy prompt compression. What design and acceptance checks do you require?

**Expected answer:** Remove duplicate instructions, obsolete history, and irrelevant evidence before compressing useful content. Compression can drop exceptions, dates, units, and safety constraints. Evaluate preservation of key facts. Saving input tokens may add another model call and erase savings. Create a stage-level baseline, remove waste, test cheaper routing and permission-scoped caching, then roll out gradually under quality and latency gates. Target ₹2 lakh savings but validate it on representative traffic.

**Deep follow-up:** First separate traffic volume changes from cost-per-task changes. Estimate opportunities from cache-eligible requests, output length, oversized model use, duplicated context, and retry frequency. Experiment one change at a time and compare held-out critical slices. Savings compound differently than adding percentages: a 20% reduction followed by another 25% reduction yields 40% total. Monitor human escalation and failed-task costs before reporting business impact.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Prompt compression; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. You are about to deploy retries and timeouts. What design and acceptance checks do you require?

**Expected answer:** Set connect, read, total stage, and request deadlines. Respect provider retry hints and use exponential backoff with jitter. Retry transient failures only within a total budget. Never allow nested retry layers to multiply unnoticed. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Retries and timeouts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. You are about to deploy fastapi process. What design and acceptance checks do you require?

**Expected answer:** Uvicorn serves ASGI requests. Worker counts affect memory and shared-state assumptions. An in-memory index is separate in each worker; it is not a distributed persistent store. Use managed process orchestration and graceful shutdown in production. Check the service hostname, internal port, network, readiness, credentials, and logs. Inside an API container, localhost is the API container, not the PostgreSQL service.

**Deep follow-up:** Use the Compose service name such as postgres and the database’s container port, not the host-mapped port. Verify startup order does not hide readiness races. Check environment precedence, credentials, and persisted volume initialization. A changed password variable does not necessarily change an already initialized database password. Add bounded connection retry and distinguish credential failures from transient startup failures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for FastAPI process; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. You are about to deploy ecs and eks. What design and acceptance checks do you require?

**Expected answer:** ECS runs containers with managed orchestration; EKS runs managed Kubernetes control planes. Use task or workload IAM identities with narrow permissions. Neither removes application reliability or data design work. EKS usually demands more platform expertise. Give each teammate their own authorized SSO or federated identity with temporary credentials, or expose a company-authenticated model gateway whose workload role invokes Bedrock. Enforce least privilege, quotas, and audit logs.

**Deep follow-up:** Local SDK calls can use the standard AWS credential chain after SSO login under an approved profile. Production uses a task, instance, or workload role. If only a small component needs model access, a central gateway can narrow model IDs, token budgets, and data policy while clients authenticate through company identity. The gateway is a service with availability and rate-limit responsibilities; it should not become an unauthenticated key-sharing proxy.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for ECS and EKS; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. You are about to deploy data leakage and pii. What design and acceptance checks do you require?

**Expected answer:** Minimize data sent to models, logs, and evaluators. Redact where appropriate and enforce data residency and retention requirements. Regex redaction catches only some patterns. Entity context and unstructured identifiers may need more careful processing and review. Treat PDF text as untrusted evidence. Restrict tools, filesystem scope, egress, and caller permissions in code. The answer generator should have no capability to upload confidential files merely because text requests it.

**Deep follow-up:** Classify data sources by trust and design capability boundaries accordingly. Retrieval applies ACLs, tool execution authorizes each operation, and outbound network access follows an allowlist. Do not include secrets in the model context. Bind approvals to exact requests. Test indirect injection end to end with a malicious source and verify no unauthorized action occurs, regardless of whether the model verbally resists or complies.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Data leakage and PII; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. You are about to deploy smaller and local models. What design and acceptance checks do you require?

**Expected answer:** Smaller models can reduce latency or cost for narrow tasks. Self-hosting adds GPU, idle capacity, ops, licensing, and reliability costs. Benchmark at expected utilization and language mix. Do not compare API token price with GPU cost while ignoring engineering effort. Create a stage-level baseline, remove waste, test cheaper routing and permission-scoped caching, then roll out gradually under quality and latency gates. Target ₹2 lakh savings but validate it on representative traffic.

**Deep follow-up:** First separate traffic volume changes from cost-per-task changes. Estimate opportunities from cache-eligible requests, output length, oversized model use, duplicated context, and retry frequency. Experiment one change at a time and compare held-out critical slices. Savings compound differently than adding percentages: a 20% reduction followed by another 25% reduction yields 40% total. Monitor human escalation and failed-task costs before reporting business impact.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Smaller and local models; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. You are about to deploy circuit breakers. What design and acceptance checks do you require?

**Expected answer:** Open a breaker after a measured failure threshold, then probe recovery cautiously. Breakers reduce calls to an unhealthy dependency but must not permanently block a recovered service. Separate circuit state by dependency and failure class. Test transitions and half-open behavior. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Circuit breakers; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. You are about to deploy persistent volumes. What design and acceptance checks do you require?

**Expected answer:** Volumes keep database state beyond a container restart. They are not backups. Test database backup, restore, and schema compatibility. Do not delete volumes casually while studying commands; local data can be lost. Check the service hostname, internal port, network, readiness, credentials, and logs. Inside an API container, localhost is the API container, not the PostgreSQL service.

**Deep follow-up:** Use the Compose service name such as postgres and the database’s container port, not the host-mapped port. Verify startup order does not hide readiness races. Check environment precedence, credentials, and persisted volume initialization. A changed password variable does not necessarily change an already initialized database password. Add bounded connection retry and distinguish credential failures from transient startup failures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Persistent volumes; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. You are about to deploy lambda. What design and acceptance checks do you require?

**Expected answer:** Lambda suits bounded event processing and lightweight endpoints when its runtime and resource constraints fit. Long model streams, large parsing jobs, or GPU workloads may need other compute. Check current service limits before selecting it. Design retries and duplicate events safely. Give each teammate their own authorized SSO or federated identity with temporary credentials, or expose a company-authenticated model gateway whose workload role invokes Bedrock. Enforce least privilege, quotas, and audit logs.

**Deep follow-up:** Local SDK calls can use the standard AWS credential chain after SSO login under an approved profile. Production uses a task, instance, or workload role. If only a small component needs model access, a central gateway can narrow model IDs, token budgets, and data policy while clients authenticate through company identity. The gateway is a service with availability and rate-limit responsibilities; it should not become an unauthenticated key-sharing proxy.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Lambda; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
