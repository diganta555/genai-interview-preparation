# Round 1 answer key

Open only after answering each question.

## 1. You are about to deploy supervised learning. What design and acceptance checks do you require?

**Expected answer:** Learn from labeled input-output pairs. Classification predicts categories such as support intent; regression predicts a continuous value such as estimated request cost. A useful baseline is a simple model or rule with a measurable business outcome. More model complexity is justified only by held-out improvement. Not necessarily. With rare attacks, predicting benign for every input can produce high accuracy. Examine attack recall, false-positive rate, precision-recall curves, and costs on realistic slices.

**Deep follow-up:** Build a confusion matrix from independently labeled traffic. If attacks are 1%, a constant benign predictor already reaches 99% accuracy with zero attack recall. Tune thresholds using validation data and report uncertainty with sufficient positive examples. Combine detection with permission boundaries so one missed classification cannot grant access. Monitor drift because attackers adapt to the detector.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Supervised learning; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy neural networks. What design and acceptance checks do you require?

**Expected answer:** A layer computes a weighted transformation followed by a nonlinearity. Multiple layers learn progressively different representations. Width and depth increase capacity but also memory, compute, and overfitting risk. Parameters are learned weights; activations are intermediate values for one input. They allow efficient parallel training across sequence positions and make long-distance interactions easier through attention. Their compute pattern scales well on accelerators, although generation remains autoregressive.

**Deep follow-up:** An RNN’s hidden state depends on the previous position; transformer attention computes interactions from all position representations together during teacher-forced training. Position information preserves order. Scaling data, parameters, and accelerator utilization made transformers effective. This does not mean unlimited context is cheap: KV cache and attention cost still grow with context length. Distinguish architectural advantages from the benefits of larger datasets and training budgets.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Neural networks; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy tokenization. What design and acceptance checks do you require?

**Expected answer:** Tokenizers map text to token IDs using learned subword vocabularies or related methods. A token is not always a word; different languages have different token counts. Tokenizer and model vocabulary must match. Chunk limits measured in characters are not model token limits. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Tokenization; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy vector representation. What design and acceptance checks do you require?

**Expected answer:** A dense embedding has one numeric value per dimension. These dimensions are learned and usually have no simple human label. Different models produce different spaces. Never compare vectors from incompatible embedding models even when their dimensions match. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Vector representation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy unsupervised learning and clustering. What design and acceptance checks do you require?

**Expected answer:** Discover structure without target labels. Cluster support tickets to discover themes, but cluster IDs are not objective business meanings. Density and distance depend on representation and scaling. Human review is needed before assigning names or policies to clusters. Not necessarily. With rare attacks, predicting benign for every input can produce high accuracy. Examine attack recall, false-positive rate, precision-recall curves, and costs on realistic slices.

**Deep follow-up:** Build a confusion matrix from independently labeled traffic. If attacks are 1%, a constant benign predictor already reaches 99% accuracy with zero attack recall. Tune thresholds using validation data and report uncertainty with sufficient positive examples. Combine detection with permission boundaries so one missed classification cannot grant access. Monitor drift because attackers adapt to the detector.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Unsupervised learning and clustering; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy backpropagation. What design and acceptance checks do you require?

**Expected answer:** The chain rule propagates loss gradients through the network. An optimizer uses those gradients to change parameters. Backpropagation computes derivatives; it is not itself the update rule. Inference usually does not retain gradients, reducing memory compared with training. They allow efficient parallel training across sequence positions and make long-distance interactions easier through attention. Their compute pattern scales well on accelerators, although generation remains autoregressive.

**Deep follow-up:** An RNN’s hidden state depends on the previous position; transformer attention computes interactions from all position representations together during teacher-forced training. Position information preserves order. Scaling data, parameters, and accelerator utilization made transformers effective. This does not mean unlimited context is cheap: KV cache and attention cost still grow with context length. Distinguish architectural advantages from the benefits of larger datasets and training budgets.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Backpropagation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy token embeddings and positions. What design and acceptance checks do you require?

**Expected answer:** Each token ID indexes a learned embedding. Position information distinguishes order, using learned positions, sinusoidal encodings, rotary methods, or other designs. Rotary position embeddings transform query and key representations according to position. Different architectures do not all use the original sinusoidal scheme. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Token embeddings and positions; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy cosine similarity. What design and acceptance checks do you require?

