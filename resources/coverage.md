# Topic coverage

## [Python for GenAI](../01-python/README.md)

Fundamentals and data structures, OOP and dependency injection, Decorators, Iterators and generators, Context managers, Async and concurrency, Threading and multiprocessing, Types and Pydantic, Errors and logging, Environment and dependencies.

## [Machine Learning Fundamentals](../02-ml-fundamentals/README.md)

Supervised learning, Unsupervised learning and clustering, Feature engineering, Overfitting and underfitting, Train validation test, Cross-validation, Precision recall and F1, ROC-AUC and imbalance, Embeddings, Dimensionality reduction.

## [Deep Learning Fundamentals](../03-deep-learning/README.md)

Neural networks, Backpropagation, Activation functions, Loss functions, Optimization, CNN, RNN, LSTM, Attention, Why transformers.

## [Transformers](../04-transformers/README.md)

Tokenization, Token embeddings and positions, Query key value, Scaled dot-product attention, Multi-head attention, Feed-forward networks, Residual connections and normalization, Encoder and decoder, Causal language modeling, Generation and KV cache.

## [LLM Fundamentals](../05-llm-fundamentals/README.md)

Architecture and inference, Tokens and context window, Temperature top-k top-p, Max tokens and stopping, Messages and roles, Structured output, Function and tool calling, Streaming, Batching latency throughput, Provider abstraction.

## [Prompt Engineering](../06-prompt-engineering/README.md)

Zero-shot and few-shot, Reasoning concepts, Role prompting, Structured prompts, Output constraints, Templates, Versioning and optimization, Prompt injection, Task-specific prompts, Failure analysis.

## [Embeddings and Similarity](../07-embeddings/README.md)

Vector representation, Cosine similarity, Euclidean distance, Normalization, Dimensions and storage, Model selection, Query and document encoding, Semantic search, Migration and versioning, Updating and deleting.

## [Vector Databases](../08-vector-databases/README.md)

FAISS, Chroma, Pinecone, Qdrant, Weaviate, Exact and ANN indexes, Metadata filtering, Hybrid search, Collections namespaces persistence, Scalability latency cost.

## [Retrieval-Augmented Generation](../09-rag/README.md)

Document loading, Recursive chunking, Semantic chunking, Parent-child chunking, Metadata and ingestion, Retrieval and rewriting, Hybrid reranking and compression, Prompt and answer, Citations, Testing and hallucination reduction.

## [Advanced RAG and Scale](../10-advanced-rag/README.md)

500000-document design, Irrelevant results, Correct answer wrong citation, Correct context wrong answer, Variable answers, Multi-query and decomposition, Reranking and relevance, Freshness and lifecycle, Evaluation experiments, Scaling and failure.

## [LangChain](../11-langchain/README.md)

Prompts and templates, Models and provider switching, Output parsers, Runnable and LCEL, Chains and boundaries, Retrievers and vector stores, Loaders and splitters, Callbacks and tracing, Memory concepts, Tools and agents, LlamaIndex comparison.

## [Custom Tools](../12-tools/README.md)

Schema and validation, Calculator, Weather API, Database tool, Search tool, Internal employee tool, File processing tool, Execution and errors, Retries and timeouts, Selection and approval.

## [Function Calling and Tool Calling](../13-function-calling/README.md)

Normal model call, Structured output, Function versus tool calling, Decision and arguments, Application execution, Results and final answer, Agent distinction, Parallel and dependent tools, Loop boundaries, Protocol testing.

## [LangGraph](../14-langgraph/README.md)

State, Nodes and updates, Edges START END, Conditional edges, Loops and budgets, Checkpoints, Persistence and side effects, Human-in-the-loop, Retries and tools, Progressive graphs.

## [AI Agents](../15-agents/README.md)

LLM chain workflow agent, Planning, Reasoning and observation, Tools, State and execution, Memory, Retries and reflection, Research and document agents, SQL support and coding agents, When not to use agents.

