# Round 3 answer key

Open only after answering each question.

## 1. You are about to deploy tokenization. What design and acceptance checks do you require?

**Expected answer:** Tokenizers map text to token IDs using learned subword vocabularies or related methods. A token is not always a word; different languages have different token counts. Tokenizer and model vocabulary must match. Chunk limits measured in characters are not model token limits. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Tokenization; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy architecture and inference. What design and acceptance checks do you require?

**Expected answer:** Many chat models are decoder transformers, but architectures vary. Inference uses trained parameters to generate outputs. Parameter count alone does not predict task quality. Distinguish model quality from service properties such as quotas, residency, uptime, and latency. Measure cost per successful task by model and stage. Inspect unused output tokens, repetitive context, failed retries, and simple tasks using oversized models. Evaluate routing, caching, and shorter context against a fixed quality baseline.

**Deep follow-up:** Estimate input and output cost from actual billed token categories, including cached input or reasoning categories where relevant. Build quality-versus-cost experiments before changing traffic. A 40% reduction from ₹5 lakh is ₹2 lakh, but reduced API cost may be offset by engineering or infrastructure. Separate eligible cached requests from personalized requests and enforce tenant scoping. Publish savings only after measurement over representative traffic.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Architecture and inference; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy zero-shot and few-shot. What design and acceptance checks do you require?

**Expected answer:** Zero-shot gives instructions without examples; few-shot adds representative input-output pairs. Examples improve consistency but consume context and can bias the output. Include ambiguous and abstention examples, not only easy successes. Keep examples separate from the final input. Provide current authorized policy excerpts, require citations to supported claims, define an abstention or escalation path, and validate policy references. Test unsupported and contradictory cases instead of relying on stronger wording alone.

**Deep follow-up:** The prompt should explicitly distinguish trusted policy instructions from customer text and retrieved content. Bind each policy excerpt to a stable version and source ID. Use a schema for answer, cited IDs, and escalation reason. Validate cited IDs and review whether the evidence entails the claim; ID presence alone is insufficient. Tool permissions must prevent refunds without explicit business authorization and, where needed, human approval.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Zero-shot and few-shot; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy token embeddings and positions. What design and acceptance checks do you require?

**Expected answer:** Each token ID indexes a learned embedding. Position information distinguishes order, using learned positions, sinusoidal encodings, rotary methods, or other designs. Rotary position embeddings transform query and key representations according to position. Different architectures do not all use the original sinusoidal scheme. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Token embeddings and positions; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy tokens and context window. What design and acceptance checks do you require?

**Expected answer:** The input, conversation history, tool messages, and generated output share context constraints according to the provider’s accounting rules. Reserve output space before packing retrieved documents. Long context can contain the right evidence while the model still misses it. Count tokens with the relevant tokenizer when available. Measure cost per successful task by model and stage. Inspect unused output tokens, repetitive context, failed retries, and simple tasks using oversized models. Evaluate routing, caching, and shorter context against a fixed quality baseline.

**Deep follow-up:** Estimate input and output cost from actual billed token categories, including cached input or reasoning categories where relevant. Build quality-versus-cost experiments before changing traffic. A 40% reduction from ₹5 lakh is ₹2 lakh, but reduced API cost may be offset by engineering or infrastructure. Separate eligible cached requests from personalized requests and enforce tenant scoping. Publish savings only after measurement over representative traffic.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Tokens and context window; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy reasoning concepts. What design and acceptance checks do you require?

**Expected answer:** Multi-step tasks can benefit from decomposition, intermediate calculations, and verifiable plans. Ask for concise explanations and evidence rather than private hidden chain-of-thought. A model’s stated reasoning is not guaranteed to describe its actual internal computation. Validate intermediate facts with tools where possible. Provide current authorized policy excerpts, require citations to supported claims, define an abstention or escalation path, and validate policy references. Test unsupported and contradictory cases instead of relying on stronger wording alone.

**Deep follow-up:** The prompt should explicitly distinguish trusted policy instructions from customer text and retrieved content. Bind each policy excerpt to a stable version and source ID. Use a schema for answer, cited IDs, and escalation reason. Validate cited IDs and review whether the evidence entails the claim; ID presence alone is insufficient. Tool permissions must prevent refunds without explicit business authorization and, where needed, human approval.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Reasoning concepts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy query key value. What design and acceptance checks do you require?

**Expected answer:** Project each representation into Q, K, and V. Query-key compatibility determines attention weights; those weights combine values. A useful analogy is a search request, an index label, and returned content, but the actual computation is learned matrix multiplication, not an external database lookup. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Query key value; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy temperature top-k top-p. What design and acceptance checks do you require?

