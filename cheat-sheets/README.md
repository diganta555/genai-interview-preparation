# GenAI interview quick reference

## One-minute distinctions

| Choice | Use when | Main trap |
|---|---|---|
| RAG | Knowledge changes, private data, citations, document ACLs | Relevant retrieval is not proof of supported answers |
| Fine-tuning | Consistent behavior or task style needs adaptation | Retraining is not a policy database or deletion mechanism |
| Workflow | Steps and branches are known | Adding an agent without measurable benefit |
| Agent | Useful action selection varies with observations | Unbounded calls or excessive permissions |
| Exact search | Small baseline and recall verification | Linear search cost at scale |
| ANN | Scale needs latency/memory trade-offs | Unmeasured recall loss |
| Code evaluator | Hard invariants and outcomes are explicit | Keyword match confused with meaning |
| Judge/human | Semantic interpretation is needed | Uncalibrated scores treated as truth |

## Formulas

Cosine = dot(a,b)/(norm(a)norm(b)); undefined for zero vectors. Precision = TP/(TP+FP). Recall = TP/(TP+FN). F1 = 2PR/(P+R). Recall@k = retrieved relevant / known relevant. Reciprocal rank = 1/rank of first relevant result. Mean concurrency ≈ request rate × mean service time. Raw float32 vector bytes = vector count × dimensions × 4. Token cost = input tokens × input rate + output tokens × output rate, with rate units matched correctly.

## Debugging sequence

Capture input and versions; locate the first violated contract; compare with a fixed baseline; change one demonstrated cause; replay; add regression evidence. Check parsing and permissions before tuning prompts.

## Security essentials

Identity and permissions live in trusted code. Retrieved text is data. Tools are narrow and validated. SQL values are parameterized. Consequential operations require idempotency and any required approval. Cache keys include tenant, ACL, source, prompt, and model scope. Never put secrets in Git or model context.

## Interview answer structure

State the approach in one sentence. Explain the mechanism. Give a concrete scenario. Discuss trade-offs. Explain a failure and how it is measured. State implementation scope honestly.

For details, follow the module index in the root README.
