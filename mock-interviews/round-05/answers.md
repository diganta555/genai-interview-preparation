# Round 5 answer key

Open only after answering each question.

## 1. You are about to deploy prompts and templates. What design and acceptance checks do you require?

**Expected answer:** A prompt template formats trusted instructions and request data into messages. Use ChatPromptTemplate for role-aware chat formatting. Why: repeatable task contracts. Where: classification and grounded answering. Example: prompt.invoke({question: ...}). Follow-up: what happens when user input contains template syntax? Keep user values as data and verify formatted messages in tests. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Prompts and templates; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy models and provider switching. What design and acceptance checks do you require?

**Expected answer:** A chat model accepts messages and returns an AI message, often with usage and tool-call metadata. init_chat_model and provider integration packages offer a common surface. Why: isolate vendor changes. Where: model routing. Follow-up: can every model support the same schema? No; capability checks and adapter contract tests are required. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Models and provider switching; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy output parsers. What design and acceptance checks do you require?

**Expected answer:** Parsers convert model output into a useful form, such as text or a validated object. StrOutputParser extracts string content in a simple text pipeline. Why: downstream code needs contracts. Where: a summary endpoint. Common mistake: assuming parsing proves factual correctness. Schema validation and business validation remain separate. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Output parsers; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy runnable and lcel. What design and acceptance checks do you require?

**Expected answer:** Runnable supports invoke, ainvoke, batch, and stream style composition. LCEL uses the pipe operator to connect compatible stages. Why: explicit reusable pipelines. Where: prompt to model to parser. Follow-up: what if one stage blocks? Async composition cannot turn a synchronous blocking SDK into nonblocking I/O automatically. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Runnable and LCEL; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy chains and boundaries. What design and acceptance checks do you require?

**Expected answer:** A chain is a fixed composition of steps. Prefer inspectable pipelines over deprecated monolithic patterns. Why: deterministic control flow. Where: retrieval then answering. Common mistake: reaching for an agent when a fixed pipeline covers the task. Record per-stage inputs and outputs with redaction. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Chains and boundaries; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy retrievers and vector stores. What design and acceptance checks do you require?

**Expected answer:** A vector store manages stored vectors; a retriever exposes a query-to-documents interface. Convert supported stores with as_retriever and configure search options. Why: hide storage-specific lookup. Where: RAG. Follow-up: where do ACLs belong? In trusted retrieval code and the underlying permission system, not in user-selected filter arguments. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Retrievers and vector stores; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy loaders and splitters. What design and acceptance checks do you require?

**Expected answer:** Loaders produce Document objects with text and metadata. Text splitters create chunks while retaining provenance. Modern installations use separate packages such as langchain_text_splitters. Why: modular ingestion. Where: PDF RAG. Common mistake: importing an obsolete path or losing page metadata during custom transformations. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Loaders and splitters; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy callbacks and tracing. What design and acceptance checks do you require?

**Expected answer:** Callbacks expose events such as model start, tool end, and errors; LangSmith can collect traces. Why: see where latency and failures occur. Where: production incidents. Follow-up: can traces leak PII? Yes; redact and control retention. Trace IDs should connect application, retrieval, and provider activity. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Callbacks and tracing; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy memory concepts. What design and acceptance checks do you require?

**Expected answer:** History is message state, not a magical truth store. Keep sessions scoped, trim to a budget, and use durable persistence where needed. Why: conversational continuity. Where: support sessions. Common mistake: one global conversation list for all users. Store factual records in an authoritative database. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Memory concepts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy tools and agents. What design and acceptance checks do you require?

**Expected answer:** Tools are typed capabilities; create_agent supplies a model-driven loop around tools. Why: variable task steps. Where: constrained support automation. Follow-up: who executes and authorizes the tool? The application. Keep step limits, timeouts, and approval rules outside model text. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Tools and agents; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy llamaindex comparison. What design and acceptance checks do you require?

**Expected answer:** LlamaIndex offers document ingestion, indexing, and query-oriented abstractions, including VectorStoreIndex. LangChain offers broad composition and agent interfaces; LangGraph exposes explicit stateful orchestration. Compare the actual task and extension needs. Framework choice does not remove retrieval, evaluation, permission, or operational design responsibilities. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for LlamaIndex comparison; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. After a release, prompts and templates behaves differently on the same user requests. How would you investigate?

