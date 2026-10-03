# Round 10 answer key

Open only after answering each question.

## 1. You are about to deploy 500000-document design. What design and acceptance checks do you require?

**Expected answer:** Estimate average chunks per document before sizing. Store originals in object storage, metadata and permissions in a relational store, and derived vectors in a versioned search index. Use queues for extraction and embedding, idempotent workers, an activation record for versions, and dead-letter handling for failed sources. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

**Deep follow-up:** If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for 500000-document design; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy supervisor and workers. What design and acceptance checks do you require?

**Expected answer:** A supervisor routes tasks to workers and collects results. Workers should have narrow responsibilities, schemas, and budgets. The supervisor must not silently grant broader permissions. Test misrouting, unavailable workers, and incomplete results. Agreement is not verification. The agents may share model biases or rely on the same incorrect summary. Verify claims against independent original sources and preserve provenance.

**Deep follow-up:** Check the evidence graph: did each worker access independent sources, or repeat one generated statement? If the fact checker only read the summarizer’s output, it had no external basis for judgment. Require claim-to-source-span mappings and separate evidence collection from synthesis. Use deterministic checks for dates, totals, and schema where possible. Evaluate whether multi-agent orchestration improves correctness enough to justify extra tokens and latency.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Supervisor and workers; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy pretraining. What design and acceptance checks do you require?

**Expected answer:** Pretraining learns broad representations and next-token patterns from large datasets. It requires substantial data and compute and is usually outside a small application team’s scope. It does not mean memorized facts remain current or accessible with reliable attribution. I would usually retrieve current authorized policies with RAG. Fine-tuning can improve how the model follows the task or formats answers, but is not a reliable policy versioning, deletion, or citation mechanism.

**Deep follow-up:** Fine-tuning can encode behavior but knowledge updates require new training and may not overwrite every outdated fact. RAG preserves source provenance and supports document-level permission changes. Use tuning when a measured behavioral problem remains after strong prompts and enough high-quality examples exist. Compare operational costs: dataset maintenance, GPU time, serving, evaluation, and rollback versus retrieval infrastructure. Assess combinations under identical benchmarks.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Pretraining; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy correctness and relevance. What design and acceptance checks do you require?

**Expected answer:** Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Correctness and relevance; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy authentication and authorization. What design and acceptance checks do you require?

**Expected answer:** Authentication establishes identity; authorization decides permitted actions and data. Verify tokens through a trusted identity provider with issuer, audience, signature, and expiry checks. Never trust a tenant header supplied by the user as proof of membership. Treat PDF text as untrusted evidence. Restrict tools, filesystem scope, egress, and caller permissions in code. The answer generator should have no capability to upload confidential files merely because text requests it.

**Deep follow-up:** Classify data sources by trust and design capability boundaries accordingly. Retrieval applies ACLs, tool execution authorizes each operation, and outbound network access follows an allowlist. Do not include secrets in the model context. Bind approvals to exact requests. Test indirect injection end to end with a malicious source and verify no unauthorized action occurs, regardless of whether the model verbally resists or complies.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Authentication and authorization; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy cost accounting. What design and acceptance checks do you require?

**Expected answer:** Break spend into model input, output, embeddings, reranking, tools, storage, and infrastructure. Include failed requests and retries. Attribute by tenant and workflow. Use current provider rate cards at deployment time; lab prices are fictional assumptions. Create a stage-level baseline, remove waste, test cheaper routing and permission-scoped caching, then roll out gradually under quality and latency gates. Target ₹2 lakh savings but validate it on representative traffic.

**Deep follow-up:** First separate traffic volume changes from cost-per-task changes. Estimate opportunities from cache-eligible requests, output length, oversized model use, duplicated context, and retry frequency. Experiment one change at a time and compare held-out critical slices. Savings compound differently than adding percentages: a 20% reduction followed by another 25% reduction yields 40% total. Monitor human escalation and failed-task costs before reporting business impact.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Cost accounting; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy requirements. What design and acceptance checks do you require?

**Expected answer:** Clarify user roles, document types, actions, languages, freshness, citations, and allowed mistakes. Functional requirements describe behavior; non-functional requirements describe latency, availability, security, and cost. Explicit assumptions are better than invented scale. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Requirements; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy api architecture. What design and acceptance checks do you require?

