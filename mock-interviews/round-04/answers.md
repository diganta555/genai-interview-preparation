# Round 4 answer key

Open only after answering each question.

## 1. You are about to deploy vector representation. What design and acceptance checks do you require?

**Expected answer:** A dense embedding has one numeric value per dimension. These dimensions are learned and usually have no simple human label. Different models produce different spaces. Never compare vectors from incompatible embedding models even when their dimensions match. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Vector representation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy faiss. What design and acceptance checks do you require?

**Expected answer:** FAISS provides local similarity-search algorithms, including exact and approximate indexes. It is useful for experiments and embedded services. The library does not by itself give a distributed database with tenant authorization, backups, or transactional metadata. Pair it with explicit ID mapping and source metadata. Measure vectors rather than document count, add persistent metadata and permissions, and choose an index or database that meets latency, update, availability, and backup requirements. A managed service is one option, not an automatic requirement.

**Deep follow-up:** Five million documents with ten chunks each yield fifty million vectors. Raw vector memory alone may exceed one node; replicas and ANN overhead add more. Partition according to query and isolation patterns, benchmark exact versus approximate recall, and build asynchronous versioned ingestion. Define recovery point and recovery time objectives. If FAISS remains appropriate, you still need a serving layer, routing, metadata consistency, snapshots, and recovery procedures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for FAISS; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy document loading. What design and acceptance checks do you require?

**Expected answer:** Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. Scanned PDFs need OCR; text extraction alone can return empty pages. Preserve table headers and units. Treat uploaded files as untrusted data with size and parsing limits. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

**Deep follow-up:** A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Document loading; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy 500000-document design. What design and acceptance checks do you require?

**Expected answer:** Estimate average chunks per document before sizing. Store originals in object storage, metadata and permissions in a relational store, and derived vectors in a versioned search index. Use queues for extraction and embedding, idempotent workers, an activation record for versions, and dead-letter handling for failed sources. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

**Deep follow-up:** If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for 500000-document design; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy cosine similarity. What design and acceptance checks do you require?

**Expected answer:** Cosine is dot(a,b)/(norm(a) norm(b)). It compares direction and ranges from -1 to 1 for nonzero real vectors. Reject zero vectors or define an explicit policy. A threshold such as 0.8 is not universally meaningful across models and corpora. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Cosine similarity; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy chroma. What design and acceptance checks do you require?

**Expected answer:** Chroma supports collections, persistence, retrieval, and metadata operations. It is convenient for local RAG labs and supports additional deployment modes. Configure embeddings explicitly so an example does not unexpectedly download a model. Update text together with vectors; upsert and update have different missing-ID behavior. Measure vectors rather than document count, add persistent metadata and permissions, and choose an index or database that meets latency, update, availability, and backup requirements. A managed service is one option, not an automatic requirement.

**Deep follow-up:** Five million documents with ten chunks each yield fifty million vectors. Raw vector memory alone may exceed one node; replicas and ANN overhead add more. Partition according to query and isolation patterns, benchmark exact versus approximate recall, and build asynchronous versioned ingestion. Define recovery point and recovery time objectives. If FAISS remains appropriate, you still need a serving layer, routing, metadata consistency, snapshots, and recovery procedures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Chroma; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy recursive chunking. What design and acceptance checks do you require?

**Expected answer:** Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. Overlap carries boundary context but increases storage and duplicate retrieval. Token-aware limits are preferable when model budgets are tight. Evaluate several sizes rather than declaring 1000/200 universally best. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

**Deep follow-up:** A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Recursive chunking; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy irrelevant results. What design and acceptance checks do you require?

**Expected answer:** Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. Compare exact search on a small labeled sample. Fix missing extraction or incorrect ACLs before tuning scores. Separate weak candidate retrieval from weak reranking. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

**Deep follow-up:** If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Irrelevant results; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy euclidean distance. What design and acceptance checks do you require?

**Expected answer:** Euclidean distance is the length of the difference vector. Smaller is closer. For unit-normalized vectors, squared Euclidean distance equals 2 minus twice cosine similarity, so ranking agrees. Without normalization, vector magnitude changes results. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Euclidean distance; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy pinecone. What design and acceptance checks do you require?

**Expected answer:** Pinecone offers managed vector infrastructure. Evaluate metadata filters, namespace strategy, ingest rate, residency, and billing for your workload. A namespace helps organize data but does not replace application authorization. Service limits and prices must be checked at design time. Measure vectors rather than document count, add persistent metadata and permissions, and choose an index or database that meets latency, update, availability, and backup requirements. A managed service is one option, not an automatic requirement.

**Deep follow-up:** Five million documents with ten chunks each yield fifty million vectors. Raw vector memory alone may exceed one node; replicas and ANN overhead add more. Partition according to query and isolation patterns, benchmark exact versus approximate recall, and build asynchronous versioned ingestion. Define recovery point and recovery time objectives. If FAISS remains appropriate, you still need a serving layer, routing, metadata consistency, snapshots, and recovery procedures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Pinecone; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy semantic chunking. What design and acceptance checks do you require?

**Expected answer:** Use boundaries based on content transitions, often from embedding changes. This can preserve coherent meaning but costs preprocessing and introduces thresholds. A semantic boundary is not necessarily the right factual citation boundary. Compare against simpler structure-aware splitting. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

