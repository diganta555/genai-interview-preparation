# Round 6 answer key

Open only after answering each question.

## 1. You are about to deploy normal model call. What design and acceptance checks do you require?

**Expected answer:** A normal call produces text or multimodal output. Use it for summarization and discussion when no external operation is required. Text mentioning a function name is not a real authorized call. Never parse free text into arbitrary code execution. Structured output returns validated-shaped data. A tool call proposes an external operation that the application must authorize and execute. Both use schemas, but only a permitted executed operation changes external state.

**Deep follow-up:** A schema is a syntax and type contract. It cannot establish that an employee exists, the caller can read salary, or a payment is approved. The execution layer validates those facts against trusted systems. Tool-result messages carry observations associated with call IDs; the model uses them to formulate a response. Agents add repeated selection and observation around this protocol, so they require independent budgets and stop conditions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Normal model call; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy state. What design and acceptance checks do you require?

**Expected answer:** State is the data carried through the graph, commonly described with TypedDict or another supported schema. Include only what nodes need: query, evidence, decisions, and counters. Keep trusted identity outside model-editable fields. Define reducers carefully for list accumulation or parallel updates. Add explicit budgets, repeated-call detection, and a no-progress condition. Route exhausted or invalid states to a final partial response or escalation. Keep the recursion limit as an additional safeguard.

**Deep follow-up:** Include step_count, tool fingerprints, elapsed time, and cumulative token cost in trusted orchestration state. A tool fingerprint includes name and canonical arguments, but repeated read calls may be legitimate if the state changed; define task-specific progress. Validate the routing decision before choosing an edge. Persist checkpoint state per authorized thread. For side effects, store a separate operation ID so checkpoint replay cannot duplicate business actions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for State; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy llm chain workflow agent. What design and acceptance checks do you require?

**Expected answer:** An LLM generates outputs; a chain composes fixed calls; a workflow branches using explicit rules; an agent lets a model choose actions. An autonomous agent can operate with reduced human intervention. These categories overlap in implementation, so define the actual control boundary. Avoid one when steps are fixed, a deterministic API already solves the problem, or variable model decisions add risk without measurable benefit. A bounded workflow is usually easier to test, operate, and explain.

**Deep follow-up:** Choose agentic control only for uncertainty that deterministic orchestration cannot cheaply resolve. Compare against a baseline using completion accuracy, action permissions, unnecessary calls, duration, and cost. A model may choose search queries while a workflow owns source fetching, validation, and publishing. This hybrid reduces the surface where probabilistic decisions can cause damage. Production readiness requires observing behavior under adversarial and failed-tool conditions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for LLM chain workflow agent; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy conversation and short-term memory. What design and acceptance checks do you require?

**Expected answer:** Conversation history supports pronouns and ongoing tasks. Keep histories separate by authenticated user and session. Bound tokens by trimming or summarizing while retaining unresolved tool messages and decisions. A global list creates both privacy and correctness failures. Use memory for approved conversational context and preferences. Retrieve current business facts from the authoritative database, with permissions and timestamps. Remembered text should not become an unverified source of truth.

**Deep follow-up:** Distinguish task state, derived summaries, profiles, and authoritative records. Each has different update frequency, correctness requirements, and retention. A profile saying the user prefers concise answers can be memory; their current account balance should come from the ledger. If storing derived facts, retain evidence, version, expiry, and correction controls. Reauthorization is needed whenever remembered context triggers a new privileged operation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Conversation and short-term memory; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy supervisor and workers. What design and acceptance checks do you require?

**Expected answer:** A supervisor routes tasks to workers and collects results. Workers should have narrow responsibilities, schemas, and budgets. The supervisor must not silently grant broader permissions. Test misrouting, unavailable workers, and incomplete results. Agreement is not verification. The agents may share model biases or rely on the same incorrect summary. Verify claims against independent original sources and preserve provenance.

**Deep follow-up:** Check the evidence graph: did each worker access independent sources, or repeat one generated statement? If the fact checker only read the summarizer’s output, it had no external basis for judgment. Require claim-to-source-span mappings and separate evidence collection from synthesis. Use deterministic checks for dates, totals, and schema where possible. Evaluate whether multi-agent orchestration improves correctness enough to justify extra tokens and latency.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Supervisor and workers; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy structured output. What design and acceptance checks do you require?