**Expected answer:** Temperature rescales logits; lower values usually concentrate probability. Top-k restricts candidate count and top-p restricts cumulative probability mass. Not every API supports every parameter. Low temperature is not a truth guarantee and should not replace evaluation. Measure cost per successful task by model and stage. Inspect unused output tokens, repetitive context, failed retries, and simple tasks using oversized models. Evaluate routing, caching, and shorter context against a fixed quality baseline.

**Deep follow-up:** Estimate input and output cost from actual billed token categories, including cached input or reasoning categories where relevant. Build quality-versus-cost experiments before changing traffic. A 40% reduction from ₹5 lakh is ₹2 lakh, but reduced API cost may be offset by engineering or infrastructure. Separate eligible cached requests from personalized requests and enforce tenant scoping. Publish savings only after measurement over representative traffic.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Temperature top-k top-p; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy role prompting. What design and acceptance checks do you require?

**Expected answer:** A role can set tone and domain expectations but does not grant real expertise or system permissions. Replace vague instructions like act as an expert with explicit criteria and evidence requirements. Define escalation behavior for unsupported requests. Provide current authorized policy excerpts, require citations to supported claims, define an abstention or escalation path, and validate policy references. Test unsupported and contradictory cases instead of relying on stronger wording alone.

**Deep follow-up:** The prompt should explicitly distinguish trusted policy instructions from customer text and retrieved content. Bind each policy excerpt to a stable version and source ID. Use a schema for answer, cited IDs, and escalation reason. Validate cited IDs and review whether the evidence entails the claim; ID presence alone is insufficient. Tool permissions must prevent refunds without explicit business authorization and, where needed, human approval.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Role prompting; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy scaled dot-product attention. What design and acceptance checks do you require?

**Expected answer:** Attention(Q,K,V) = softmax(QKᵀ/√d_k + mask)V. Scaling controls logit magnitude as dimension grows. Masked positions receive effectively negative infinity before softmax. Normalize over the key positions for each query. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Scaled dot-product attention; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy max tokens and stopping. What design and acceptance checks do you require?

**Expected answer:** An output cap bounds generated length and cost. Truncation can produce incomplete JSON or mid-sentence answers. Inspect finish reasons and validate completeness. Use task-specific budgets; one huge default wastes resources on simple classification. Measure cost per successful task by model and stage. Inspect unused output tokens, repetitive context, failed retries, and simple tasks using oversized models. Evaluate routing, caching, and shorter context against a fixed quality baseline.

**Deep follow-up:** Estimate input and output cost from actual billed token categories, including cached input or reasoning categories where relevant. Build quality-versus-cost experiments before changing traffic. A 40% reduction from ₹5 lakh is ₹2 lakh, but reduced API cost may be offset by engineering or infrastructure. Separate eligible cached requests from personalized requests and enforce tenant scoping. Publish savings only after measurement over representative traffic.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Max tokens and stopping; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. You are about to deploy structured prompts. What design and acceptance checks do you require?

**Expected answer:** Use clear sections for task, context, constraints, examples, and output. XML-style tags or JSON can make boundaries readable but do not prevent prompt injection by themselves. Encode untrusted content and cap its length. Keep policy text outside retrieved document content. Provide current authorized policy excerpts, require citations to supported claims, define an abstention or escalation path, and validate policy references. Test unsupported and contradictory cases instead of relying on stronger wording alone.

**Deep follow-up:** The prompt should explicitly distinguish trusted policy instructions from customer text and retrieved content. Bind each policy excerpt to a stable version and source ID. Use a schema for answer, cited IDs, and escalation reason. Validate cited IDs and review whether the evidence entails the claim; ID presence alone is insufficient. Tool permissions must prevent refunds without explicit business authorization and, where needed, human approval.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Structured prompts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. You are about to deploy multi-head attention. What design and acceptance checks do you require?

**Expected answer:** Different heads use different learned projections and can represent different relations. Concatenate head outputs and apply an output projection. More heads are not automatically better. Grouped-query and multi-query variants share key/value projections to reduce inference cache cost. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Multi-head attention; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. You are about to deploy messages and roles. What design and acceptance checks do you require?

**Expected answer:** System or developer instructions describe behavior, user messages express requests, assistant messages carry responses, and tool messages return observations. Provider schemas differ. Role labels are not authorization controls: tool code and data stores must enforce permissions. Measure cost per successful task by model and stage. Inspect unused output tokens, repetitive context, failed retries, and simple tasks using oversized models. Evaluate routing, caching, and shorter context against a fixed quality baseline.

