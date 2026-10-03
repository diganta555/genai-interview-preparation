# Top 50 Rag

Answer aloud before revealing the sections. Repeated concepts use different engineering lenses. Code pointers are implementation references, not complete bespoke solutions for every scenario.

## Question 1: You are about to deploy document loading. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply document loading in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Scanned PDFs need OCR; text extraction alone can return empty pages. Preserve table headers and units. Treat uploaded files as untrusted data with size and parsing limits. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Scanned PDFs need OCR; text extraction alone can return empty pages. Preserve table headers and units. Treat uploaded files as untrusted data with size and parsing limits.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating document loading as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 2: You are about to deploy 500000-document design. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply 500000-document design in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Estimate average chunks per document before sizing. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Estimate average chunks per document before sizing. Store originals in object storage, metadata and permissions in a relational store, and derived vectors in a versioned search index. Use queues for extraction and embedding, idempotent workers, an activation record for versions, and dead-letter handling for failed sources. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Estimate average chunks per document before sizing. Store originals in object storage, metadata and permissions in a relational store, and derived vectors in a versioned search index. Use queues for extraction and embedding, idempotent workers, an activation record for versions, and dead-letter handling for failed sources.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating 500000-document design as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 3: You are about to deploy recursive chunking. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply recursive chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Overlap carries boundary context but increases storage and duplicate retrieval. Token-aware limits are preferable when model budgets are tight. Evaluate several sizes rather than declaring 1000/200 universally best. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Overlap carries boundary context but increases storage and duplicate retrieval. Token-aware limits are preferable when model budgets are tight. Evaluate several sizes rather than declaring 1000/200 universally best.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating recursive chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 4: You are about to deploy irrelevant results. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply irrelevant results in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Compare exact search on a small labeled sample. Fix missing extraction or incorrect ACLs before tuning scores. Separate weak candidate retrieval from weak reranking. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Compare exact search on a small labeled sample. Fix missing extraction or incorrect ACLs before tuning scores. Separate weak candidate retrieval from weak reranking.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating irrelevant results as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 5: You are about to deploy semantic chunking. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply semantic chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Use boundaries based on content transitions, often from embedding changes. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Use boundaries based on content transitions, often from embedding changes. This can preserve coherent meaning but costs preprocessing and introduces thresholds. A semantic boundary is not necessarily the right factual citation boundary. Compare against simpler structure-aware splitting. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Use boundaries based on content transitions, often from embedding changes. This can preserve coherent meaning but costs preprocessing and introduces thresholds. A semantic boundary is not necessarily the right factual citation boundary. Compare against simpler structure-aware splitting.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating semantic chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 6: You are about to deploy correct answer wrong citation. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply correct answer wrong citation in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Track whether citations refer to parent IDs, child IDs, or source spans. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Track whether citations refer to parent IDs, child IDs, or source spans. A common bug is positional numbering after reranking while generation uses older numbering. Another is cached answer text paired with fresh citations. Bind answer and evidence version as one immutable result. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Track whether citations refer to parent IDs, child IDs, or source spans. A common bug is positional numbering after reranking while generation uses older numbering. Another is cached answer text paired with fresh citations. Bind answer and evidence version as one immutable result.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating correct answer wrong citation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 7: You are about to deploy parent-child chunking. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply parent-child chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Index small children for precise retrieval and supply their larger parent sections for context. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Index small children for precise retrieval and supply their larger parent sections for context. Keep both IDs and avoid returning an entire oversized parent. Enforce permissions on parent and child together. Deduplicate parents when multiple children match. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Index small children for precise retrieval and supply their larger parent sections for context. Keep both IDs and avoid returning an entire oversized parent. Enforce permissions on parent and child together. Deduplicate parents when multiple children match.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating parent-child chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 8: You are about to deploy correct context wrong answer. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply correct context wrong answer in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Decompose multi-hop questions and use tools for arithmetic. Relevance does not imply completeness. Abstain when all required evidence is not present. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Decompose multi-hop questions and use tools for arithmetic. Relevance does not imply completeness. Abstain when all required evidence is not present.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating correct context wrong answer as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 9: You are about to deploy metadata and ingestion. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply metadata and ingestion in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Assign stable IDs with document version, chunk offset, language, title, and access attributes. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Assign stable IDs with document version, chunk offset, language, title, and access attributes. Persist the original source separately from derived text and vectors. Re-ingestion should atomically activate a complete new version rather than expose half an update. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Assign stable IDs with document version, chunk offset, language, title, and access attributes. Persist the original source separately from derived text and vectors. Re-ingestion should atomically activate a complete new version rather than expose half an update.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating metadata and ingestion as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 10: You are about to deploy variable answers. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply variable answers in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Lower temperature reduces one source of variation. Version configurations and use canonical evidence ordering, but do not promise universal determinism. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Lower temperature reduces one source of variation. Version configurations and use canonical evidence ordering, but do not promise universal determinism.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating variable answers as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 11: You are about to deploy retrieval and rewriting. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply retrieval and rewriting in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Retrieve candidates using the current question and relevant conversational context. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Retrieve candidates using the current question and relevant conversational context. Query rewriting can resolve pronouns but can also introduce unsupported assumptions. Keep the original question and log the rewrite. Multi-query retrieval increases coverage at the expense of extra calls and duplicate candidates. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Retrieve candidates using the current question and relevant conversational context. Query rewriting can resolve pronouns but can also introduce unsupported assumptions. Keep the original question and log the rewrite. Multi-query retrieval increases coverage at the expense of extra calls and duplicate candidates.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating retrieval and rewriting as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 12: You are about to deploy multi-query and decomposition. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply multi-query and decomposition in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Create paraphrases or subquestions to improve coverage. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Create paraphrases or subquestions to improve coverage. Merge and deduplicate candidates before reranking. Constrain rewriting so user identifiers, dates, and amounts survive. Every extra query consumes latency, tokens, and quota; compare improvement per added cost. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Create paraphrases or subquestions to improve coverage. Merge and deduplicate candidates before reranking. Constrain rewriting so user identifiers, dates, and amounts survive. Every extra query consumes latency, tokens, and quota; compare improvement per added cost.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating multi-query and decomposition as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 13: You are about to deploy hybrid reranking and compression. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply hybrid reranking and compression in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Fuse lexical and dense candidates, then apply a cross-encoder or other reranker to a bounded set. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Fuse lexical and dense candidates, then apply a cross-encoder or other reranker to a bounded set. Contextual compression extracts relevant portions, but must preserve provenance and avoid changing meaning. Relevance filtering removes weak evidence; thresholds need calibration. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Fuse lexical and dense candidates, then apply a cross-encoder or other reranker to a bounded set. Contextual compression extracts relevant portions, but must preserve provenance and avoid changing meaning. Relevance filtering removes weak evidence; thresholds need calibration.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating hybrid reranking and compression as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 14: You are about to deploy reranking and relevance. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply reranking and relevance in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Rerank a candidate set larger than the final context. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Rerank a candidate set larger than the final context. Cross-encoders score query-document pairs jointly and can improve ranking. They cannot recover an absent relevant document. Calibrate acceptance thresholds for the actual domain and evaluate false abstentions. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Rerank a candidate set larger than the final context. Cross-encoders score query-document pairs jointly and can improve ranking. They cannot recover an absent relevant document. Calibrate acceptance thresholds for the actual domain and evaluate false abstentions.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating reranking and relevance as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 15: You are about to deploy prompt and answer. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply prompt and answer in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Pack evidence within a token budget, use explicit source IDs, and define an abstention policy. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Pack evidence within a token budget, use explicit source IDs, and define an abstention policy. Separate retrieved content from trusted instructions. Ask for claims supported by evidence and validate the output shape. The application retains responsibility for authorization. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Pack evidence within a token budget, use explicit source IDs, and define an abstention policy. Separate retrieved content from trusted instructions. Ask for claims supported by evidence and validate the output shape. The application retains responsibility for authorization.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating prompt and answer as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 16: You are about to deploy freshness and lifecycle. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply freshness and lifecycle in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Use change tracking, source checksums, tombstones, and index version aliases. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Use change tracking, source checksums, tombstones, and index version aliases. Delete or replace all chunks belonging to an outdated version. Permissions may change more often than content; recheck authorization against the source of truth. Define acceptable ingestion lag. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Use change tracking, source checksums, tombstones, and index version aliases. Delete or replace all chunks belonging to an outdated version. Permissions may change more often than content; recheck authorization against the source of truth. Define acceptable ingestion lag.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating freshness and lifecycle as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 17: You are about to deploy citations. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply citations in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Tie each citation to immutable document version and source span. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Tie each citation to immutable document version and source span. Validate that the ID exists in the supplied evidence and assess whether the span supports the claim. A correct URL attached to an unsupported answer is still a bad citation. Do not fabricate page numbers. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Tie each citation to immutable document version and source span. Validate that the ID exists in the supplied evidence and assess whether the span supports the claim. A correct URL attached to an unsupported answer is still a bad citation. Do not fabricate page numbers.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating citations as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 18: You are about to deploy evaluation experiments. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply evaluation experiments in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Separate retrieval, context selection, generation, and citation experiments. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Separate retrieval, context selection, generation, and citation experiments. Use paired comparisons on the same queries and slice by language, PDF type, and question complexity. Prevent prompt tuning on the final test set. Record confidence and inspect failures, not only aggregate averages. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Separate retrieval, context selection, generation, and citation experiments. Use paired comparisons on the same queries and slice by language, PDF type, and question complexity. Prevent prompt tuning on the final test set. Record confidence and inspect failures, not only aggregate averages.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating evaluation experiments as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 19: You are about to deploy testing and hallucination reduction. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply testing and hallucination reduction in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Measure parsing coverage, chunk coverage, Recall@k, ranking, answer correctness, faithfulness, abstention, and citation quality separately. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Measure parsing coverage, chunk coverage, Recall@k, ranking, answer correctness, faithfulness, abstention, and citation quality separately. Add missing-answer, contradictory-source, outdated-source, and injection tests. Better retrieval cannot fix every generation failure, and better generation cannot invent missing evidence. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Measure parsing coverage, chunk coverage, Recall@k, ranking, answer correctness, faithfulness, abstention, and citation quality separately. Add missing-answer, contradictory-source, outdated-source, and injection tests. Better retrieval cannot fix every generation failure, and better generation cannot invent missing evidence.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating testing and hallucination reduction as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 20: You are about to deploy scaling and failure. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply scaling and failure in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Bound query fanout and context length. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Bound query fanout and context length. Cache only permission-scoped, versioned results. Maintain partial-service behavior if reranking fails, but label the degraded path and validate quality. Load-test mixed ingestion and queries and test restore from snapshots. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Bound query fanout and context length. Cache only permission-scoped, versioned results. Maintain partial-service behavior if reranking fails, but label the degraded path and validate quality. Load-test mixed ingestion and queries and test restore from snapshots.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating scaling and failure as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 21: After a release, document loading behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply document loading in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Scanned PDFs need OCR; text extraction alone can return empty pages. Preserve table headers and units. Treat uploaded files as untrusted data with size and parsing limits. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Scanned PDFs need OCR; text extraction alone can return empty pages. Preserve table headers and units. Treat uploaded files as untrusted data with size and parsing limits.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating document loading as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 22: After a release, 500000-document design behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply 500000-document design in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Estimate average chunks per document before sizing. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Estimate average chunks per document before sizing. Store originals in object storage, metadata and permissions in a relational store, and derived vectors in a versioned search index. Use queues for extraction and embedding, idempotent workers, an activation record for versions, and dead-letter handling for failed sources. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Estimate average chunks per document before sizing. Store originals in object storage, metadata and permissions in a relational store, and derived vectors in a versioned search index. Use queues for extraction and embedding, idempotent workers, an activation record for versions, and dead-letter handling for failed sources.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating 500000-document design as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 23: After a release, recursive chunking behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply recursive chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Overlap carries boundary context but increases storage and duplicate retrieval. Token-aware limits are preferable when model budgets are tight. Evaluate several sizes rather than declaring 1000/200 universally best. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Overlap carries boundary context but increases storage and duplicate retrieval. Token-aware limits are preferable when model budgets are tight. Evaluate several sizes rather than declaring 1000/200 universally best.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating recursive chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 24: After a release, irrelevant results behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply irrelevant results in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Compare exact search on a small labeled sample. Fix missing extraction or incorrect ACLs before tuning scores. Separate weak candidate retrieval from weak reranking. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Compare exact search on a small labeled sample. Fix missing extraction or incorrect ACLs before tuning scores. Separate weak candidate retrieval from weak reranking.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating irrelevant results as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 25: After a release, semantic chunking behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply semantic chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Use boundaries based on content transitions, often from embedding changes. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Use boundaries based on content transitions, often from embedding changes. This can preserve coherent meaning but costs preprocessing and introduces thresholds. A semantic boundary is not necessarily the right factual citation boundary. Compare against simpler structure-aware splitting. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Use boundaries based on content transitions, often from embedding changes. This can preserve coherent meaning but costs preprocessing and introduces thresholds. A semantic boundary is not necessarily the right factual citation boundary. Compare against simpler structure-aware splitting.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating semantic chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 26: After a release, correct answer wrong citation behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply correct answer wrong citation in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Track whether citations refer to parent IDs, child IDs, or source spans. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Track whether citations refer to parent IDs, child IDs, or source spans. A common bug is positional numbering after reranking while generation uses older numbering. Another is cached answer text paired with fresh citations. Bind answer and evidence version as one immutable result. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Track whether citations refer to parent IDs, child IDs, or source spans. A common bug is positional numbering after reranking while generation uses older numbering. Another is cached answer text paired with fresh citations. Bind answer and evidence version as one immutable result.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating correct answer wrong citation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 27: After a release, parent-child chunking behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply parent-child chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Index small children for precise retrieval and supply their larger parent sections for context. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Index small children for precise retrieval and supply their larger parent sections for context. Keep both IDs and avoid returning an entire oversized parent. Enforce permissions on parent and child together. Deduplicate parents when multiple children match. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Index small children for precise retrieval and supply their larger parent sections for context. Keep both IDs and avoid returning an entire oversized parent. Enforce permissions on parent and child together. Deduplicate parents when multiple children match.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating parent-child chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 28: After a release, correct context wrong answer behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply correct context wrong answer in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Decompose multi-hop questions and use tools for arithmetic. Relevance does not imply completeness. Abstain when all required evidence is not present. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Decompose multi-hop questions and use tools for arithmetic. Relevance does not imply completeness. Abstain when all required evidence is not present.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating correct context wrong answer as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 29: After a release, metadata and ingestion behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply metadata and ingestion in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Assign stable IDs with document version, chunk offset, language, title, and access attributes. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Assign stable IDs with document version, chunk offset, language, title, and access attributes. Persist the original source separately from derived text and vectors. Re-ingestion should atomically activate a complete new version rather than expose half an update. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Assign stable IDs with document version, chunk offset, language, title, and access attributes. Persist the original source separately from derived text and vectors. Re-ingestion should atomically activate a complete new version rather than expose half an update.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating metadata and ingestion as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 30: After a release, variable answers behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply variable answers in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Lower temperature reduces one source of variation. Version configurations and use canonical evidence ordering, but do not promise universal determinism. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Lower temperature reduces one source of variation. Version configurations and use canonical evidence ordering, but do not promise universal determinism.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating variable answers as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 31: After a release, retrieval and rewriting behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply retrieval and rewriting in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Retrieve candidates using the current question and relevant conversational context. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Retrieve candidates using the current question and relevant conversational context. Query rewriting can resolve pronouns but can also introduce unsupported assumptions. Keep the original question and log the rewrite. Multi-query retrieval increases coverage at the expense of extra calls and duplicate candidates. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Retrieve candidates using the current question and relevant conversational context. Query rewriting can resolve pronouns but can also introduce unsupported assumptions. Keep the original question and log the rewrite. Multi-query retrieval increases coverage at the expense of extra calls and duplicate candidates.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating retrieval and rewriting as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 32: After a release, multi-query and decomposition behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply multi-query and decomposition in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Create paraphrases or subquestions to improve coverage. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Create paraphrases or subquestions to improve coverage. Merge and deduplicate candidates before reranking. Constrain rewriting so user identifiers, dates, and amounts survive. Every extra query consumes latency, tokens, and quota; compare improvement per added cost. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Create paraphrases or subquestions to improve coverage. Merge and deduplicate candidates before reranking. Constrain rewriting so user identifiers, dates, and amounts survive. Every extra query consumes latency, tokens, and quota; compare improvement per added cost.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating multi-query and decomposition as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 33: After a release, hybrid reranking and compression behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply hybrid reranking and compression in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Fuse lexical and dense candidates, then apply a cross-encoder or other reranker to a bounded set. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Fuse lexical and dense candidates, then apply a cross-encoder or other reranker to a bounded set. Contextual compression extracts relevant portions, but must preserve provenance and avoid changing meaning. Relevance filtering removes weak evidence; thresholds need calibration. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Fuse lexical and dense candidates, then apply a cross-encoder or other reranker to a bounded set. Contextual compression extracts relevant portions, but must preserve provenance and avoid changing meaning. Relevance filtering removes weak evidence; thresholds need calibration.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating hybrid reranking and compression as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 34: After a release, reranking and relevance behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply reranking and relevance in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Rerank a candidate set larger than the final context. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Rerank a candidate set larger than the final context. Cross-encoders score query-document pairs jointly and can improve ranking. They cannot recover an absent relevant document. Calibrate acceptance thresholds for the actual domain and evaluate false abstentions. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Rerank a candidate set larger than the final context. Cross-encoders score query-document pairs jointly and can improve ranking. They cannot recover an absent relevant document. Calibrate acceptance thresholds for the actual domain and evaluate false abstentions.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating reranking and relevance as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 35: After a release, prompt and answer behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply prompt and answer in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Pack evidence within a token budget, use explicit source IDs, and define an abstention policy. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Pack evidence within a token budget, use explicit source IDs, and define an abstention policy. Separate retrieved content from trusted instructions. Ask for claims supported by evidence and validate the output shape. The application retains responsibility for authorization. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Pack evidence within a token budget, use explicit source IDs, and define an abstention policy. Separate retrieved content from trusted instructions. Ask for claims supported by evidence and validate the output shape. The application retains responsibility for authorization.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating prompt and answer as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 36: After a release, freshness and lifecycle behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply freshness and lifecycle in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Use change tracking, source checksums, tombstones, and index version aliases. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Use change tracking, source checksums, tombstones, and index version aliases. Delete or replace all chunks belonging to an outdated version. Permissions may change more often than content; recheck authorization against the source of truth. Define acceptable ingestion lag. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Use change tracking, source checksums, tombstones, and index version aliases. Delete or replace all chunks belonging to an outdated version. Permissions may change more often than content; recheck authorization against the source of truth. Define acceptable ingestion lag.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating freshness and lifecycle as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 37: After a release, citations behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply citations in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Tie each citation to immutable document version and source span. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Tie each citation to immutable document version and source span. Validate that the ID exists in the supplied evidence and assess whether the span supports the claim. A correct URL attached to an unsupported answer is still a bad citation. Do not fabricate page numbers. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Tie each citation to immutable document version and source span. Validate that the ID exists in the supplied evidence and assess whether the span supports the claim. A correct URL attached to an unsupported answer is still a bad citation. Do not fabricate page numbers.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating citations as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 38: After a release, evaluation experiments behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply evaluation experiments in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Separate retrieval, context selection, generation, and citation experiments. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Separate retrieval, context selection, generation, and citation experiments. Use paired comparisons on the same queries and slice by language, PDF type, and question complexity. Prevent prompt tuning on the final test set. Record confidence and inspect failures, not only aggregate averages. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Separate retrieval, context selection, generation, and citation experiments. Use paired comparisons on the same queries and slice by language, PDF type, and question complexity. Prevent prompt tuning on the final test set. Record confidence and inspect failures, not only aggregate averages.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating evaluation experiments as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 39: After a release, testing and hallucination reduction behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply testing and hallucination reduction in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Measure parsing coverage, chunk coverage, Recall@k, ranking, answer correctness, faithfulness, abstention, and citation quality separately. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Measure parsing coverage, chunk coverage, Recall@k, ranking, answer correctness, faithfulness, abstention, and citation quality separately. Add missing-answer, contradictory-source, outdated-source, and injection tests. Better retrieval cannot fix every generation failure, and better generation cannot invent missing evidence. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Measure parsing coverage, chunk coverage, Recall@k, ranking, answer correctness, faithfulness, abstention, and citation quality separately. Add missing-answer, contradictory-source, outdated-source, and injection tests. Better retrieval cannot fix every generation failure, and better generation cannot invent missing evidence.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating testing and hallucination reduction as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 40: After a release, scaling and failure behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply scaling and failure in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Bound query fanout and context length. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Bound query fanout and context length. Cache only permission-scoped, versioned results. Maintain partial-service behavior if reranking fails, but label the degraded path and validate quality. Load-test mixed ingestion and queries and test restore from snapshots. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Bound query fanout and context length. Cache only permission-scoped, versioned results. Maintain partial-service behavior if reranking fails, but label the degraded path and validate quality. Load-test mixed ingestion and queries and test restore from snapshots.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating scaling and failure as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 41: How would you demonstrate that a change involving document loading actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply document loading in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Scanned PDFs need OCR; text extraction alone can return empty pages. Preserve table headers and units. Treat uploaded files as untrusted data with size and parsing limits. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Scanned PDFs need OCR; text extraction alone can return empty pages. Preserve table headers and units. Treat uploaded files as untrusted data with size and parsing limits.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating document loading as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 42: How would you demonstrate that a change involving 500000-document design actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply 500000-document design in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Estimate average chunks per document before sizing. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Estimate average chunks per document before sizing. Store originals in object storage, metadata and permissions in a relational store, and derived vectors in a versioned search index. Use queues for extraction and embedding, idempotent workers, an activation record for versions, and dead-letter handling for failed sources. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Estimate average chunks per document before sizing. Store originals in object storage, metadata and permissions in a relational store, and derived vectors in a versioned search index. Use queues for extraction and embedding, idempotent workers, an activation record for versions, and dead-letter handling for failed sources.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating 500000-document design as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 43: How would you demonstrate that a change involving recursive chunking actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply recursive chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Overlap carries boundary context but increases storage and duplicate retrieval. Token-aware limits are preferable when model budgets are tight. Evaluate several sizes rather than declaring 1000/200 universally best. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Overlap carries boundary context but increases storage and duplicate retrieval. Token-aware limits are preferable when model budgets are tight. Evaluate several sizes rather than declaring 1000/200 universally best.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating recursive chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 44: How would you demonstrate that a change involving irrelevant results actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply irrelevant results in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Compare exact search on a small labeled sample. Fix missing extraction or incorrect ACLs before tuning scores. Separate weak candidate retrieval from weak reranking. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Compare exact search on a small labeled sample. Fix missing extraction or incorrect ACLs before tuning scores. Separate weak candidate retrieval from weak reranking.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating irrelevant results as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 45: How would you demonstrate that a change involving semantic chunking actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply semantic chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Use boundaries based on content transitions, often from embedding changes. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Use boundaries based on content transitions, often from embedding changes. This can preserve coherent meaning but costs preprocessing and introduces thresholds. A semantic boundary is not necessarily the right factual citation boundary. Compare against simpler structure-aware splitting. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Use boundaries based on content transitions, often from embedding changes. This can preserve coherent meaning but costs preprocessing and introduces thresholds. A semantic boundary is not necessarily the right factual citation boundary. Compare against simpler structure-aware splitting.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating semantic chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 46: How would you demonstrate that a change involving correct answer wrong citation actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply correct answer wrong citation in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Track whether citations refer to parent IDs, child IDs, or source spans. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Track whether citations refer to parent IDs, child IDs, or source spans. A common bug is positional numbering after reranking while generation uses older numbering. Another is cached answer text paired with fresh citations. Bind answer and evidence version as one immutable result. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Track whether citations refer to parent IDs, child IDs, or source spans. A common bug is positional numbering after reranking while generation uses older numbering. Another is cached answer text paired with fresh citations. Bind answer and evidence version as one immutable result.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating correct answer wrong citation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 47: How would you demonstrate that a change involving parent-child chunking actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply parent-child chunking in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Index small children for precise retrieval and supply their larger parent sections for context. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Index small children for precise retrieval and supply their larger parent sections for context. Keep both IDs and avoid returning an entire oversized parent. Enforce permissions on parent and child together. Deduplicate parents when multiple children match. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Index small children for precise retrieval and supply their larger parent sections for context. Keep both IDs and avoid returning an entire oversized parent. Enforce permissions on parent and child together. Deduplicate parents when multiple children match.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating parent-child chunking as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 48: How would you demonstrate that a change involving correct context wrong answer actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply correct context wrong answer in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Decompose multi-hop questions and use tools for arithmetic. Relevance does not imply completeness. Abstain when all required evidence is not present. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Decompose multi-hop questions and use tools for arithmetic. Relevance does not imply completeness. Abstain when all required evidence is not present.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating correct context wrong answer as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