**Expected answer:** Structured output returns data conforming to a requested schema. It may be an extraction result, not a request for action. A structured invoice object should be stored only after validation. Distinguish generating fields from authorizing a payment. Structured output returns validated-shaped data. A tool call proposes an external operation that the application must authorize and execute. Both use schemas, but only a permitted executed operation changes external state.

**Deep follow-up:** A schema is a syntax and type contract. It cannot establish that an employee exists, the caller can read salary, or a payment is approved. The execution layer validates those facts against trusted systems. Tool-result messages carry observations associated with call IDs; the model uses them to formulate a response. Agents add repeated selection and observation around this protocol, so they require independent budgets and stop conditions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Structured output; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy nodes and updates. What design and acceptance checks do you require?

**Expected answer:** A node reads state and returns updates. Avoid mutating shared nested state in place; return explicit changes. A model node, retrieval node, and validation node have different contracts. Unit-test them independently before testing the graph. Add explicit budgets, repeated-call detection, and a no-progress condition. Route exhausted or invalid states to a final partial response or escalation. Keep the recursion limit as an additional safeguard.

**Deep follow-up:** Include step_count, tool fingerprints, elapsed time, and cumulative token cost in trusted orchestration state. A tool fingerprint includes name and canonical arguments, but repeated read calls may be legitimate if the state changed; define task-specific progress. Validate the routing decision before choosing an edge. Persist checkpoint state per authorized thread. For side effects, store a separate operation ID so checkpoint replay cannot duplicate business actions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Nodes and updates; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy planning. What design and acceptance checks do you require?

**Expected answer:** A plan decomposes a goal into actions. Validate dependencies, required permissions, and budgets before execution. Plans can be wrong or stale. Short bounded replanning after new evidence is often safer than an enormous initial plan. Avoid one when steps are fixed, a deterministic API already solves the problem, or variable model decisions add risk without measurable benefit. A bounded workflow is usually easier to test, operate, and explain.

**Deep follow-up:** Choose agentic control only for uncertainty that deterministic orchestration cannot cheaply resolve. Compare against a baseline using completion accuracy, action permissions, unnecessary calls, duration, and cost. A model may choose search queries while a workflow owns source fetching, validation, and publishing. This hybrid reduces the surface where probabilistic decisions can cause damage. Production readiness requires observing behavior under adversarial and failed-tool conditions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Planning; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy long-term memory. What design and acceptance checks do you require?

**Expected answer:** Persist selected information across sessions when the use case and permissions allow it. Store what is useful rather than everything the model sees. Include source, timestamp, retention, and user controls. Revalidate claims that may change. Use memory for approved conversational context and preferences. Retrieve current business facts from the authoritative database, with permissions and timestamps. Remembered text should not become an unverified source of truth.

**Deep follow-up:** Distinguish task state, derived summaries, profiles, and authoritative records. Each has different update frequency, correctness requirements, and retention. A profile saying the user prefers concise answers can be memory; their current account balance should come from the ledger. If storing derived facts, retain evidence, version, expiry, and correction controls. Reauthorization is needed whenever remembered context triggers a new privileged operation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Long-term memory; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy specialist agents. What design and acceptance checks do you require?

**Expected answer:** A specialist may handle retrieval, SQL planning, summarization, or fact checking. Domain prompts do not create genuine expertise. Evaluate each specialist and the integrated result. A shared underlying model may reproduce the same error across roles. Agreement is not verification. The agents may share model biases or rely on the same incorrect summary. Verify claims against independent original sources and preserve provenance.

**Deep follow-up:** Check the evidence graph: did each worker access independent sources, or repeat one generated statement? If the fact checker only read the summarizer’s output, it had no external basis for judgment. Require claim-to-source-span mappings and separate evidence collection from synthesis. Use deterministic checks for dates, totals, and schema where possible. Evaluate whether multi-agent orchestration improves correctness enough to justify extra tokens and latency.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Specialist agents; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy function versus tool calling. What design and acceptance checks do you require?

