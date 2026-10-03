# Assignment: SQL Agent

Read this first and implement before opening solution.md.

## Requirements

Answer aggregate questions using scoped read-only data. Define paid/refund/currency/date semantics and return no invented rows.

## Constraints

Python 3.12; synthetic data first; no credentials in Git; hard permissions in code; bounded tool/model calls. The offline baseline is allowed, but clearly distinguish it from live integrations. State your time and deployment assumptions.

## Expected APIs

POST /analytics/query.

## Expected architecture

Validated typed plan → parameterized SQL → row limits → result explanation.

## Test cases

Try empty results, exact threshold, refund rows, canceled orders, ambiguous dates, malformed plans, and cross-tenant attempts.

## Evaluation criteria

Correctness 30%; validation and security 25%; failure handling 15%; tests and evaluation 15%; architecture explanation and documentation 15%. These are exercise grading weights, not an employer’s official rubric.

## Production considerations

Explain data lifecycle, identity, deadlines, quotas, telemetry, deployment, and rollback. Show at least one measured result with the exact configuration and one remaining limitation.

## Submission

README, runnable baseline, meaningful tests, example requests, per-case report, architecture decisions, and no real secrets. Commit your attempt before reading the separate solution guidance.