**Deep follow-up:** A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Semantic chunking; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. You are about to deploy correct answer wrong citation. What design and acceptance checks do you require?

**Expected answer:** Track whether citations refer to parent IDs, child IDs, or source spans. A common bug is positional numbering after reranking while generation uses older numbering. Another is cached answer text paired with fresh citations. Bind answer and evidence version as one immutable result. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

**Deep follow-up:** If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Correct answer wrong citation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. You are about to deploy normalization. What design and acceptance checks do you require?

**Expected answer:** Divide a vector by its norm to make its length one. This permits dot product to act as cosine similarity. Apply the same normalization consistently to documents and queries when the index expects it. Do not blindly normalize a model designed for a different scoring convention. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Normalization; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. You are about to deploy qdrant. What design and acceptance checks do you require?

**Expected answer:** Qdrant exposes vector search with payload filtering and collection management. It can run locally or in managed infrastructure. Payload indexes matter for selective filters. Measure performance under the actual filter distribution, vector count, and concurrency, including updates. Measure vectors rather than document count, add persistent metadata and permissions, and choose an index or database that meets latency, update, availability, and backup requirements. A managed service is one option, not an automatic requirement.

**Deep follow-up:** Five million documents with ten chunks each yield fifty million vectors. Raw vector memory alone may exceed one node; replicas and ANN overhead add more. Partition according to query and isolation patterns, benchmark exact versus approximate recall, and build asynchronous versioned ingestion. Define recovery point and recovery time objectives. If FAISS remains appropriate, you still need a serving layer, routing, metadata consistency, snapshots, and recovery procedures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Qdrant; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. You are about to deploy parent-child chunking. What design and acceptance checks do you require?

**Expected answer:** Index small children for precise retrieval and supply their larger parent sections for context. Keep both IDs and avoid returning an entire oversized parent. Enforce permissions on parent and child together. Deduplicate parents when multiple children match. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

**Deep follow-up:** A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Parent-child chunking; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. You are about to deploy correct context wrong answer. What design and acceptance checks do you require?

**Expected answer:** Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. Decompose multi-hop questions and use tools for arithmetic. Relevance does not imply completeness. Abstain when all required evidence is not present. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

**Deep follow-up:** If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Correct context wrong answer; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. You are about to deploy dimensions and storage. What design and acceptance checks do you require?

**Expected answer:** Raw float32 storage is N × d × 4 bytes, excluding IDs, metadata, replicas, and index overhead. One million 768-dimensional vectors use about 3.072 GB decimal for values alone. Higher dimension can increase capacity and cost but does not guarantee relevance. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Dimensions and storage; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. You are about to deploy weaviate. What design and acceptance checks do you require?

**Expected answer:** Weaviate combines object data and search capabilities, with configurations for vectorization and hybrid retrieval. Understand whether embeddings are generated by the service or application. Evaluate schema, tenant isolation, backups, and operational ownership against your requirements. Measure vectors rather than document count, add persistent metadata and permissions, and choose an index or database that meets latency, update, availability, and backup requirements. A managed service is one option, not an automatic requirement.

**Deep follow-up:** Five million documents with ten chunks each yield fifty million vectors. Raw vector memory alone may exceed one node; replicas and ANN overhead add more. Partition according to query and isolation patterns, benchmark exact versus approximate recall, and build asynchronous versioned ingestion. Define recovery point and recovery time objectives. If FAISS remains appropriate, you still need a serving layer, routing, metadata consistency, snapshots, and recovery procedures.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Weaviate; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. You are about to deploy metadata and ingestion. What design and acceptance checks do you require?

**Expected answer:** Assign stable IDs with document version, chunk offset, language, title, and access attributes. Persist the original source separately from derived text and vectors. Re-ingestion should atomically activate a complete new version rather than expose half an update. Inspect the exact prompt sent to the model, truncation, conflicting instructions, source versions, and the unsupported claim. Separate retrieval relevance from evidence sufficiency, then test grounding and abstention with a fixed benchmark.

**Deep follow-up:** A relevant document may not contain the requested fact. Verify the retrieved span actually supports the answer, then check whether packing dropped that span or placed it among conflicting content. Inspect chat history and retrieved instructions for contamination. Require source-linked claims and independent citation checks. If correct context is ignored, compare a minimal prompt, smaller evidence set, and a model change. Keep latency and quality budgets visible rather than endlessly increasing top-k.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Metadata and ingestion; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. You are about to deploy variable answers. What design and acceptance checks do you require?

**Expected answer:** Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. Lower temperature reduces one source of variation. Version configurations and use canonical evidence ordering, but do not promise universal determinism. Use asynchronous versioned ingestion, object storage, metadata and ACL records, filtered retrieval, bounded reranking, a provider gateway, and independent retrieval and answer evaluations. Treat freshness and permission updates as first-class requirements.

**Deep follow-up:** If each document produces twenty chunks, plan for ten million vectors. Build parsing and embedding stages with deduplication and per-source version checks. Activate a source version only after complete ingestion. Track ingestion lag, permission freshness, index recall, query p95, and citation support. During model or embedding migration, build a shadow index and compare on fixed queries before alias switching. Restrict fanout to keep provider quotas and costs predictable.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Variable answers; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
