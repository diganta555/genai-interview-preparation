# Top 50 Evaluation

Answer aloud before revealing the sections. Repeated concepts use different engineering lenses. Code pointers are implementation references, not complete bespoke solutions for every scenario.

## Question 1: You are about to deploy correctness and relevance. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply correctness and relevance in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating correctness and relevance as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 2: You are about to deploy faithfulness groundedness hallucination. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply faithfulness groundedness hallucination in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating faithfulness groundedness hallucination as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 3: You are about to deploy retrieval evaluation. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply retrieval evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Recall@k measures how many known relevant documents appear in the candidate set. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating retrieval evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 4: You are about to deploy code-based evaluation. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply code-based evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating code-based evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 5: You are about to deploy llm-as-a-judge. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply llm-as-a-judge in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

A judge model scores answers against a structured rubric and evidence. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating llm-as-a-judge as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 6: You are about to deploy human evaluation. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply human evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Humans assess nuanced correctness and business impact. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating human evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 7: You are about to deploy safety bias and toxicity. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply safety bias and toxicity in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Define representative slices and context-specific harms. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating safety bias and toxicity as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 8: You are about to deploy latency cost and tokens. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply latency cost and tokens in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating latency cost and tokens as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 9: You are about to deploy agent evaluation. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply agent evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating agent evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 10: You are about to deploy regression and release gates. What design and acceptance checks do you require?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply regression and release gates in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Version datasets, prompts, models, indexes, and evaluators. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout.

### Interview Answer

Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set. Separate the component contract from its surrounding dependencies. Define inputs, outputs, versioning, permissions, and a measurable acceptance gate before rollout. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How would you roll back this change?

### Follow-up Answer

Keep the last tested configuration and compatible data version available. Test rollback of both application behavior and derived artifacts; a container rollback alone may not restore data semantics.

### Common Mistake

Treating regression and release gates as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 11: After a release, correctness and relevance behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply correctness and relevance in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating correctness and relevance as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 12: After a release, faithfulness groundedness hallucination behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply faithfulness groundedness hallucination in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating faithfulness groundedness hallucination as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 13: After a release, retrieval evaluation behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply retrieval evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Recall@k measures how many known relevant documents appear in the candidate set. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating retrieval evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 14: After a release, code-based evaluation behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply code-based evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating code-based evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 15: After a release, llm-as-a-judge behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply llm-as-a-judge in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

A judge model scores answers against a structured rubric and evidence. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating llm-as-a-judge as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 16: After a release, human evaluation behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply human evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Humans assess nuanced correctness and business impact. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating human evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 17: After a release, safety bias and toxicity behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply safety bias and toxicity in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Define representative slices and context-specific harms. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating safety bias and toxicity as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 18: After a release, latency cost and tokens behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply latency cost and tokens in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating latency cost and tokens as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 19: After a release, agent evaluation behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply agent evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating agent evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 20: After a release, regression and release gates behaves differently on the same user requests. How would you investigate?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply regression and release gates in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Version datasets, prompts, models, indexes, and evaluators. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause.

### Interview Answer

Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set. Reproduce a failing case with the exact versions and inputs, compare one stage at a time with the previous baseline, and change only the demonstrated cause. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What if the aggregate score is unchanged?

### Follow-up Answer

Inspect slices and individual failures. Gains on common cases can hide regressions on rare languages, permissions, long inputs, or critical business cases. Use paired comparisons and hard-invariant gates.

### Common Mistake

Treating regression and release gates as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 21: How would you demonstrate that a change involving correctness and relevance actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply correctness and relevance in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating correctness and relevance as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 22: How would you demonstrate that a change involving faithfulness groundedness hallucination actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply faithfulness groundedness hallucination in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating faithfulness groundedness hallucination as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 23: How would you demonstrate that a change involving retrieval evaluation actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply retrieval evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Recall@k measures how many known relevant documents appear in the candidate set. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating retrieval evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 24: How would you demonstrate that a change involving code-based evaluation actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply code-based evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating code-based evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 25: How would you demonstrate that a change involving llm-as-a-judge actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply llm-as-a-judge in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