**Deep follow-up:** Estimate input and output cost from actual billed token categories, including cached input or reasoning categories where relevant. Build quality-versus-cost experiments before changing traffic. A 40% reduction from ₹5 lakh is ₹2 lakh, but reduced API cost may be offset by engineering or infrastructure. Separate eligible cached requests from personalized requests and enforce tenant scoping. Publish savings only after measurement over representative traffic.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Messages and roles; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. You are about to deploy output constraints. What design and acceptance checks do you require?

**Expected answer:** Specify the schema, supported citation IDs, null behavior, and maximum length. Validate the result using Pydantic or another runtime checker. Retry schema repair only within a budget. Never accept a malicious operation just because its JSON is valid. Provide current authorized policy excerpts, require citations to supported claims, define an abstention or escalation path, and validate policy references. Test unsupported and contradictory cases instead of relying on stronger wording alone.

**Deep follow-up:** The prompt should explicitly distinguish trusted policy instructions from customer text and retrieved content. Bind each policy excerpt to a stable version and source ID. Use a schema for answer, cited IDs, and escalation reason. Validate cited IDs and review whether the evidence entails the claim; ID presence alone is insufficient. Tool permissions must prevent refunds without explicit business authorization and, where needed, human approval.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Output constraints; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. You are about to deploy feed-forward networks. What design and acceptance checks do you require?

**Expected answer:** Each token representation passes through a position-wise nonlinear network, often expanding then contracting the hidden dimension. Attention mixes positions; the feed-forward sublayer transforms features. Mixture-of-experts architectures selectively activate subsets of feed-forward parameters. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Feed-forward networks; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. You are about to deploy structured output. What design and acceptance checks do you require?

**Expected answer:** Schema-constrained generation can improve syntactic reliability. Runtime validation still checks types, required fields, ranges, and allowed values. A well-formed object can still contain invented facts. Business invariants need independent verification. Measure cost per successful task by model and stage. Inspect unused output tokens, repetitive context, failed retries, and simple tasks using oversized models. Evaluate routing, caching, and shorter context against a fixed quality baseline.

**Deep follow-up:** Estimate input and output cost from actual billed token categories, including cached input or reasoning categories where relevant. Build quality-versus-cost experiments before changing traffic. A 40% reduction from ₹5 lakh is ₹2 lakh, but reduced API cost may be offset by engineering or infrastructure. Separate eligible cached requests from personalized requests and enforce tenant scoping. Publish savings only after measurement over representative traffic.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Structured output; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. You are about to deploy templates. What design and acceptance checks do you require?

**Expected answer:** A template fills a stable instruction skeleton with request-specific data. Treat user values as data, not executable template expressions. Version the template with its output schema and evaluation dataset. Do not interpolate secrets into a prompt. Provide current authorized policy excerpts, require citations to supported claims, define an abstention or escalation path, and validate policy references. Test unsupported and contradictory cases instead of relying on stronger wording alone.

**Deep follow-up:** The prompt should explicitly distinguish trusted policy instructions from customer text and retrieved content. Bind each policy excerpt to a stable version and source ID. Use a schema for answer, cited IDs, and escalation reason. Validate cited IDs and review whether the evidence entails the claim; ID presence alone is insufficient. Tool permissions must prevent refunds without explicit business authorization and, where needed, human approval.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Templates; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. You are about to deploy residual connections and normalization. What design and acceptance checks do you require?

**Expected answer:** Residual paths add earlier representations to sublayer outputs, improving gradient flow. LayerNorm or RMSNorm stabilizes scale. Pre-norm and post-norm place normalization differently; real models differ. These operations influence training stability, not just cosmetic implementation style. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Residual connections and normalization; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. You are about to deploy function and tool calling. What design and acceptance checks do you require?

**Expected answer:** The model proposes a tool name and arguments; the application executes the call. Match result messages to call IDs. Validate tool permissions and input before execution. Tool calling provides an interface, not permission to perform arbitrary side effects. Measure cost per successful task by model and stage. Inspect unused output tokens, repetitive context, failed retries, and simple tasks using oversized models. Evaluate routing, caching, and shorter context against a fixed quality baseline.

**Deep follow-up:** Estimate input and output cost from actual billed token categories, including cached input or reasoning categories where relevant. Build quality-versus-cost experiments before changing traffic. A 40% reduction from ₹5 lakh is ₹2 lakh, but reduced API cost may be offset by engineering or infrastructure. Separate eligible cached requests from personalized requests and enforce tenant scoping. Publish savings only after measurement over representative traffic.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Function and tool calling; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
