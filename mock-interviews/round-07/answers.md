# Round 7 answer key

Open only after answering each question.

## 1. You are about to deploy correctness and relevance. What design and acceptance checks do you require?

**Expected answer:** Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Correctness and relevance; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 2. You are about to deploy structured logging. What design and acceptance checks do you require?

**Expected answer:** Log JSON events with request ID, stage, safe error code, duration, and version identifiers. Avoid full prompts and responses by default. Centralize redaction and control access. Sample detailed payloads only under a justified retention policy. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Structured logging; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 3. You are about to deploy faithfulness groundedness hallucination. What design and acceptance checks do you require?

**Expected answer:** Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Faithfulness groundedness hallucination; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 4. You are about to deploy tracing. What design and acceptance checks do you require?

**Expected answer:** A trace groups spans for API, retrieval, reranking, model, tools, and database calls. Propagate trace context across queues and service boundaries. Distinguish queue time from execution. Trace correlation reveals whether model latency or your own code dominates p95. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Tracing; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 5. You are about to deploy retrieval evaluation. What design and acceptance checks do you require?

**Expected answer:** Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Retrieval evaluation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 6. You are about to deploy tokens and cost. What design and acceptance checks do you require?

**Expected answer:** Record provider-reported token usage and model configuration. Attribute cost by tenant, task, and stage without leaking sensitive payloads. Include retries, cache behavior, and failures. A successful-response-only dashboard underestimates actual spend. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Tokens and cost; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 7. You are about to deploy code-based evaluation. What design and acceptance checks do you require?

**Expected answer:** Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Code-based evaluation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 8. You are about to deploy latency and errors. What design and acceptance checks do you require?

**Expected answer:** Track percentiles and error categories, not only average latency. An increasing p99 can reveal saturation before mean latency changes. Separate validation failures, forbidden calls, rate limits, network failures, and model timeouts. Use alerts tied to user impact. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Latency and errors; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 9. You are about to deploy llm-as-a-judge. What design and acceptance checks do you require?

**Expected answer:** A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for LLM-as-a-judge; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 10. You are about to deploy tool traces. What design and acceptance checks do you require?

**Expected answer:** Record allowed tool name, call ID, outcome, duration, and safe argument summary. Consequential actions need separate audit records. A trace helps debugging but is not a substitute for a durable business ledger. Test correlation under retries. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Tool traces; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 11. You are about to deploy human evaluation. What design and acceptance checks do you require?

**Expected answer:** Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Human evaluation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 12. You are about to deploy retrieval traces. What design and acceptance checks do you require?

**Expected answer:** Record index version, filter policy version, candidate IDs, scores, rank, and final supplied sources. Avoid raw sensitive chunks when IDs suffice. Preserve enough detail to reproduce a wrong answer using authorized access. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Retrieval traces; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 13. You are about to deploy safety bias and toxicity. What design and acceptance checks do you require?

**Expected answer:** Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Safety bias and toxicity; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 14. You are about to deploy prompt and model versions. What design and acceptance checks do you require?

**Expected answer:** Attach prompt hash, output schema revision, model identifier, adapter revision, and sampling configuration. Hosted model aliases can change behavior. Versioning makes regressions diagnosable even when the provider does not expose exact internal weights. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Prompt and model versions; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 15. You are about to deploy latency cost and tokens. What design and acceptance checks do you require?

**Expected answer:** Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Latency cost and tokens; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 16. You are about to deploy langsmith. What design and acceptance checks do you require?

**Expected answer:** LangSmith offers tracing, evaluation, and dataset workflows across supported applications. Treat exported traces as sensitive data. Configure redaction, sampling, and access. Instrumentation needs its own failure policy so unavailable telemetry does not crash every request. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for LangSmith; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 17. You are about to deploy agent evaluation. What design and acceptance checks do you require?

**Expected answer:** Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Agent evaluation; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 18. You are about to deploy opentelemetry. What design and acceptance checks do you require?

**Expected answer:** OpenTelemetry provides vendor-neutral instrumentation and context propagation concepts. Use spans, metrics, and exporters compatible with your infrastructure. Keep high-cardinality values out of metric labels; request IDs belong in logs and traces. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for OpenTelemetry; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 19. You are about to deploy regression and release gates. What design and acceptance checks do you require?

**Expected answer:** Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

**Deep follow-up:** A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for Regression and release gates; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.

## 20. You are about to deploy mlflow and operations. What design and acceptance checks do you require?

**Expected answer:** MLflow concepts help track experiments, parameters, metrics, artifacts, and model versions. An experiment tracker does not replace runtime incident response. Define SLOs, alert owners, runbooks, retention, and restore procedures. Run a simulated incident to prove the dashboard is actionable. Compare usage by prompt version, model, tenant, task, retries, tool loops, and retrieved context size. Correlate the change with releases and traffic mix, then isolate the stage responsible.

**Deep follow-up:** Check whether measurement changed before assuming behavior changed. Distinguish input growth from output growth and billed token categories. Inspect conversation trimming, duplicated retrieval chunks, expanded tool schemas, retries, and looping agents. Compare cost per successful task and volume separately. A prompt rollback may help, but only if traces show that prompt version caused the growth. Keep privacy-preserving records sufficient to reproduce the path.

**Ask next:** How would you roll back this change?

**Rubric:** Accurate mechanism for MLflow and operations; Concrete implementation example; Relevant trade-off; Failure and permission boundary; Clear concise explanation.