A judge model scores answers against a structured rubric and evidence. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating llm-as-a-judge as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 26: How would you demonstrate that a change involving human evaluation actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply human evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Humans assess nuanced correctness and business impact. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating human evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 27: How would you demonstrate that a change involving safety bias and toxicity actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply safety bias and toxicity in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Define representative slices and context-specific harms. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating safety bias and toxicity as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 28: How would you demonstrate that a change involving latency cost and tokens actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply latency cost and tokens in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating latency cost and tokens as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 29: How would you demonstrate that a change involving agent evaluation actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply agent evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating agent evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 30: How would you demonstrate that a change involving regression and release gates actually helps?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply regression and release gates in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Version datasets, prompts, models, indexes, and evaluators. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible.

### Interview Answer

Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set. Choose an independent benchmark and explicit success criteria, measure a fixed baseline, and compare the candidate on the same cases with quality, cost, and latency visible. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

How do you avoid overfitting the benchmark?

### Follow-up Answer

Use separate development and untouched test sets, split correlated records by source or time, and add periodic representative new cases. Record what was tuned and inspect uncertainty.

### Common Mistake

Treating regression and release gates as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 31: What trade-offs would make you choose a simpler alternative to correctness and relevance?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply correctness and relevance in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating correctness and relevance as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 32: What trade-offs would make you choose a simpler alternative to faithfulness groundedness hallucination?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply faithfulness groundedness hallucination in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating faithfulness groundedness hallucination as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 33: What trade-offs would make you choose a simpler alternative to retrieval evaluation?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply retrieval evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Recall@k measures how many known relevant documents appear in the candidate set. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating retrieval evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 34: What trade-offs would make you choose a simpler alternative to code-based evaluation?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply code-based evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating code-based evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 35: What trade-offs would make you choose a simpler alternative to llm-as-a-judge?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply llm-as-a-judge in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

A judge model scores answers against a structured rubric and evidence. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating llm-as-a-judge as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 36: What trade-offs would make you choose a simpler alternative to human evaluation?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply human evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Humans assess nuanced correctness and business impact. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating human evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 37: What trade-offs would make you choose a simpler alternative to safety bias and toxicity?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply safety bias and toxicity in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Define representative slices and context-specific harms. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating safety bias and toxicity as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 38: What trade-offs would make you choose a simpler alternative to latency cost and tokens?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply latency cost and tokens in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating latency cost and tokens as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 39: What trade-offs would make you choose a simpler alternative to agent evaluation?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply agent evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating agent evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 40: What trade-offs would make you choose a simpler alternative to regression and release gates?

### Difficulty

Medium

### What interviewer is testing

Whether you can apply regression and release gates in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Version datasets, prompts, models, indexes, and evaluators. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better.

### Interview Answer

Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set. Choose the least complex design that meets the task contract. Compare quality, operational work, failure surface, latency, and cost rather than assuming more components are better. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

What would make you change your decision?

### Follow-up Answer

A measured requirement gap: lower quality on important cases, insufficient capacity, unacceptable recovery, or an operational burden that a better-supported design resolves. Benchmark before migrating.

### Common Mistake

Treating regression and release gates as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 41: What trusted boundaries must surround correctness and relevance in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply correctness and relevance in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. A fluent relevant answer can still be wrong. Define acceptable alternatives and edge cases in a rubric rather than comparing every answer character-for-character.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating correctness and relevance as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 42: What trusted boundaries must surround faithfulness groundedness hallucination in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply faithfulness groundedness hallucination in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. Hallucination is an unsupported or incorrect generated claim according to the chosen rubric. An answer can be faithful to an outdated document and factually obsolete. State the metric definitions explicitly.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating faithfulness groundedness hallucination as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 43: What trusted boundaries must surround retrieval evaluation in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply retrieval evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Recall@k measures how many known relevant documents appear in the candidate set. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Recall@k measures how many known relevant documents appear in the candidate set. MRR emphasizes the first relevant rank; nDCG accounts for graded relevance. Gold relevance labels are often incomplete, so inspect apparently false positives. Evaluate authorized relevance rather than treating forbidden documents as valid hits.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating retrieval evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 44: What trusted boundaries must surround code-based evaluation in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply code-based evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. These checks are fast and repeatable. They cannot alone measure every semantic quality. Matching a keyword does not prove that an answer correctly addresses a question.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating code-based evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 45: What trusted boundaries must surround llm-as-a-judge in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply llm-as-a-judge in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

