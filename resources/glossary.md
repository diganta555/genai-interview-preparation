# Glossary

## Fundamentals and data structures

Use lists for ordered chunks, dictionaries for records keyed by ID, sets for deduplication, and tuples for immutable coordinates. See [Python for GenAI](../01-python/README.md).

## OOP and dependency injection

A provider interface separates business logic from one vendor SDK. See [Python for GenAI](../01-python/README.md).

## Decorators

A decorator wraps a function to add behavior such as tracing or timing. See [Python for GenAI](../01-python/README.md).

## Iterators and generators

An iterator produces values on demand; a generator implements this with yield. See [Python for GenAI](../01-python/README.md).

## Context managers

with and async with express resource lifetime. See [Python for GenAI](../01-python/README.md).

## Async and concurrency

async/await lets one thread serve other work while waiting for compatible nonblocking I/O. See [Python for GenAI](../01-python/README.md).

## Threading and multiprocessing

Threads can isolate blocking I/O libraries; processes can parallelize CPU work on conventional GIL-enabled CPython. See [Python for GenAI](../01-python/README.md).

## Types and Pydantic

Type hints document contracts and support static checks; Python does not enforce them automatically. See [Python for GenAI](../01-python/README.md).

## Errors and logging

Classify validation failures, rate limits, transient network failures, and permanent authorization failures. See [Python for GenAI](../01-python/README.md).

## Environment and dependencies

Use Python 3.12 with uv or venv for these labs. See [Python for GenAI](../01-python/README.md).

## Supervised learning

Learn from labeled input-output pairs. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Unsupervised learning and clustering

Discover structure without target labels. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Feature engineering

Construct informative inputs such as query length, language, domain, retrieved score gap, or recent error rate. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Overfitting and underfitting

Overfitting memorizes training specifics; underfitting misses useful structure. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Train validation test

Train fits parameters, validation chooses configurations, and test estimates final generalization. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Cross-validation

Repeat training and validation across folds to estimate variability. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Precision recall and F1

Precision is TP/(TP+FP); recall is TP/(TP+FN); F1 is their harmonic mean. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## ROC-AUC and imbalance

ROC-AUC summarizes ranking across thresholds through true-positive and false-positive rates. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Embeddings

Embeddings are learned features represented as vectors. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Dimensionality reduction

PCA finds directions of high variance and can reduce storage or visualize structure. See [Machine Learning Fundamentals](../02-ml-fundamentals/README.md).

## Neural networks

A layer computes a weighted transformation followed by a nonlinearity. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## Backpropagation

The chain rule propagates loss gradients through the network. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## Activation functions

ReLU, GELU, sigmoid, and tanh introduce nonlinearity. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## Loss functions

Cross-entropy compares predicted token probabilities with the target token. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## Optimization

SGD and Adam-like optimizers adjust weights. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## CNN

Convolutions apply shared local filters, useful for spatial features in images. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## RNN

An RNN carries a hidden state across a sequence. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## LSTM

LSTM gates control which information to store, forget, and expose. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## Attention

Attention weights relevant positions based on the current representation. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## Why transformers

Transformers allow parallel processing of sequence positions during training and flexible interactions through attention. See [Deep Learning Fundamentals](../03-deep-learning/README.md).

## Tokenization

Tokenizers map text to token IDs using learned subword vocabularies or related methods. See [Transformers](../04-transformers/README.md).

## Token embeddings and positions

Each token ID indexes a learned embedding. See [Transformers](../04-transformers/README.md).

## Query key value

Project each representation into Q, K, and V. See [Transformers](../04-transformers/README.md).

## Scaled dot-product attention

Attention(Q,K,V) = softmax(QKᵀ/√d_k + mask)V. See [Transformers](../04-transformers/README.md).

## Multi-head attention

Different heads use different learned projections and can represent different relations. See [Transformers](../04-transformers/README.md).

## Feed-forward networks

Each token representation passes through a position-wise nonlinear network, often expanding then contracting the hidden dimension. See [Transformers](../04-transformers/README.md).

## Residual connections and normalization

Residual paths add earlier representations to sublayer outputs, improving gradient flow. See [Transformers](../04-transformers/README.md).

## Encoder and decoder

Encoders usually attend bidirectionally and are useful for representations. See [Transformers](../04-transformers/README.md).

## Causal language modeling

Training uses shifted targets: previous tokens predict the following token. See [Transformers](../04-transformers/README.md).

## Generation and KV cache

Prefill computes representations for the prompt; decode generates subsequent tokens. See [Transformers](../04-transformers/README.md).

## Architecture and inference

Many chat models are decoder transformers, but architectures vary. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Tokens and context window

The input, conversation history, tool messages, and generated output share context constraints according to the provider’s accounting rules. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Temperature top-k top-p