**Expected answer:** Function calling generally refers to calling application functions; tool calling is the broader provider terminology and may include other tool types. Provider formats vary. Document your internal protocol explicitly rather than pretending terminology is universal. Structured output returns validated-shaped data. A tool call proposes an external operation that the application must authorize and execute. Both use schemas, but only a permitted executed operation changes external state.

**Deep follow-up:** A schema is a syntax and type contract. It cannot establish that an employee exists, the caller can read salary, or a payment is approved. The execution layer validates those facts against trusted systems. Tool-result messages carry observations associated with call IDs; the model uses them to formulate a response. Agents add repeated selection and observation around this protocol, so they require independent budgets and stop conditions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Function versus tool calling; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. You are about to deploy edges start end. What design and acceptance checks do you require?

**Expected answer:** START identifies entry and END termination. Static edges model fixed transitions. A simple graph can normalize a query then retrieve then answer. Keep the graph readable: a diagram should match implemented transitions, including error paths. Add explicit budgets, repeated-call detection, and a no-progress condition. Route exhausted or invalid states to a final partial response or escalation. Keep the recursion limit as an additional safeguard.

**Deep follow-up:** Include step_count, tool fingerprints, elapsed time, and cumulative token cost in trusted orchestration state. A tool fingerprint includes name and canonical arguments, but repeated read calls may be legitimate if the state changed; define task-specific progress. Validate the routing decision before choosing an edge. Persist checkpoint state per authorized thread. For side effects, store a separate operation ID so checkpoint replay cannot duplicate business actions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Edges START END; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. You are about to deploy reasoning and observation. What design and acceptance checks do you require?

**Expected answer:** The agent conditions its next choice on tool observations and state. Expose concise action rationales and evidence, not hidden chain-of-thought. An observation is untrusted if it comes from a webpage or uploaded file. Validate its source and shape before reuse. Avoid one when steps are fixed, a deterministic API already solves the problem, or variable model decisions add risk without measurable benefit. A bounded workflow is usually easier to test, operate, and explain.

**Deep follow-up:** Choose agentic control only for uncertainty that deterministic orchestration cannot cheaply resolve. Compare against a baseline using completion accuracy, action permissions, unnecessary calls, duration, and cost. A model may choose search queries while a workflow owns source fetching, validation, and publishing. This hybrid reduces the surface where probabilistic decisions can cause damage. Production readiness requires observing behavior under adversarial and failed-tool conditions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Reasoning and observation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. You are about to deploy semantic memory. What design and acceptance checks do you require?

**Expected answer:** Semantic memory stores facts or knowledge-like descriptions. It can help recall preferences, but inferred preferences may be wrong. Distinguish user statements from model inference. Conflicting facts should be resolved through provenance and recency rather than arbitrary vector closeness. Use memory for approved conversational context and preferences. Retrieve current business facts from the authoritative database, with permissions and timestamps. Remembered text should not become an unverified source of truth.

**Deep follow-up:** Distinguish task state, derived summaries, profiles, and authoritative records. Each has different update frequency, correctness requirements, and retention. A profile saying the user prefers concise answers can be memory; their current account balance should come from the ledger. If storing derived facts, retain evidence, version, expiry, and correction controls. Reauthorization is needed whenever remembered context triggers a new privileged operation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Semantic memory; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. You are about to deploy planner executor. What design and acceptance checks do you require?

**Expected answer:** A planner proposes steps; an executor performs permitted actions. Validate the plan through deterministic rules and budget checks. Separate proposing a write from authorizing it. Replanning should use new observations rather than repeat failed steps indefinitely. Agreement is not verification. The agents may share model biases or rely on the same incorrect summary. Verify claims against independent original sources and preserve provenance.

**Deep follow-up:** Check the evidence graph: did each worker access independent sources, or repeat one generated statement? If the fact checker only read the summarizer’s output, it had no external basis for judgment. Require claim-to-source-span mappings and separate evidence collection from synthesis. Use deterministic checks for dates, totals, and schema where possible. Evaluate whether multi-agent orchestration improves correctness enough to justify extra tokens and latency.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Planner executor; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. You are about to deploy decision and arguments. What design and acceptance checks do you require?