## [Memory](../16-memory/README.md)

Conversation and short-term memory, Long-term memory, Semantic memory, Episodic memory, User profile memory, Vector memory, Memory versus database, Summarization and drift, Poisoning and permissions, Retention and deletion.

## [Multi-Agent Systems](../17-multi-agent/README.md)

Supervisor and workers, Specialist agents, Planner executor, Sequential agents, Parallel agents, Communication contracts, State sharing, Fact checking, Budget and termination, Research architecture.

## [Fine-Tuning](../18-fine-tuning/README.md)

Pretraining, Instruction tuning and SFT, LoRA, QLoRA, PEFT, Dataset preparation, Training, Evaluation, Catastrophic forgetting, RAG versus tuning.

## [LLM and Agent Evaluation](../19-llm-evaluation/README.md)

Correctness and relevance, Faithfulness groundedness hallucination, Retrieval evaluation, Code-based evaluation, LLM-as-a-judge, Human evaluation, Safety bias and toxicity, Latency cost and tokens, Agent evaluation, Regression and release gates.

## [LLM Observability](../20-observability/README.md)

Structured logging, Tracing, Tokens and cost, Latency and errors, Tool traces, Retrieval traces, Prompt and model versions, LangSmith, OpenTelemetry, MLflow and operations.

## [Guardrails and Security](../21-security/README.md)

Authentication and authorization, Prompt injection and indirect injection, Jailbreaks, Data leakage and PII, Tool abuse and excessive agency, SQL injection, Output validation, SSRF and file security, Attack scenarios, Testing and incident response.

## [LLM Cost Optimization](../22-cost-optimization/README.md)

Cost accounting, Model routing, Prompt compression, Smaller and local models, Batching, Token reduction, Exact response caching, Semantic caching, Retrieval optimization, Fallback and rollout.

## [LLM System Design](../23-system-design/README.md)

Requirements, APIs and contracts, Database and search, Caching and queues, Model layer, Scaling, Reliability, Security and observability, Cost and trade-offs, Eight designs.

## [Production GenAI Services](../24-production/README.md)

API architecture, Authentication and rate limiting, Retries and timeouts, Circuit breakers, Queues and backpressure, Caching, Streaming and disconnects, Concurrency and scaling, Monitoring and alerting, CI CD and rollout.

## [Docker and Deployment](../25-docker/README.md)

Docker images, Compose services, FastAPI process, Persistent volumes, Secrets and configuration, Health readiness liveness, Networking and TLS, ECS EKS and orchestration, Deployment strategy, Included stack boundary.

## [AWS for GenAI](../26-aws/README.md)

S3, EC2, ECS and EKS, Lambda, RDS, ElastiCache, CloudWatch, IAM and Secrets Manager, API Gateway, Bedrock and architecture.

## [Databases and GenAI](../27-database/README.md)

SQL fundamentals, PostgreSQL and MySQL, Redis, Text-to-SQL, SQL agents, Injection prevention, Aggregations and semantics, Metadata filtering, Relational plus vector search, Testing and audit.

## [Real-World Debugging](../28-debugging/README.md)

Irrelevant RAG results, Embedding failures, Slow vector search, Hallucinated answers and citations, Token and latency spikes, Infinite loops and invalid tools, Dangerous database queries, Injection and memory errors, Provider outage, Streaming stops.

## [GenAI Coding Interviews](../29-coding-interview/README.md)

Python exercises, API exercises, Async exercises, Embedding and similarity, Chunking exercises, Retrieval and hybrid, RAG exercises, Tools and agents, Evaluation exercises, Difficulty progression.

## [Project-Based Interview Preparation](../30-projects/README.md)

Production-style RAG, Customer support agent, Research agent, SQL agent, Document intelligence, AI question bank, Evaluation platform, Multi-agent research, Enterprise knowledge assistant, Cost optimization router.

The learning reference covers the listed technologies. Live integration examples are limited to the explicitly named optional adapters; provisioning a service is not proof of integration.