Temperature rescales logits; lower values usually concentrate probability. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Max tokens and stopping

An output cap bounds generated length and cost. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Messages and roles

System or developer instructions describe behavior, user messages express requests, assistant messages carry responses, and tool messages return observations. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Structured output

Schema-constrained generation can improve syntactic reliability. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Function and tool calling

The model proposes a tool name and arguments; the application executes the call. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Streaming

Send incremental output to reduce perceived latency. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Batching latency throughput

Batching can amortize overhead and improve throughput, but may increase individual waiting time. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Provider abstraction

Normalize messages, usage, errors, and capabilities behind a small interface. See [LLM Fundamentals](../05-llm-fundamentals/README.md).

## Zero-shot and few-shot

Zero-shot gives instructions without examples; few-shot adds representative input-output pairs. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Reasoning concepts

Multi-step tasks can benefit from decomposition, intermediate calculations, and verifiable plans. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Role prompting

A role can set tone and domain expectations but does not grant real expertise or system permissions. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Structured prompts

Use clear sections for task, context, constraints, examples, and output. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Output constraints

Specify the schema, supported citation IDs, null behavior, and maximum length. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Templates

A template fills a stable instruction skeleton with request-specific data. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Versioning and optimization

Change prompts through review, offline evaluation, and limited traffic rollout. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Prompt injection

Injection occurs when untrusted input attempts to override intended behavior. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Task-specific prompts

Customer support should use policy evidence and escalation. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Failure analysis

Compare instruction compliance, factual accuracy, format validity, and retrieval sufficiency separately. See [Prompt Engineering](../06-prompt-engineering/README.md).

## Vector representation

A dense embedding has one numeric value per dimension. See [Embeddings and Similarity](../07-embeddings/README.md).

## Cosine similarity

Cosine is dot(a,b)/(norm(a) norm(b)). See [Embeddings and Similarity](../07-embeddings/README.md).

## Euclidean distance

Euclidean distance is the length of the difference vector. See [Embeddings and Similarity](../07-embeddings/README.md).

## Normalization

Divide a vector by its norm to make its length one. See [Embeddings and Similarity](../07-embeddings/README.md).

## Dimensions and storage

Raw float32 storage is N × d × 4 bytes, excluding IDs, metadata, replicas, and index overhead. See [Embeddings and Similarity](../07-embeddings/README.md).

## Model selection

Compare domain retrieval, languages, short versus long inputs, latency, embedding cost, and licensing. See [Embeddings and Similarity](../07-embeddings/README.md).

## Query and document encoding

Some models use different instructions or functions for queries and documents. See [Embeddings and Similarity](../07-embeddings/README.md).

## Semantic search

Encode a query, retrieve nearest candidates, apply permissions, optionally rerank, then inspect results. See [Embeddings and Similarity](../07-embeddings/README.md).

## Migration and versioning

Store embedding model, revision, preprocessing, and dimension with each index version. See [Embeddings and Similarity](../07-embeddings/README.md).

## Updating and deleting

Changing document text requires new embeddings. See [Embeddings and Similarity](../07-embeddings/README.md).

## FAISS

FAISS provides local similarity-search algorithms, including exact and approximate indexes. See [Vector Databases](../08-vector-databases/README.md).

## Chroma

Chroma supports collections, persistence, retrieval, and metadata operations. See [Vector Databases](../08-vector-databases/README.md).

## Pinecone

Pinecone offers managed vector infrastructure. See [Vector Databases](../08-vector-databases/README.md).

## Qdrant

Qdrant exposes vector search with payload filtering and collection management. See [Vector Databases](../08-vector-databases/README.md).

## Weaviate

Weaviate combines object data and search capabilities, with configurations for vectorization and hybrid retrieval. See [Vector Databases](../08-vector-databases/README.md).

## Exact and ANN indexes

Exact search compares every vector and provides a correctness baseline. See [Vector Databases](../08-vector-databases/README.md).

## Metadata filtering

Filter by tenant, user permissions, document state, date, and type. See [Vector Databases](../08-vector-databases/README.md).

## Hybrid search

Combine dense retrieval with lexical retrieval such as BM25. See [Vector Databases](../08-vector-databases/README.md).

## Collections namespaces persistence

Choose organization from lifecycle and isolation requirements. See [Vector Databases](../08-vector-databases/README.md).

## Scalability latency cost

Estimate vector bytes, metadata, index overhead, replicas, ingest throughput, query QPS, and filter selectivity. See [Vector Databases](../08-vector-databases/README.md).

## Document loading

Read source bytes, extract text and layout, and retain source identifiers, page numbers, versions, and permissions. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Recursive chunking