**Expected answer:** The model selects from offered tools and proposes arguments. Validate tool name, schema, size, and business rules. Do not accept a new tool name invented by the model. Model-suggested arguments may include fabricated identifiers or unsafe values. Structured output returns validated-shaped data. A tool call proposes an external operation that the application must authorize and execute. Both use schemas, but only a permitted executed operation changes external state.

**Deep follow-up:** A schema is a syntax and type contract. It cannot establish that an employee exists, the caller can read salary, or a payment is approved. The execution layer validates those facts against trusted systems. Tool-result messages carry observations associated with call IDs; the model uses them to formulate a response. Agents add repeated selection and observation around this protocol, so they require independent budgets and stop conditions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Decision and arguments; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. You are about to deploy conditional edges. What design and acceptance checks do you require?

**Expected answer:** A routing function selects the next node from validated state. Use explicit routes such as answer, tool, retry, and escalate. Do not let arbitrary model text become a node name. Test every branch, especially exhausted budgets. Add explicit budgets, repeated-call detection, and a no-progress condition. Route exhausted or invalid states to a final partial response or escalation. Keep the recursion limit as an additional safeguard.

**Deep follow-up:** Include step_count, tool fingerprints, elapsed time, and cumulative token cost in trusted orchestration state. A tool fingerprint includes name and canonical arguments, but repeated read calls may be legitimate if the state changed; define task-specific progress. Validate the routing decision before choosing an edge. Persist checkpoint state per authorized thread. For side effects, store a separate operation ID so checkpoint replay cannot duplicate business actions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Conditional edges; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. You are about to deploy tools. What design and acceptance checks do you require?

**Expected answer:** Provide narrow capabilities rather than unrestricted shell, database, or browser access. Match permissions to the task and caller. A research agent may search public sources but does not need payroll access. Sandbox coding tools and limit egress and filesystem scope. Avoid one when steps are fixed, a deterministic API already solves the problem, or variable model decisions add risk without measurable benefit. A bounded workflow is usually easier to test, operate, and explain.

**Deep follow-up:** Choose agentic control only for uncertainty that deterministic orchestration cannot cheaply resolve. Compare against a baseline using completion accuracy, action permissions, unnecessary calls, duration, and cost. A model may choose search queries while a workflow owns source fetching, validation, and publishing. This hybrid reduces the surface where probabilistic decisions can cause damage. Production readiness requires observing behavior under adversarial and failed-tool conditions.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Tools; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. You are about to deploy episodic memory. What design and acceptance checks do you require?

**Expected answer:** Episodic memory stores events such as a prior support incident and outcome. It can improve future assistance, but old actions are not permission for new actions. Preserve event context and authorization scope. Avoid replaying obsolete solutions automatically. Use memory for approved conversational context and preferences. Retrieve current business facts from the authoritative database, with permissions and timestamps. Remembered text should not become an unverified source of truth.

**Deep follow-up:** Distinguish task state, derived summaries, profiles, and authoritative records. Each has different update frequency, correctness requirements, and retention. A profile saying the user prefers concise answers can be memory; their current account balance should come from the ledger. If storing derived facts, retain evidence, version, expiry, and correction controls. Reauthorization is needed whenever remembered context triggers a new privileged operation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Episodic memory; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. You are about to deploy sequential agents. What design and acceptance checks do you require?

**Expected answer:** Sequential stages are useful when one result depends on another: gather evidence, summarize, verify, answer. Each transformation can lose information. Preserve source spans through all stages. A final editor must not invent facts absent from earlier evidence. Agreement is not verification. The agents may share model biases or rely on the same incorrect summary. Verify claims against independent original sources and preserve provenance.

**Deep follow-up:** Check the evidence graph: did each worker access independent sources, or repeat one generated statement? If the fact checker only read the summarizer’s output, it had no external basis for judgment. Require claim-to-source-span mappings and separate evidence collection from synthesis. Use deterministic checks for dates, totals, and schema where possible. Evaluate whether multi-agent orchestration improves correctness enough to justify extra tokens and latency.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Sequential agents; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