A judge model scores answers against a structured rubric and evidence. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: A judge model scores answers against a structured rubric and evidence. Calibrate it against human labels and test sensitivity to ordering, verbosity, and injection. Use blinded comparisons where possible. Judge agreement is not ground truth; avoid self-grading without independent evidence.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating llm-as-a-judge as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 46: What trusted boundaries must surround human evaluation in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply human evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Humans assess nuanced correctness and business impact. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Humans assess nuanced correctness and business impact. Provide clear rubrics, examples, and adjudication for disagreement. Measure inter-rater consistency. Use targeted review of critical slices and failures rather than only random happy-path samples.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating human evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 47: What trusted boundaries must surround safety bias and toxicity in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply safety bias and toxicity in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Define representative slices and context-specific harms. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Define representative slices and context-specific harms. Separate undesired content from legitimate discussion or quoted evidence. Test refusal quality and overblocking. Safety evaluation must include actions and data access, not only final text.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating safety bias and toxicity as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 48: What trusted boundaries must surround latency cost and tokens in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply latency cost and tokens in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. Include failed requests and retries. Synthetic model rates in a lab are not vendor price quotes. Measure actual billed categories when deploying.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating latency cost and tokens as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 49: What trusted boundaries must surround agent evaluation in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply agent evaluation in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. An agent that says done without performing the operation fails. Use tool traces and authoritative outcomes. Test loops, partial failures, and repeated writes.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating agent evaluation as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.

## Question 50: What trusted boundaries must surround regression and release gates in a multi-tenant application?

### Difficulty

Hard

### What interviewer is testing

Whether you can apply regression and release gates in a real llm and agent evaluation system and explain the relevant failure boundary.

### Short Answer

Version datasets, prompts, models, indexes, and evaluators. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts.

### Interview Answer

Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set. Derive identity from trusted authentication, validate input and outputs, enforce data and action permissions in code, scope stored state, and test cross-tenant attempts. In this application, I would make the assumptions explicit, compare the observed result with the stated contract, and keep a reproducible case showing why the chosen behavior is correct. I would also check the impact on the module scenario: How would you build an LLM evaluation POC that proves something useful?

### Deep Technical Answer

A POC can use 30 to 100 carefully chosen cases, but that sample does not establish universal reliability. Include answerable, unanswerable, contradictory, injection, and permission cases. Store JSONL with case IDs, source versions, expected facts, and permitted tool outcomes. Use code checks for hard invariants and human or calibrated judge review for semantic quality. Report counts and confidence, not just a single average. Preserve inputs and configuration so results can be reproduced. For this question, the specific mechanism is: Version datasets, prompts, models, indexes, and evaluators. Use representative held-out cases and slice-level release gates. Track paired changes and confidence intervals. Online A/B tests complement offline evaluation; never tune repeatedly on the final test set.

### Real-World Example

How would you build an LLM evaluation POC that proves something useful? Apply the checks above to that scenario and show the stage-level evidence before changing configuration.

### Code

See [evaluate.py](../examples/evaluate.py) and the corresponding module chapter. The runnable example demonstrates a specific mechanism; integration and production gaps are stated in its documentation.

### Follow-up Question

Can prompt instructions enforce this boundary?

### Follow-up Answer

No. Prompts can guide model behavior, but deterministic authorization and capability limits protect data and actions even when a model follows malicious input.

### Common Mistake

Treating regression and release gates as a universal solution while ignoring the stated input assumptions, permissions, and observable failure modes.

### Senior-Level Insight

Explain what you would measure before a change and what result would falsify your design assumption. Create a small representative labeled dataset, define deterministic and semantic rubrics, run a fixed baseline, record quality, citations, latency, and cost, and compare one controlled change. Manually inspect failures and calibrate any judge.