Split using a hierarchy of separators, trying to preserve paragraphs and sentences within a target budget. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Semantic chunking

Use boundaries based on content transitions, often from embedding changes. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Parent-child chunking

Index small children for precise retrieval and supply their larger parent sections for context. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Metadata and ingestion

Assign stable IDs with document version, chunk offset, language, title, and access attributes. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Retrieval and rewriting

Retrieve candidates using the current question and relevant conversational context. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Hybrid reranking and compression

Fuse lexical and dense candidates, then apply a cross-encoder or other reranker to a bounded set. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Prompt and answer

Pack evidence within a token budget, use explicit source IDs, and define an abstention policy. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Citations

Tie each citation to immutable document version and source span. See [Retrieval-Augmented Generation](../09-rag/README.md).

## Testing and hallucination reduction

Measure parsing coverage, chunk coverage, Recall@k, ranking, answer correctness, faithfulness, abstention, and citation quality separately. See [Retrieval-Augmented Generation](../09-rag/README.md).

## 500000-document design

Estimate average chunks per document before sizing. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Irrelevant results

Inspect actual query, rewriting, corpus coverage, filters, chunk text, embedding revision, index recall, and rank order. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Correct answer wrong citation

Track whether citations refer to parent IDs, child IDs, or source spans. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Correct context wrong answer

Check truncation, confusing source order, units, negatives, conflicting policy versions, and conversation contamination. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Variable answers

Sampling, changing indexes, approximate search, provider model changes, rewriting, and prompt changes can all vary responses. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Multi-query and decomposition

Create paraphrases or subquestions to improve coverage. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Reranking and relevance

Rerank a candidate set larger than the final context. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Freshness and lifecycle

Use change tracking, source checksums, tombstones, and index version aliases. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Evaluation experiments

Separate retrieval, context selection, generation, and citation experiments. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Scaling and failure

Bound query fanout and context length. See [Advanced RAG and Scale](../10-advanced-rag/README.md).

## Prompts and templates

A prompt template formats trusted instructions and request data into messages. See [LangChain](../11-langchain/README.md).

## Models and provider switching

A chat model accepts messages and returns an AI message, often with usage and tool-call metadata. See [LangChain](../11-langchain/README.md).

## Output parsers

Parsers convert model output into a useful form, such as text or a validated object. See [LangChain](../11-langchain/README.md).

## Runnable and LCEL

Runnable supports invoke, ainvoke, batch, and stream style composition. See [LangChain](../11-langchain/README.md).

## Chains and boundaries

A chain is a fixed composition of steps. See [LangChain](../11-langchain/README.md).

## Retrievers and vector stores

A vector store manages stored vectors; a retriever exposes a query-to-documents interface. See [LangChain](../11-langchain/README.md).

## Loaders and splitters

Loaders produce Document objects with text and metadata. See [LangChain](../11-langchain/README.md).

## Callbacks and tracing

Callbacks expose events such as model start, tool end, and errors; LangSmith can collect traces. See [LangChain](../11-langchain/README.md).

## Memory concepts

History is message state, not a magical truth store. See [LangChain](../11-langchain/README.md).

## Tools and agents

Tools are typed capabilities; create_agent supplies a model-driven loop around tools. See [LangChain](../11-langchain/README.md).

## LlamaIndex comparison

LlamaIndex offers document ingestion, indexing, and query-oriented abstractions, including VectorStoreIndex. See [LangChain](../11-langchain/README.md).

## Schema and validation

Describe fields, types, constraints, and units in a tool schema. See [Custom Tools](../12-tools/README.md).

## Calculator

Use explicit operations and numbers instead of eval on model-generated text. See [Custom Tools](../12-tools/README.md).

## Weather API

Accept a city or controlled location ID, use a configured API origin, and set a network timeout. See [Custom Tools](../12-tools/README.md).

## Database tool

Expose a read-only, authorized operation with parameterized values and row limits. See [Custom Tools](../12-tools/README.md).

## Search tool

Call a configured search provider with bounded query length, response count, and timeout. See [Custom Tools](../12-tools/README.md).

## Internal employee tool

Resolve the caller identity from authentication, then enforce field-level and row-level permissions. See [Custom Tools](../12-tools/README.md).

## File processing tool

Parse approved file types in a restricted worker with size, time, and page limits. See [Custom Tools](../12-tools/README.md).

## Execution and errors

Use a tool registry that maps allowed names to functions. See [Custom Tools](../12-tools/README.md).

## Retries and timeouts

Use per-tool deadlines and a total task budget. See [Custom Tools](../12-tools/README.md).

## Selection and approval

Tool descriptions should explain applicability and limits. See [Custom Tools](../12-tools/README.md).

## Normal model call

A normal call produces text or multimodal output. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Structured output