## Question 49: How would you demonstrate that a change involving metadata and ingestion actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply metadata and ingestion in a real retrieval-augmented generation system and explain the relevant failure boundary.

### Short Answer

Assign stable IDs with document version, chunk offset, language, title, and access attributes. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Assign stable IDs with document version, chunk offset, language, title, and access attributes. Persist the original source separately from derived text and vectors. Re-ingestion should atomically activate a complete new version rather than expose half an update. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Retrieval returns relevant context, but the answer still hallucinates. How do you debug it?

### Deep Technical Answer

A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k. For this question, the specific mechanism is: Assign stable IDs with document version, chunk offset, language, title, and access attributes. Persist the original source separately from derived text and vectors. Re-ingestion should atomically activate a complete new version rather than expose half an update.

### Real-World Example

Retrieval returns relevant context, but the answer still hallucinates. How do you debug it? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [rag.py](../examples/rag.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating metadata and ingestion as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

## Question 50: How would you demonstrate that a change involving variable answers actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply variable answers in a real advanced rag and scale system and explain the relevant failure boundary.

### Short Answer

Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Lower temperature reduces one source of variation. Version configurations and use canonical evidence ordering, but do not promise universal determinism. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: Design a RAG system for 500,000 documents with frequent policy changes.

### Deep Technical Answer

If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable. For this question, the specific mechanism is: Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Lower temperature reduces one source of variation. Version configurations and use canonical evidence ordering, but do not promise universal determinism.

### Real-World Example

Design a RAG system for 500,000 documents with frequent policy changes. Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [hybrid.py](../examples/hybrid.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating variable answers as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.