**Expected answer:** Cosine is dot(a,b)/(norm(a) norm(b)). It compares direction and ranges from -1 to 1 for nonzero real vectors. Reject zero vectors or define an explicit policy. A threshold such as 0.8 is not universally meaningful across models and corpora. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Cosine similarity; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy feature engineering. What design and acceptance checks do you require?

**Expected answer:** Construct informative inputs such as query length, language, domain, retrieved score gap, or recent error rate. Prevent features from using information unavailable at prediction time. Standardize scale-sensitive features using training-set statistics only. Keep transformation logic identical during training and serving. Not necessarily. With rare attacks, predicting benign for every input can produce high accuracy. Examine attack recall, false-positive rate, precision-recall curves, and costs on realistic slices.

**Deep follow-up:** Build a confusion matrix from independently labeled traffic. If attacks are 1%, a constant benign predictor already reaches 99% accuracy with zero attack recall. Tune thresholds using validation data and report uncertainty with sufficient positive examples. Combine detection with permission boundaries so one missed classification cannot grant access. Monitor drift because attackers adapt to the detector.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Feature engineering; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy activation functions. What design and acceptance checks do you require?

**Expected answer:** ReLU, GELU, sigmoid, and tanh introduce nonlinearity. Sigmoid is useful for probabilities but saturates at extremes. ReLU is simple but can produce inactive units. Transformer feed-forward blocks often use GELU or gated variants; activation choice affects optimization and compute. They allow efficient parallel training across sequence positions and make long-distance interactions easier through attention. Their compute pattern scales well on accelerators, although generation remains autoregressive.

**Deep follow-up:** An RNN’s hidden state depends on the previous position; transformer attention computes interactions from all position representations together during teacher-forced training. Position information preserves order. Scaling data, parameters, and accelerator utilization made transformers effective. This does not mean unlimited context is cheap: KV cache and attention cost still grow with context length. Distinguish architectural advantages from the benefits of larger datasets and training budgets.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Activation functions; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy query key value. What design and acceptance checks do you require?

**Expected answer:** Project each representation into Q, K, and V. Query-key compatibility determines attention weights; those weights combine values. A useful analogy is a search request, an index label, and returned content, but the actual computation is learned matrix multiplication, not an external database lookup. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Query key value; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. You are about to deploy euclidean distance. What design and acceptance checks do you require?

**Expected answer:** Euclidean distance is the length of the difference vector. Smaller is closer. For unit-normalized vectors, squared Euclidean distance equals 2 minus twice cosine similarity, so ranking agrees. Without normalization, vector magnitude changes results. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Euclidean distance; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. You are about to deploy overfitting and underfitting. What design and acceptance checks do you require?

**Expected answer:** Overfitting memorizes training specifics; underfitting misses useful structure. Compare training and validation errors. Regularization, simpler models, better data, and early stopping address different causes. A prompt can also overfit when repeatedly tuned on the same small evaluation set. Not necessarily. With rare attacks, predicting benign for every input can produce high accuracy. Examine attack recall, false-positive rate, precision-recall curves, and costs on realistic slices.

**Deep follow-up:** Build a confusion matrix from independently labeled traffic. If attacks are 1%, a constant benign predictor already reaches 99% accuracy with zero attack recall. Tune thresholds using validation data and report uncertainty with sufficient positive examples. Combine detection with permission boundaries so one missed classification cannot grant access. Monitor drift because attackers adapt to the detector.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Overfitting and underfitting; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. You are about to deploy loss functions. What design and acceptance checks do you require?

**Expected answer:** Cross-entropy compares predicted token probabilities with the target token. Mean squared error is common for regression. Contrastive losses pull relevant embedding pairs together and separate negatives. Minimizing token loss does not directly guarantee truthful, safe, or helpful answers. They allow efficient parallel training across sequence positions and make long-distance interactions easier through attention. Their compute pattern scales well on accelerators, although generation remains autoregressive.