Structured output returns data conforming to a requested schema. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Function versus tool calling

Function calling generally refers to calling application functions; tool calling is the broader provider terminology and may include other tool types. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Decision and arguments

The model selects from offered tools and proposes arguments. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Application execution

Execute through a trusted registry with caller permissions and a deadline. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Results and final answer

Return the observation under the matching tool-call ID, then ask the model to continue. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Agent distinction

One tool call is not necessarily an agent. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Parallel and dependent tools

Independent lookups can run concurrently; a second operation depending on the first result must wait. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Loop boundaries

Set maximum steps, model calls, tool calls, output tokens, elapsed time, and repeat-call limits. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## Protocol testing

Use recorded proposals to test call IDs, argument validation, forbidden names, error handling, and repeated calls. See [Function Calling and Tool Calling](../13-function-calling/README.md).

## State

State is the data carried through the graph, commonly described with TypedDict or another supported schema. See [LangGraph](../14-langgraph/README.md).

## Nodes and updates

A node reads state and returns updates. See [LangGraph](../14-langgraph/README.md).

## Edges START END

START identifies entry and END termination. See [LangGraph](../14-langgraph/README.md).

## Conditional edges

A routing function selects the next node from validated state. See [LangGraph](../14-langgraph/README.md).

## Loops and budgets

Increase a step counter and enforce elapsed-time, token, and repeat-call budgets. See [LangGraph](../14-langgraph/README.md).

## Checkpoints

A checkpointer stores graph state at execution boundaries. See [LangGraph](../14-langgraph/README.md).

## Persistence and side effects

Checkpointing supports recovery; it does not automatically guarantee exactly-once external operations. See [LangGraph](../14-langgraph/README.md).

## Human-in-the-loop

interrupt pauses a workflow and Command(resume=...) supplies the decision. See [LangGraph](../14-langgraph/README.md).

## Retries and tools

Set retry policies for specific transient node failures and deadlines for tools. See [LangGraph](../14-langgraph/README.md).

## Progressive graphs

Build a simple graph, then a RAG graph, then a research loop, support workflow, and specialist orchestration. See [LangGraph](../14-langgraph/README.md).

## LLM chain workflow agent

An LLM generates outputs; a chain composes fixed calls; a workflow branches using explicit rules; an agent lets a model choose actions. See [AI Agents](../15-agents/README.md).

## Planning

A plan decomposes a goal into actions. See [AI Agents](../15-agents/README.md).

## Reasoning and observation

The agent conditions its next choice on tool observations and state. See [AI Agents](../15-agents/README.md).

## Tools

Provide narrow capabilities rather than unrestricted shell, database, or browser access. See [AI Agents](../15-agents/README.md).

## State and execution

Track task goal, progress, evidence, tool calls, errors, and stop reasons. See [AI Agents](../15-agents/README.md).

## Memory

Use session state for the current task and explicit authorized stores for longer-lived information. See [AI Agents](../15-agents/README.md).

## Retries and reflection

Reflection can identify missing work but is another model call with additional cost and potential errors. See [AI Agents](../15-agents/README.md).

## Research and document agents

Research gathers sources, deduplicates facts, compares evidence, and cites claims. See [AI Agents](../15-agents/README.md).

## SQL support and coding agents

SQL agents need read-only scoped operations. See [AI Agents](../15-agents/README.md).

## When not to use agents

Do not use an agent for a deterministic lookup, fixed classification, or a known transactional flow without clear added value. See [AI Agents](../15-agents/README.md).

## Conversation and short-term memory

Conversation history supports pronouns and ongoing tasks. See [Memory](../16-memory/README.md).

## Long-term memory

Persist selected information across sessions when the use case and permissions allow it. See [Memory](../16-memory/README.md).

## Semantic memory

Semantic memory stores facts or knowledge-like descriptions. See [Memory](../16-memory/README.md).

## Episodic memory

Episodic memory stores events such as a prior support incident and outcome. See [Memory](../16-memory/README.md).

## User profile memory

Profiles can store language preference or preferred format. See [Memory](../16-memory/README.md).

## Vector memory

Vector retrieval can find semantically related past records. See [Memory](../16-memory/README.md).

## Memory versus database

Store balances, inventory, policy versions, and employee records in an authoritative database. See [Memory](../16-memory/README.md).

## Summarization and drift

Repeated summarization can lose conditions, dates, negatives, and uncertainty. See [Memory](../16-memory/README.md).

## Poisoning and permissions

An attacker may plant a false preference or instruction in memory. See [Memory](../16-memory/README.md).

## Retention and deletion

Define expiry, export, correction, and deletion across caches, vectors, checkpoints, and backups. See [Memory](../16-memory/README.md).

## Supervisor and workers

