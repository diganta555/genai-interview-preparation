# Assignment: LLM Evaluation System

Read this first and implement before opening solution.md.

## Requirements

Version cases and configurations, run deterministic checks, support semantic review, and compare two configurations without tuning on the final test set.

## Constraints

Python 3.12; synthetic data first; no credentials in Git; hard permissions in code; bounded tool/model calls. The offline baseline is allowed, but clearly distinguish it from live integrations. State your time and deployment assumptions.

## Expected APIs

POST /eval/runs; GET /eval/runs/{id}; POST /eval/reviews.

## Expected architecture

JSONL dataset → runner → structural/retrieval checks → human or calibrated judge → per-case report.

## Test cases

Try malformed records, schema failures, wrong-but-present citations, correct abstention, failed requests, and slice-level regression.

## Evaluation criteria

Correctness 30%; validation and security 25%; failure handling 15%; tests and evaluation 15%; architecture explanation and documentation 15%. These are exercise grading weights, not an employer’s official rubric.

## Production considerations

Explain data lifecycle, identity, deadlines, quotas, telemetry, deployment, and rollback. Show at least one measured result with the exact configuration and one remaining limitation.

## Submission

README, runnable baseline, meaningful tests, example requests, per-case report, architecture decisions, and no real secrets. Commit your attempt before reading the separate solution guidance.
