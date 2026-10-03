# Mock interviews

Ten rounds contain twenty questions each. The terminal runner asks one question, waits for your answer, then reveals the expected points and a self-assessment rubric.

```bash
python scripts/mock_interview.py --round 1
python scripts/mock_interview.py --round 4 --start 5
```

It does not automatically judge semantic correctness. For a deeper interview, use the chat protocol with a human or assistant who can review your actual explanation. Self-assessment scores are local study notes, not a certification.

| Round | Topic | Questions |
|---|---|---|
| 1 | Fundamentals | [20 prompts](round-01/questions.md) |
| 2 | Python and Backend | [20 prompts](round-02/questions.md) |
| 3 | LLMs | [20 prompts](round-03/questions.md) |
| 4 | RAG | [20 prompts](round-04/questions.md) |
| 5 | LangChain | [20 prompts](round-05/questions.md) |
| 6 | LangGraph and Agents | [20 prompts](round-06/questions.md) |
| 7 | Evaluation | [20 prompts](round-07/questions.md) |
| 8 | System Design | [20 prompts](round-08/questions.md) |
| 9 | Production | [20 prompts](round-09/questions.md) |
| 10 | Senior and Expert | [20 prompts](round-10/questions.md) |