A supervisor routes tasks to workers and collects results. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Specialist agents

A specialist may handle retrieval, SQL planning, summarization, or fact checking. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Planner executor

A planner proposes steps; an executor performs permitted actions. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Sequential agents

Sequential stages are useful when one result depends on another: gather evidence, summarize, verify, answer. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Parallel agents

Independent source checks can run concurrently. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Communication contracts

Use typed task and result messages with IDs, evidence, status, confidence, and failure reasons. See [Multi-Agent Systems](../17-multi-agent/README.md).

## State sharing

Use controlled shared state or explicit message passing. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Fact checking

A checker verifies claims against original sources, not only the summarizer’s assertions. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Budget and termination

Allocate total task time, cost, token, and step budgets across workers. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Research architecture

A bounded research workflow can search, collect sources, summarize evidence, check claims, and synthesize. See [Multi-Agent Systems](../17-multi-agent/README.md).

## Pretraining

Pretraining learns broad representations and next-token patterns from large datasets. See [Fine-Tuning](../18-fine-tuning/README.md).

## Instruction tuning and SFT

Supervised fine-tuning trains on task inputs paired with desired outputs. See [Fine-Tuning](../18-fine-tuning/README.md).

## LoRA

LoRA trains low-rank updates to selected weight matrices while freezing base weights. See [Fine-Tuning](../18-fine-tuning/README.md).

## QLoRA

QLoRA uses a quantized frozen base with trainable adapters and related memory-saving techniques. See [Fine-Tuning](../18-fine-tuning/README.md).

## PEFT

Parameter-efficient fine-tuning includes methods that update only selected parameters or small added modules. See [Fine-Tuning](../18-fine-tuning/README.md).

## Dataset preparation

Remove duplicates, secrets, contradictory labels, and evaluation contamination. See [Fine-Tuning](../18-fine-tuning/README.md).

## Training

Choose batch size, gradient accumulation, optimizer, schedule, and maximum sequence length. See [Fine-Tuning](../18-fine-tuning/README.md).

## Evaluation

Compare the base model, prompting, RAG, and tuned model on the same held-out tasks. See [Fine-Tuning](../18-fine-tuning/README.md).

## Catastrophic forgetting

Specialization can degrade capabilities outside the training domain. See [Fine-Tuning](../18-fine-tuning/README.md).

## RAG versus tuning

Use RAG for fresh private knowledge, document permissions, and citations. See [Fine-Tuning](../18-fine-tuning/README.md).

## Correctness and relevance

Correctness asks whether the answer is right under trusted reference facts; relevance asks whether it addresses the request. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Faithfulness groundedness hallucination

Faithfulness or groundedness concerns support by provided evidence, though definitions vary across tools. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Retrieval evaluation

Recall@k measures how many known relevant documents appear in the candidate set. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Code-based evaluation

Use deterministic checks for schema, required fields, cited IDs, permitted tool use, arithmetic, and database outcomes. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## LLM-as-a-judge

A judge model scores answers against a structured rubric and evidence. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Human evaluation

Humans assess nuanced correctness and business impact. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Safety bias and toxicity

Define representative slices and context-specific harms. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Latency cost and tokens

Record wall time, first-token time, p95, errors, input/output usage, tool time, and cost per completed task. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Agent evaluation

Evaluate task completion, tool choice, argument validity, permissions, number of calls, recovery, and side effects. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Regression and release gates

Version datasets, prompts, models, indexes, and evaluators. See [LLM and Agent Evaluation](../19-llm-evaluation/README.md).

## Structured logging

Log JSON events with request ID, stage, safe error code, duration, and version identifiers. See [LLM Observability](../20-observability/README.md).

## Tracing

A trace groups spans for API, retrieval, reranking, model, tools, and database calls. See [LLM Observability](../20-observability/README.md).

## Tokens and cost

Record provider-reported token usage and model configuration. See [LLM Observability](../20-observability/README.md).

## Latency and errors

Track percentiles and error categories, not only average latency. See [LLM Observability](../20-observability/README.md).

## Tool traces

Record allowed tool name, call ID, outcome, duration, and safe argument summary. See [LLM Observability](../20-observability/README.md).

## Retrieval traces

Record index version, filter policy version, candidate IDs, scores, rank, and final supplied sources. See [LLM Observability](../20-observability/README.md).

## Prompt and model versions

Attach prompt hash, output schema revision, model identifier, adapter revision, and sampling configuration. See [LLM Observability](../20-observability/README.md).

## LangSmith

LangSmith offers tracing, evaluation, and dataset workflows across supported applications. See [LLM Observability](../20-observability/README.md).

## OpenTelemetry

OpenTelemetry provides vendor-neutral instrumentation and context propagation concepts. See [LLM Observability](../20-observability/README.md).