**Expected answer:** A prompt template formats trusted instructions and request data into messages. Use ChatPromptTemplate for role-aware chat formatting. Why: repeatable task contracts. Where: classification and grounded answering. Example: prompt.invoke({question: ...}). Follow-up: what happens when user input contains template syntax? Keep user values as data and verify formatted messages in tests. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Prompts and templates; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. After a release, models and provider switching behaves differently on the same user requests. How would you investigate?

**Expected answer:** A chat model accepts messages and returns an AI message, often with usage and tool-call metadata. init_chat_model and provider integration packages offer a common surface. Why: isolate vendor changes. Where: model routing. Follow-up: can every model support the same schema? No; capability checks and adapter contract tests are required. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Models and provider switching; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. After a release, output parsers behaves differently on the same user requests. How would you investigate?

**Expected answer:** Parsers convert model output into a useful form, such as text or a validated object. StrOutputParser extracts string content in a simple text pipeline. Why: downstream code needs contracts. Where: a summary endpoint. Common mistake: assuming parsing proves factual correctness. Schema validation and business validation remain separate. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Output parsers; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. After a release, runnable and lcel behaves differently on the same user requests. How would you investigate?

**Expected answer:** Runnable supports invoke, ainvoke, batch, and stream style composition. LCEL uses the pipe operator to connect compatible stages. Why: explicit reusable pipelines. Where: prompt to model to parser. Follow-up: what if one stage blocks? Async composition cannot turn a synchronous blocking SDK into nonblocking I/O automatically. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Runnable and LCEL; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. After a release, chains and boundaries behaves differently on the same user requests. How would you investigate?

**Expected answer:** A chain is a fixed composition of steps. Prefer inspectable pipelines over deprecated monolithic patterns. Why: deterministic control flow. Where: retrieval then answering. Common mistake: reaching for an agent when a fixed pipeline covers the task. Record per-stage inputs and outputs with redaction. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Chains and boundaries; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. After a release, retrievers and vector stores behaves differently on the same user requests. How would you investigate?

**Expected answer:** A vector store manages stored vectors; a retriever exposes a query-to-documents interface. Convert supported stores with as_retriever and configure search options. Why: hide storage-specific lookup. Where: RAG. Follow-up: where do ACLs belong? In trusted retrieval code and the underlying permission system, not in user-selected filter arguments. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Retrievers and vector stores; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. After a release, loaders and splitters behaves differently on the same user requests. How would you investigate?

**Expected answer:** Loaders produce Document objects with text and metadata. Text splitters create chunks while retaining provenance. Modern installations use separate packages such as langchain_text_splitters. Why: modular ingestion. Where: PDF RAG. Common mistake: importing an obsolete path or losing page metadata during custom transformations. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Loaders and splitters; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. After a release, callbacks and tracing behaves differently on the same user requests. How would you investigate?

**Expected answer:** Callbacks expose events such as model start, tool end, and errors; LangSmith can collect traces. Why: see where latency and failures occur. Where: production incidents. Follow-up: can traces leak PII? Yes; redact and control retention. Trace IDs should connect application, retrieval, and provider activity. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Callbacks and tracing; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. After a release, memory concepts behaves differently on the same user requests. How would you investigate?

**Expected answer:** History is message state, not a magical truth store. Keep sessions scoped, trim to a budget, and use durable persistence where needed. Why: conversational continuity. Where: support sessions. Common mistake: one global conversation list for all users. Store factual records in an authoritative database. Use a plain SDK for a small direct call, LCEL for a fixed composed pipeline, LangGraph for explicit stateful control flow, and LlamaIndex when its document indexing and query abstractions fit the problem.

**Deep follow-up:** Framework overhead must earn its place through maintainability, tracing, persistence, or reusable integrations. A plain SDK can still support robust production behavior. LCEL is convenient for composable stages; LangGraph is appropriate for loops, branching, checkpointing, and approvals. LlamaIndex is an alternative abstraction for data-oriented applications, not a substitute for source quality and authorization. Evaluate team familiarity, dependency surface, and version stability.

**Ask next:** What if the aggregate score is unchanged?

**Rubric:** Accurate mechanism for Memory concepts; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
