# Debugging runbooks

## RAG irrelevant

**Symptoms:** Top hits discuss the topic but omit the requested fact.

**Investigation:** Inspect parsing, chunks, query rewrite, permissions, and exact-search baseline.

**Root cause in this example:** The embedding input was truncated before the relevant section.

**Fix:** Use shorter structure-aware chunks and re-embed a new version.

**Prevention:** Measure source coverage and Recall@k on long documents.

## Embedding dimensions

**Symptoms:** Writes fail only after an embedding model change.

**Investigation:** Compare index dimension and model revision for every batch.

**Root cause in this example:** Old and new model spaces were mixed.

**Fix:** Build a new versioned index and switch only after evaluation.

**Prevention:** Reject revision mismatch in the ingestion contract.

## Vector latency

**Symptoms:** p95 retrieval grows during ingestion.

**Investigation:** Inspect ANN settings, payload indexes, CPU, memory, and selective-filter queries.

**Root cause in this example:** Unindexed payload filters scan too many candidates.

**Fix:** Create appropriate metadata indexes and benchmark representative queries.

**Prevention:** Load-test read/write mixtures and track p95 by filter type.

## Hallucination

**Symptoms:** Answer cites a relevant source but invents a number.

**Investigation:** Inspect source support, packed context, truncation, history, and units.

**Root cause in this example:** The source lacks the number, but the prompt did not abstain.

**Fix:** Add sufficiency checks and supported-claim behavior.

**Prevention:** Add unanswerable cases and semantic citation review.

## Citation mismatch

**Symptoms:** Correct claim points to the wrong chunk.

**Investigation:** Compare IDs before and after reranking and answer caching.

**Root cause in this example:** Position-based citation numbering changed after candidate reordering.

**Fix:** Use stable source-version-span IDs.

**Prevention:** Test reordered contexts and cached answer/evidence consistency.

## Token spike

**Symptoms:** Spend increases without more requests.

**Investigation:** Compare input/output tokens, prompt hash, retries, history, and tool traces.

**Root cause in this example:** Conversation history stopped being trimmed.

**Fix:** Restore token budgets with safe summary and message-pair handling.

**Prevention:** Alert on tokens per successful task and history length.

## API latency

**Symptoms:** Provider time is stable but total p95 increases.

**Investigation:** Separate queue, parsing, database, retrieval, and model spans.

**Root cause in this example:** Synchronous parsing blocks the event loop.

**Fix:** Move parsing to bounded workers or async-safe execution.

**Prevention:** Test mixed requests under load and observe event-loop lag.

## Agent loop

**Symptoms:** Same tool and arguments recur without progress.

**Investigation:** Inspect routing state and tool fingerprints.

**Root cause in this example:** Error observations never trigger a stop or alternate route.

**Fix:** Add no-progress handling and step/time/cost budgets.

**Prevention:** Regression-test repeated failure observations.

## Invalid arguments

**Symptoms:** Tools receive invented employee IDs or extra fields.

**Investigation:** Inspect offered schema and raw completed arguments.

**Root cause in this example:** Schema is loose and business validation is missing.

**Fix:** Validate strict fields and look up authorized IDs.

**Prevention:** Contract-test every tool with malformed and forbidden inputs.

## Dangerous SQL

**Symptoms:** A proposal includes writes or a costly query.

**Investigation:** Inspect the parsed plan and database role before any execution.

**Root cause in this example:** Generated SQL was sent to a privileged connection.

**Fix:** Use constrained plans and a read-only scoped role with timeout.

**Prevention:** Adversarial SQL tests and operation audit.

## Prompt injection

**Symptoms:** A webpage tells the agent to exfiltrate data.

**Investigation:** Inspect source trust, offered capabilities, and egress policy.

**Root cause in this example:** Untrusted content influenced a broadly privileged tool.

**Fix:** Restrict permissions and treat source instructions as data.

**Prevention:** End-to-end indirect injection tests with denied actions.

## Wrong memory

**Symptoms:** A corrected preference is replaced by an older summary.

**Investigation:** Inspect timestamps, provenance, update paths, and retrieved scope.

**Root cause in this example:** Append-only memories return conflicting entries.

**Fix:** Implement explicit supersession and correction.

**Prevention:** Test updates, expiry, deletion, and cross-tenant reads.

## Provider outage

**Symptoms:** Most model requests time out or rate-limit.

**Investigation:** Inspect error categories, quotas, request volume, and circuit state.

**Root cause in this example:** Nested retries amplify provider saturation.

**Fix:** Bound total retries and use admission control or validated fallback.

**Prevention:** Failure injection and retry amplification metrics.

## Stream interruption

**Symptoms:** Client sees partial text and no completion.

**Investigation:** Inspect proxy buffering, idle deadlines, exceptions, and disconnects.

**Root cause in this example:** Generator fails midstream and the server records success too early.

**Fix:** Use safe error/final events and cancellation-aware cleanup.

**Prevention:** Test disconnects and midstream dependency failures.

## Stale policy

**Symptoms:** Deleted rules continue to appear in answers.

**Investigation:** Inspect active source version, tombstones, caches, and old chunks.

**Root cause in this example:** A shorter replacement left orphaned chunks.

**Fix:** Replace all source chunks and invalidate scoped caches.

**Prevention:** Version lifecycle and deletion tests.