**Expected answer:** Separate transport validation, authorization, application logic, retrieval, model adapters, and persistence. Keep external provider schemas behind adapters. FastAPI and Pydantic fit request contracts; async dependencies need nonblocking libraries. Share clients through application lifecycle management. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for API architecture; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy irrelevant results. What design and acceptance checks do you require?

**Expected answer:** Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Compare exact search on a small labeled sample. Fix missing extraction or incorrect ACLs before tuning scores. Separate weak candidate retrieval from weak reranking. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

**Deep follow-up:** If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Irrelevant results; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy specialist agents. What design and acceptance checks do you require?

**Expected answer:** A specialist may handle retrieval, SQL planning, summarization, or fact checking. Domain prompts do not create genuine expertise. Evaluate each specialist and the integrated result. A shared underlying model may reproduce the same error across roles. Agreement is not verification. The agents may share model biases or rely on the same incorrect summary. Verify claims against independent original sources and preserve provenance.

**Deep follow-up:** Check the evidence graph: did each worker access independent sources, or repeat one generated statement? If the fact checker only read the summarizer’s output, it had no external basis for judgment. Require claim-to-source-span mappings and separate evidence collection from synthesis. Use deterministic checks for dates, totals, and schema where possible. Evaluate whether multi-agent orchestration improves correctness enough to justify extra tokens and latency.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Specialist agents; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy instruction tuning and sft. What design and acceptance checks do you require?

**Expected answer:** Supervised fine-tuning trains on task inputs paired with desired outputs. It can improve style, formatting, domain behavior, or repeated task patterns. Good demonstrations need consistent labels and permissions. Keep validation and test examples separate from training. I would usually retrieve current authorized policies with RAG. Fine-tuning can improve how the model follows the task or formats answers, but is not a reliable policy versioning, deletion, or citation mechanism.

**Deep follow-up:** Fine-tuning can encode behavior but knowledge updates require new training and may not overwrite every outdated fact. RAG preserves source provenance and supports document-level permission changes. Use tuning when a measured behavioral problem remains after strong prompts and enough high-quality examples exist. Compare operational costs: dataset maintenance, GPU time, serving, evaluation, and rollback versus retrieval infrastructure. Assess combinations under identical benchmarks.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Instruction tuning and SFT; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. You are about to deploy faithfulness groundedness hallucination. What design and acceptance checks do you require?

**Expected answer:** Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Faithfulness groundedness hallucination; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. You are about to deploy prompt injection and indirect injection. What design and acceptance checks do you require?

**Expected answer:** A user or retrieved source may instruct the model to ignore policy or exfiltrate data. Treat documents, webpages, memory, and tool output as untrusted. Delimiters help readability but cannot enforce isolation. Restrict permissions even if the model follows malicious instructions. Treat PDF text as untrusted evidence. Restrict tools, filesystem scope, egress, and caller permissions in code. The answer generator should have no capability to upload confidential files merely because text requests it.

**Deep follow-up:** Classify data sources by trust and design capability boundaries accordingly. Retrieval applies ACLs, tool execution authorizes each operation, and outbound network access follows an allowlist. Do not include secrets in the model context. Bind approvals to exact requests. Test indirect injection end to end with a malicious source and verify no unauthorized action occurs, regardless of whether the model verbally resists or complies.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Prompt injection and indirect injection; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. You are about to deploy model routing. What design and acceptance checks do you require?

**Expected answer:** Route easy tasks to cheaper suitable models and hard tasks to stronger ones when measured quality justifies it. Use observable features or a calibrated classifier. A complexity estimate is not proof of quality. Keep fallback and escalation policies explicit. Create a stage-level baseline, remove waste, test cheaper routing and permission-scoped caching, then roll out gradually under quality and latency gates. Target ₹2 lakh savings but validate it on representative traffic.

**Deep follow-up:** First separate traffic volume changes from cost-per-task changes. Estimate opportunities from cache-eligible requests, output length, oversized model use, duplicated context, and retry frequency. Experiment one change at a time and compare held-out critical slices. Savings compound differently than adding percentages: a 20% reduction followed by another 25% reduction yields 40% total. Monitor human escalation and failed-task costs before reporting business impact.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Model routing; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. You are about to deploy apis and contracts. What design and acceptance checks do you require?