## MLflow and operations

MLflow concepts help track experiments, parameters, metrics, artifacts, and model versions. See [LLM Observability](../20-observability/README.md).

## Authentication and authorization

Authentication establishes identity; authorization decides permitted actions and data. See [Guardrails and Security](../21-security/README.md).

## Prompt injection and indirect injection

A user or retrieved source may instruct the model to ignore policy or exfiltrate data. See [Guardrails and Security](../21-security/README.md).

## Jailbreaks

Jailbreaks attempt to defeat behavioral restrictions. See [Guardrails and Security](../21-security/README.md).

## Data leakage and PII

Minimize data sent to models, logs, and evaluators. See [Guardrails and Security](../21-security/README.md).

## Tool abuse and excessive agency

A broad shell or database tool can transform a bad model decision into damage. See [Guardrails and Security](../21-security/README.md).

## SQL injection

Use parameterized values and constrained identifiers. See [Guardrails and Security](../21-security/README.md).

## Output validation

Validate schema, allowed citations, references, numeric bounds, and business invariants. See [Guardrails and Security](../21-security/README.md).

## SSRF and file security

Block private network targets and unsafe redirects when tools fetch URLs. See [Guardrails and Security](../21-security/README.md).

## Attack scenarios

A PDF saying send payroll to this URL must remain evidence, not policy. See [Guardrails and Security](../21-security/README.md).

## Testing and incident response

Maintain adversarial test cases for data access, tool execution, output rendering, and memory poisoning. See [Guardrails and Security](../21-security/README.md).

## Cost accounting

Break spend into model input, output, embeddings, reranking, tools, storage, and infrastructure. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Model routing

Route easy tasks to cheaper suitable models and hard tasks to stronger ones when measured quality justifies it. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Prompt compression

Remove duplicate instructions, obsolete history, and irrelevant evidence before compressing useful content. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Smaller and local models

Smaller models can reduce latency or cost for narrow tasks. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Batching

Offline batch processing may suit ingestion and evaluation when turnaround is flexible. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Token reduction

Cap output appropriately, simplify schemas, avoid sending the same long tool description repeatedly when the protocol permits, and reduce context to relevant spans. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Exact response caching

Cache only when request, tenant, authorization scope, prompt version, model configuration, source version, and relevant user context agree. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Semantic caching

Reuse answers for semantically related queries only when business equivalence is verified. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Retrieval optimization

Reduce duplicate chunks and unnecessary fanout, cache embeddings of safe repeat queries, and tune candidate count. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Fallback and rollout

A fallback should meet task capability and permission requirements. See [LLM Cost Optimization](../22-cost-optimization/README.md).

## Requirements

Clarify user roles, document types, actions, languages, freshness, citations, and allowed mistakes. See [LLM System Design](../23-system-design/README.md).

## APIs and contracts

Define ingestion jobs, status endpoints, queries, conversation IDs, and response evidence. See [LLM System Design](../23-system-design/README.md).

## Database and search

Relational tables hold users, ACLs, source versions, jobs, and audit records. See [LLM System Design](../23-system-design/README.md).

## Caching and queues

Cache safe repeat operations with tenant and version scope. See [LLM System Design](../23-system-design/README.md).

## Model layer

Use provider adapters with capability checks, budgets, and controlled fallback. See [LLM System Design](../23-system-design/README.md).

## Scaling

Size active users and request rate rather than registered users alone. See [LLM System Design](../23-system-design/README.md).

## Reliability

Set total and stage deadlines, classify retryable failures, and stop cascades with circuit breakers and admission control. See [LLM System Design](../23-system-design/README.md).

## Security and observability

Authorize retrieval and tools using authenticated identities. See [LLM System Design](../23-system-design/README.md).

## Cost and trade-offs

Compare cost per completed task and operations overhead. See [LLM System Design](../23-system-design/README.md).

## Eight designs

The separate system-design directory contains worked designs for a chat service, enterprise RAG, support automation, PDF QA, coding assistance, SQL copilot, document intelligence, and multi-agent research. See [LLM System Design](../23-system-design/README.md).

## API architecture

Separate transport validation, authorization, application logic, retrieval, model adapters, and persistence. See [Production GenAI Services](../24-production/README.md).

## Authentication and rate limiting

Use a real identity provider and derive tenant and role from verified identity. See [Production GenAI Services](../24-production/README.md).

## Retries and timeouts

Set connect, read, total stage, and request deadlines. See [Production GenAI Services](../24-production/README.md).

## Circuit breakers

Open a breaker after a measured failure threshold, then probe recovery cautiously. See [Production GenAI Services](../24-production/README.md).

## Queues and backpressure

Queue slow work with job IDs and status. See [Production GenAI Services](../24-production/README.md).