**Deep follow-up:** An RNN’s hidden state depends on the previous position; transformer attention computes interactions from all position representations together during teacher-forced training. Position information preserves order. Scaling data, parameters, and accelerator utilization made transformers effective. This does not mean unlimited context is cheap: KV cache and attention cost still grow with context length. Distinguish architectural advantages from the benefits of larger datasets and training budgets.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Loss functions; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. You are about to deploy scaled dot-product attention. What design and acceptance checks do you require?

**Expected answer:** Attention(Q,K,V) = softmax(QKᵀ/√d_k + mask)V. Scaling controls logit magnitude as dimension grows. Masked positions receive effectively negative infinity before softmax. Normalize over the key positions for each query. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Scaled dot-product attention; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. You are about to deploy normalization. What design and acceptance checks do you require?

**Expected answer:** Divide a vector by its norm to make its length one. This permits dot product to act as cosine similarity. Apply the same normalization consistently to documents and queries when the index expects it. Do not blindly normalize a model designed for a different scoring convention. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Normalization; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. You are about to deploy train validation test. What design and acceptance checks do you require?

**Expected answer:** Train fits parameters, validation chooses configurations, and test estimates final generalization. Split by user, document family, or time when records are correlated. Randomly splitting near-duplicate chunks from the same PDF leaks information. Freeze the test set before tuning prompts or retrieval settings. Not necessarily. With rare attacks, predicting benign for every input can produce high accuracy. Examine attack recall, false-positive rate, precision-recall curves, and costs on realistic slices.

**Deep follow-up:** Build a confusion matrix from independently labeled traffic. If attacks are 1%, a constant benign predictor already reaches 99% accuracy with zero attack recall. Tune thresholds using validation data and report uncertainty with sufficient positive examples. Combine detection with permission boundaries so one missed classification cannot grant access. Monitor drift because attackers adapt to the detector.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Train validation test; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. You are about to deploy optimization. What design and acceptance checks do you require?

**Expected answer:** SGD and Adam-like optimizers adjust weights. Learning rate controls update scale; too high can destabilize training, too low can waste time. Batch size, warmup, clipping, and schedules matter. Record optimizer configuration and random seeds to investigate regressions. They allow efficient parallel training across sequence positions and make long-distance interactions easier through attention. Their compute pattern scales well on accelerators, although generation remains autoregressive.

**Deep follow-up:** An RNN’s hidden state depends on the previous position; transformer attention computes interactions from all position representations together during teacher-forced training. Position information preserves order. Scaling data, parameters, and accelerator utilization made transformers effective. This does not mean unlimited context is cheap: KV cache and attention cost still grow with context length. Distinguish architectural advantages from the benefits of larger datasets and training budgets.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Optimization; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. You are about to deploy multi-head attention. What design and acceptance checks do you require?

**Expected answer:** Different heads use different learned projections and can represent different relations. Concatenate head outputs and apply an output projection. More heads are not automatically better. Grouped-query and multi-query variants share key/value projections to reduce inference cache cost. It tokenizes the prefix, combines token and position representations through masked attention blocks, predicts probabilities for the next token, selects one token, appends it, and repeats.

**Deep follow-up:** Technically, the last-position hidden state is projected to vocabulary logits, then normalized and selected with an allowed decoding policy. Expert-level discussion separates prefill from decode, explains KV cache reuse, causal masks, attention variants, and the effect of batching on cache memory. Greedy decoding reduces sampling variability but does not promise bit-for-bit determinism across all hardware and provider changes. EOS or an output limit ends generation.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Multi-head attention; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. You are about to deploy dimensions and storage. What design and acceptance checks do you require?

**Expected answer:** Raw float32 storage is N × d × 4 bytes, excluding IDs, metadata, replicas, and index overhead. One million 768-dimensional vectors use about 3.072 GB decimal for values alone. Higher dimension can increase capacity and cost but does not guarantee relevance. Inspect query and document encoding, domain and language mismatch, truncation, index distance, normalization, and difficult cases such as negation. Evaluate lexical hybrid search and reranking on a labeled dataset.

**Deep follow-up:** First use exact search on a small sample to separate embedding failures from approximate-index failures. Compare top results for paraphrases, identifiers, negatives, and language slices. Confirm query instructions match the model and that old embeddings are not mixed with a new model. An approximate index can lose recall even if embeddings are good; a cross-encoder can reorder a candidate set but cannot recover relevant documents absent from that set.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Dimensions and storage; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
