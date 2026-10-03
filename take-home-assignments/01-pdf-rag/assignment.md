# Assignment: PDF RAG

Read this first and implement before opening solution.md.

## Requirements

Accept approved PDFs, preserve page provenance, answer with source spans or abstain, and handle scanned or malformed files.

## Constraints

Python 3.12; synthetic data first; no credentials in Git; hard permissions in code; bounded tool/model calls. The offline baseline is allowed, but clearly distinguish it from live integrations. State your time and deployment assumptions.

## Expected APIs

POST /documents; GET /jobs/{id}; POST /query.

## Expected architecture

Upload worker → extraction/OCR → chunks → filtered retrieval → model → source checks.

## Test cases

Try a two-page text PDF, a scanned page, missing facts, conflicting dates, an injected instruction, and another tenant’s document.

## Evaluation criteria

Correctness 30%; validation and security 25%; failure handling 15%; tests and evaluation 15%; architecture explanation and documentation 15%. These are exercise grading weights, not an employer’s official rubric.

## Production considerations

Explain data lifecycle, identity, deadlines, quotas, telemetry, deployment, and rollback. Show at least one measured result with the exact configuration and one remaining limitation.

## Submission

README, runnable baseline, meaningful tests, example requests, per-case report, architecture decisions, and no real secrets. Commit your attempt before reading the separate solution guidance.