## Caching

Use versioned, authorization-scoped keys and explicit invalidation. See [Production GenAI Services](../24-production/README.md).

## Streaming and disconnects

Define start, token, error, and completion events. See [Production GenAI Services](../24-production/README.md).

## Concurrency and scaling

Limit provider concurrency and CPU parsing separately. See [Production GenAI Services](../24-production/README.md).

## Monitoring and alerting

Monitor request availability, latency, quality samples, retrieval health, token spend, queue lag, and permission failures. See [Production GenAI Services](../24-production/README.md).

## CI CD and rollout

Run unit, contract, integration, evaluation, and adversarial checks appropriate to the change. See [Production GenAI Services](../24-production/README.md).

## Docker images

Build from a supported base, install explicit dependencies, copy only needed files, and run as a non-root user. See [Docker and Deployment](../25-docker/README.md).

## Compose services

Define API, frontend, PostgreSQL, Redis, and Qdrant as separate services in the included local stack. See [Docker and Deployment](../25-docker/README.md).

## FastAPI process

Uvicorn serves ASGI requests. See [Docker and Deployment](../25-docker/README.md).

## Persistent volumes

Volumes keep database state beyond a container restart. See [Docker and Deployment](../25-docker/README.md).

## Secrets and configuration

Load credentials from runtime secrets or environment under the orchestrator. See [Docker and Deployment](../25-docker/README.md).

## Health readiness liveness

Liveness asks whether a process should restart; readiness asks whether it can accept traffic. See [Docker and Deployment](../25-docker/README.md).

## Networking and TLS

Expose only required entrypoints, use TLS at a trusted gateway, and restrict database and cache network access. See [Docker and Deployment](../25-docker/README.md).

## ECS EKS and orchestration

ECS provides managed container scheduling; Kubernetes or EKS offers a broader orchestration system with more operational complexity. See [Docker and Deployment](../25-docker/README.md).

## Deployment strategy

Use immutable artifacts, reviewed configuration, staged migrations, and a canary or rolling rollout. See [Docker and Deployment](../25-docker/README.md).

## Included stack boundary

The Compose file runs the educational API with an offline index and fixture answering plus companion services. See [Docker and Deployment](../25-docker/README.md).

## S3

Store original documents and versioned derived artifacts in object storage. See [AWS for GenAI](../26-aws/README.md).

## EC2

EC2 offers virtual machines, useful for custom serving or specialized infrastructure. See [AWS for GenAI](../26-aws/README.md).

## ECS and EKS

ECS runs containers with managed orchestration; EKS runs managed Kubernetes control planes. See [AWS for GenAI](../26-aws/README.md).

## Lambda

Lambda suits bounded event processing and lightweight endpoints when its runtime and resource constraints fit. See [AWS for GenAI](../26-aws/README.md).

## RDS

Use RDS for relational metadata, ACLs, jobs, and authoritative business records. See [AWS for GenAI](../26-aws/README.md).

## ElastiCache

Managed caching can provide Redis-compatible infrastructure for scoped caches, quotas, and transient state. See [AWS for GenAI](../26-aws/README.md).

## CloudWatch

Collect logs, metrics, and alarms. See [AWS for GenAI](../26-aws/README.md).

## IAM and Secrets Manager

IAM grants AWS permissions to identities. See [AWS for GenAI](../26-aws/README.md).

## API Gateway

A gateway can manage entrypoints, authentication integration, throttling, and routing. See [AWS for GenAI](../26-aws/README.md).

## Bedrock and architecture

An AWS RAG design can use S3, an ingestion queue, ECS workers, RDS metadata, a search service, an API layer, and Bedrock inference. See [AWS for GenAI](../26-aws/README.md).

## SQL fundamentals

Understand SELECT, WHERE, JOIN, GROUP BY, HAVING, ORDER BY, indexes, transactions, and query plans. See [Databases and GenAI](../27-database/README.md).

## PostgreSQL and MySQL

Both are relational databases with transactions and query planning, but dialects, extensions, and date semantics differ. See [Databases and GenAI](../27-database/README.md).

## Redis

Redis is useful for caches, counters, queues in suitable designs, and session data. See [Databases and GenAI](../27-database/README.md).

## Text-to-SQL

Translate a question into a constrained logical plan or SQL proposal using authorized schema information. See [Databases and GenAI](../27-database/README.md).

## SQL agents

Agents may inspect schema and repair invalid queries, but must remain bounded. See [Databases and GenAI](../27-database/README.md).

## Injection prevention

Use parameterized values and whitelist identifiers or structured operations. See [Databases and GenAI](../27-database/README.md).

## Aggregations and semantics