**Expected answer:** Define ingestion jobs, status endpoints, queries, conversation IDs, and response evidence. Use pagination, idempotency keys, and structured error codes. Streaming requires an event contract. Version external contracts and keep internal provider details out of product APIs. Clarify active concurrency and request rates, then size API replicas, queues, storage, provider quotas, and token budgets. Registered user count alone is insufficient. Enforce tenant isolation and load-test representative workflows.

**Deep follow-up:** If one million registered users generate 100 requests per second and mean service time is five seconds, roughly 500 requests are in flight before queueing, by Little’s law. At 3000 input and 500 output tokens per request, provider token throughput can dominate. Use admission control, per-tenant quotas, shared caching where safe, and async ingestion. Plan hot partitions, regional requirements, failure recovery, and SLO-based capacity margins. Validate the assumed workload with measurements.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for APIs and contracts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. You are about to deploy authentication and rate limiting. What design and acceptance checks do you require?

**Expected answer:** Use a real identity provider and derive tenant and role from verified identity. Limit by user, tenant, and workflow cost, with shared state for multi-replica services. Protect both requests per second and token budgets. A local API key is only a development control. Apply bounded backoff, shared admission control, per-tenant quotas, and an overall deadline. Avoid retry storms. Offer a queued, degraded, or explicit retryable result according to the endpoint contract.

**Deep follow-up:** Differentiate request-rate and token-rate limits and honor provider retry headers. A global concurrency cap alone may not regulate tokens per minute. Coordinate quotas across replicas, reserve capacity for critical workflows, and reduce fanout during saturation. Only use fallback models with validated task capabilities and data permissions. Track upstream saturation separately from local queue delay and tell clients whether the task is queued, partial, or failed.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Authentication and rate limiting; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. You are about to deploy correct answer wrong citation. What design and acceptance checks do you require?

**Expected answer:** Track whether citations refer to parent IDs, child IDs, or source spans. A common bug is positional numbering after reranking while generation uses older numbering. Another is cached answer text paired with fresh citations. Bind answer and evidence version as one immutable result. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

**Deep follow-up:** If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Correct answer wrong citation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. You are about to deploy planner executor. What design and acceptance checks do you require?

**Expected answer:** A planner proposes steps; an executor performs permitted actions. Validate the plan through deterministic rules and budget checks. Separate proposing a write from authorizing it. Replanning should use new observations rather than repeat failed steps indefinitely. Agreement is not verification. The agents may share model biases or rely on the same incorrect summary. Verify claims against independent original sources and preserve provenance.

**Deep follow-up:** Check the evidence graph: did each worker access independent sources, or repeat one generated statement? If the fact checker only read the summarizer’s output, it had no external basis for judgment. Require claim-to-source-span mappings and separate evidence collection from synthesis. Use deterministic checks for dates, totals, and schema where possible. Evaluate whether multi-agent orchestration improves correctness enough to justify extra tokens and latency.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Planner executor; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. You are about to deploy lora. What design and acceptance checks do you require?

**Expected answer:** LoRA trains low-rank updates to selected weight matrices while freezing base weights. W becomes W plus a scaled BA update. Rank, target modules, and learning rate affect adaptation. It reduces trainable parameters but still needs base-model storage, activations, and optimizer resources. I would usually retrieve current authorized policies with RAG. Fine-tuning can improve how the model follows the task or formats answers, but is not a reliable policy versioning, deletion, or citation mechanism.

**Deep follow-up:** Fine-tuning can encode behavior but knowledge updates require new training and may not overwrite every outdated fact. RAG preserves source provenance and supports document-level permission changes. Use tuning when a measured behavioral problem remains after strong prompts and enough high-quality examples exist. Compare operational costs: dataset maintenance, GPU time, serving, evaluation, and rollback versus retrieval infrastructure. Assess combinations under identical benchmarks.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for LoRA; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. You are about to deploy retrieval evaluation. What design and acceptance checks do you require?

**Expected answer:** Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Retrieval evaluation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