For customers spending more than ₹1 lakh in six months, define currency, refund treatment, paid status, timezone, and rolling-month boundaries. See [Databases and GenAI](../27-database/README.md).

## Metadata filtering

Keep tenant, ACL, version, and document state as structured data. See [Databases and GenAI](../27-database/README.md).

## Relational plus vector search

Use SQL for exact eligibility and vectors for content relevance. See [Databases and GenAI](../27-database/README.md).

## Testing and audit

Test empty results, missing joins, boundary dates, canceled orders, multi-currency data, and cross-tenant attempts. See [Databases and GenAI](../27-database/README.md).

## Irrelevant RAG results

Symptom: semantically similar but useless context. See [Real-World Debugging](../28-debugging/README.md).

## Embedding failures

Symptom: empty vectors, dimension errors, or ingestion stalls. See [Real-World Debugging](../28-debugging/README.md).

## Slow vector search

Inspect filter selectivity, payload indexes, candidate count, ANN settings, concurrent ingestion, and resource saturation. See [Real-World Debugging](../28-debugging/README.md).

## Hallucinated answers and citations

Trace final evidence, packing, source versions, unsupported claims, and citation mapping. See [Real-World Debugging](../28-debugging/README.md).

## Token and latency spikes

Compare prompt versions, history trimming, chunk count, output length, retries, and tool loops. See [Real-World Debugging](../28-debugging/README.md).

## Infinite loops and invalid tools

Inspect step state, repeated tool fingerprints, validation errors, and routing. See [Real-World Debugging](../28-debugging/README.md).

## Dangerous database queries

Inspect proposed plan and verify no privileged execution happened. See [Real-World Debugging](../28-debugging/README.md).

## Injection and memory errors

Inspect source trust, authorized memory writes, provenance, and retrieved scope. See [Real-World Debugging](../28-debugging/README.md).

## Provider outage

Inspect error type, provider status, network path, and quotas. See [Real-World Debugging](../28-debugging/README.md).

## Streaming stops

Inspect disconnects, proxy buffering, timeouts, generator exceptions, and incomplete final events. See [Real-World Debugging](../28-debugging/README.md).

## Python exercises

Implement deduplication by stable ID, bounded batches, a generator, and a context manager. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## API exercises

Validate request fields, classify errors, and keep authorization out of user input. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## Async exercises

Write bounded parallel calls with cancellation, timeouts, and per-record results. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## Embedding and similarity

Implement cosine, normalization, and top-k search. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## Chunking exercises

Implement overlapping windows with 0 ≤ overlap < size and termination guarantees. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## Retrieval and hybrid

Implement ranked retrieval with tenant filtering and reciprocal rank fusion. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## RAG exercises

Compose ingestion, retrieval, answer generation, and citations with a fake model first. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## Tools and agents

Build a registry with typed arguments, permissions, timeouts, and bounded execution. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## Evaluation exercises

Compute precision, recall, MRR, and Recall@k with defined edge behavior. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## Difficulty progression

Easy tasks cover metrics and data structures; medium covers chunking and retrieval; hard covers concurrency and workflow state; production tasks cover lifecycle, authorization, outages, and evidence. See [GenAI Coding Interviews](../29-coding-interview/README.md).

## Production-style RAG

Build versioned ingestion, authorized retrieval, source-linked answers, and an evaluation suite. See [Project-Based Interview Preparation](../30-projects/README.md).

## Customer support agent

Use current policy evidence, ticket lookup, escalation, and approval for consequential actions. See [Project-Based Interview Preparation](../30-projects/README.md).

## Research agent

Collect bounded sources, preserve provenance, summarize claims, and verify support. See [Project-Based Interview Preparation](../30-projects/README.md).

## SQL agent

Translate questions into constrained plans and read-only queries. See [Project-Based Interview Preparation](../30-projects/README.md).

## Document intelligence

Extract fields and source spans from varied document layouts. See [Project-Based Interview Preparation](../30-projects/README.md).

## AI question bank

Generate questions from approved educational content and validate answer support, difficulty, duplication, and coverage. See [Project-Based Interview Preparation](../30-projects/README.md).

## Evaluation platform

Store versioned cases, run configurations, per-case metrics, human judgments, and comparisons. See [Project-Based Interview Preparation](../30-projects/README.md).

## Multi-agent research

Divide collection, synthesis, and checking with explicit contracts and budgets. See [Project-Based Interview Preparation](../30-projects/README.md).

## Enterprise knowledge assistant

Combine identity, ACLs, source lifecycle, retrieval, optional tools, observability, and deployment. See [Project-Based Interview Preparation](../30-projects/README.md).

## Cost optimization router

Build configuration-driven routes with capability checks and task quality thresholds. See [Project-Based Interview Preparation](../30-projects/README.md).
