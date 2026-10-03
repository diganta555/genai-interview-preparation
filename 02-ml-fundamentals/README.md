# 02: Machine Learning Fundamentals

[Previous module](../01-python/README.md) · [Repository home](../README.md) · [Next module](../03-deep-learning/README.md)

---

# 1. Supervised Learning

## What is Supervised Learning?

Supervised learning is a type of machine learning where we train a model using **input data together with the correct answer**, called a label.

The model studies many examples and learns a relationship between the input and output.

The basic idea is:

```text
Input + Correct Answer
        ↓
      Model
        ↓
Learn the Pattern
        ↓
New Input
        ↓
Prediction
```

For example, imagine we want to build a system that automatically categorizes customer-support messages.

We might have training data like:

```text
Input                              Label

"My payment failed"              Payment Issue

"I cannot login"                 Login Issue

"Where is my order?"             Delivery Issue

"I want to cancel my order"      Cancellation
```

The model sees these examples and learns patterns.

Later, if a new customer sends:

```text
"My card payment was declined"
```

the model might predict:

```text
Payment Issue
```

The important point is that during training, we already know the correct answer.

---

## Why Do We Need Supervised Learning?

Many real-world engineering problems require prediction.

For example:

```text
Email
   ↓
Spam / Not Spam
```

```text
Transaction
   ↓
Fraud / Not Fraud
```

```text
Customer Query
   ↓
Billing / Technical / Sales
```

```text
LLM Request
   ↓
Simple / Medium / Complex
```

```text
User Request
   ↓
Estimated API Cost
```

These are all prediction problems.

---

# Classification

Classification means the model predicts a **category**.

For example:

```text
Input:
"My password doesn't work"

Prediction:
Login Problem
```

The output is not an arbitrary number. It belongs to a predefined class.

Common classification problems include:

```text
Spam / Not Spam

Fraud / Not Fraud

Positive / Negative

Safe / Prompt Injection

Billing / Technical / Sales
```

---

## Binary Classification

Binary classification has two possible classes.

Example:

```text
Spam
Not Spam
```

or:

```text
Fraud
Not Fraud
```

The model may internally produce a probability:

```text
Fraud probability = 0.91
```

Then we apply a threshold.

For example:

```text
if probability >= 0.5:
    Fraud
else:
    Not Fraud
```

However, the threshold does not always have to be `0.5`.

The correct threshold depends on the cost of false positives and false negatives.

This becomes very important in production systems.

---

# Multiclass Classification

Multiclass classification means there are more than two possible classes.

For example:

```text
Billing
Technical
Sales
Account
Delivery
Refund
```

Suppose the model receives:

```text
"I haven't received my refund."
```

It might output:

```text
Refund = 0.87
Billing = 0.08
Account = 0.03
Technical = 0.02
```

The final prediction would be:

```text
Refund
```

---

# Regression

Regression is different from classification.

Instead of predicting a category, regression predicts a **continuous numerical value**.

For example:

```text
Input:
Number of tokens
Model
Request complexity

        ↓

Predicted API cost
```

The output could be:

```text
$0.024
```

Other regression examples include:

```text
House price
Delivery time
Temperature
API latency
Monthly revenue
Estimated inference cost
```

---

# Classification vs Regression

| Problem        | Output   | Example          |
| -------------- | -------- | ---------------- |
| Classification | Category | Spam / Not Spam  |
| Regression     | Number   | API cost = $0.04 |

A simple way to remember:

```text
Classification
→ "Which category?"

Regression
→ "How much?"
```

---

# Real-World GenAI Example

Imagine we are building an **LLM Cost Router**.

We have three models:

```text
Small Model
Medium Model
Large Model
```

The large model is more expensive.

We don't want every request to use it.

So we create a classifier that predicts the complexity of the request.

Example:

```text
User:
"What is the capital of France?"

        ↓

Classifier

        ↓

Simple

        ↓

Small Model
```

Another request:

```text
User:
"Design a distributed multi-agent architecture
with fault tolerance and explain the trade-offs."

        ↓

Classifier

        ↓

Complex

        ↓

Large Model
```

The classifier itself becomes a supervised-learning problem if we have labeled examples such as:

```text
Question                              Label

"What is Python?"                    Simple

"Explain REST API"                   Simple

"Design distributed system..."       Complex
```

---

# How Would You Build a Supervised Learning System?

A typical process is:

```text
1. Define the business problem
          ↓
2. Collect data
          ↓
3. Label the data
          ↓
4. Clean the data
          ↓
5. Create features
          ↓
6. Split the dataset
          ↓
7. Train baseline model
          ↓
8. Evaluate on validation data
          ↓
9. Tune the model
          ↓
10. Evaluate on untouched test data
          ↓
11. Deploy
          ↓
12. Monitor production performance
```

The important part is that the job is not finished when the model trains successfully.

You must also evaluate:

```text
Quality
Latency
Cost
Failure cases
Data drift
Security
```

---

# What is a Baseline?

A baseline is a simple solution that gives us a reference point.

For example, before building an ML classifier, we could use:

```python
if "refund" in query.lower():
    category = "refund"
```

This is not a sophisticated ML system.

But it gives us a baseline.

Suppose:

```text
Rule-based baseline = 82%

ML model = 89%
```

Now we have evidence that the ML model improves the result.

Without a baseline, it is difficult to know whether the additional complexity is actually useful.

---

# Why Should We Start With a Simple Model?

Because complexity has a cost.

A complicated model can introduce:

```text
More computation
More latency
More maintenance
More dependencies
Harder debugging
Higher infrastructure cost
```

If a simple model achieves the required quality, there may be no engineering reason to replace it with a much more complicated system.

A good engineer asks:

> "What is the simplest solution that satisfies the requirement?"

---

# Important Interview Question

## What is the difference between supervised and unsupervised learning?

### Interview-Ready Answer

> "The main difference is whether we have labeled target values. In supervised learning, the training data contains inputs and expected outputs, and the model learns to predict the output for new inputs. In unsupervised learning, there are no target labels, so the algorithm tries to discover structure or patterns in the data itself. For example, classifying support tickets as billing or technical is supervised learning, while grouping unlabeled support tickets into similar clusters is unsupervised learning."

---

# Interview Follow-Up

## Can clustering be used to create labels?

Yes, but we should be careful.

Clustering can help discover groups:

```text
Cluster 1
Cluster 2
Cluster 3
```

Humans can inspect those groups and assign meanings:

```text
Cluster 1 → Payment
Cluster 2 → Login
Cluster 3 → Delivery
```

The clustering algorithm itself does not know that these names are correct.

This is why human validation is important.

---

# Common Interview Mistake

Bad answer:

> "Supervised learning is when the model learns from data."

This is incomplete.

A stronger answer says:

> "Supervised learning learns a mapping from labeled input-output examples and is evaluated on unseen examples to determine whether it generalizes."

Then give an example.

---

# Senior-Level Consideration

A senior engineer should think beyond:

```text
Can I train the model?
```

They should ask:

```text
Is the data representative?

Are the labels reliable?

Is there leakage?

What happens when the model is wrong?

Which errors are expensive?

What metric represents the business requirement?

Does the model generalize?

How will I monitor drift?

What happens when the model or dependency changes?
```

That is the difference between knowing the ML definition and designing an ML system.

---

# 2. Unsupervised Learning and Clustering

## What is Unsupervised Learning?

Unsupervised learning works with data where we don't have a predefined target label.

Instead of telling the model:

```text
This is Payment
This is Login
This is Delivery
```

we give it data and ask it to discover structure.

For example:

```text
100,000 support tickets
        ↓
Embedding / Features
        ↓
Clustering
        ↓
Similar groups
```

---

## Real-World Example

Suppose a company has 1 million customer queries but nobody has categorized them.

Some examples may be:

```text
"My card isn't working"

"Payment failed"

"Transaction declined"

"I forgot my password"

"I can't login"

"Reset my password"
```

A clustering algorithm may identify groups of similar examples.

Humans can then inspect them:

```text
Cluster A → Payment
Cluster B → Authentication
```

This can help create an initial taxonomy.

---

# Important Limitation

A cluster does not automatically have business meaning.

For example:

```text
Cluster 0
Cluster 1
Cluster 2
```

does not mean:

```text
0 = Low Priority
1 = Medium Priority
2 = High Priority
```

The cluster number is simply an identifier.

---

# Interview-Ready Answer

> "Unsupervised learning works without predefined target labels. It is useful for discovering structure in data, such as grouping similar customer tickets. However, the resulting clusters don't automatically represent business concepts, so I would inspect representative examples and validate the clusters before using them for business decisions."

---

# 3. Feature Engineering

## What is Feature Engineering?

Feature engineering means transforming raw data into information that is useful for a model.

Suppose the raw input is:

```text
"Why is my payment failing?"
```

We can derive:

```text
Query length = 28
Language = English
Domain = Payment
Contains error keyword = True
```

These are features.

---

## Why Is It Important?

A model can only learn from the information we provide.

If the useful signal isn't represented properly, even a powerful model may perform poorly.

---

## Real-World GenAI Example

For an LLM routing system:

```text
Query
 ↓
Features

Token count
Query length
Language
Code present?
Domain
Complexity indicators
Retrieval score
Retrieval score gap
Historical error rate
 ↓
Router
 ↓
LLM selection
```

---

# Data Leakage in Feature Engineering

This is an important interview topic.

Suppose we're predicting whether an LLM response will be successful.

At prediction time we know:

```text
User query
User type
Language
Retrieved documents
```

But we don't know:

```text
Final answer quality
User satisfaction after response
Human evaluation score
```

Using these future values as features would create leakage.

The model would effectively receive information from the future.

---

# Interview-Ready Answer

> "Feature engineering is the process of creating useful representations from raw data for a machine learning model. I also need to ensure that features are available at prediction time. Otherwise, I can introduce data leakage and get unrealistically high evaluation results."

---

# 4. Overfitting and Underfitting

## What is Overfitting?

Overfitting happens when the model learns the training data too specifically instead of learning patterns that generalize.

Example:

```text
Training accuracy = 99%
Validation accuracy = 70%
```

The large gap suggests the model is not generalizing well.

---

## What is Underfitting?

Underfitting means the model hasn't learned enough useful structure.

Example:

```text
Training accuracy = 65%
Validation accuracy = 63%
```

The model performs poorly even on the training data.

---

# Real-World GenAI Example

Suppose you create an evaluation dataset with only 50 questions.

You repeatedly modify your prompt until it gets:

```text
48 / 50 correct
```

Then you test it on 1,000 new questions:

```text
68% correct
```

Your development process may have overfit the small evaluation set.

This is why an untouched test set matters.

---

# Interview-Ready Answer

> "Overfitting occurs when a model learns training-specific patterns and doesn't generalize well to unseen data. I would compare training and validation performance to identify the generalization gap. Depending on the cause, I might use more representative data, regularization, a simpler model, early stopping, or a better validation strategy."

---

# 5. Train, Validation and Test

## Why Do We Need Three Sets?

Because we have three different jobs.

### Training

Learn parameters.

```text
Data → Model
```

### Validation

Make development decisions.

```text
Model A → 90%
Model B → 94%
Model C → 91%

Choose Model B
```

### Test

Estimate final generalization.

```text
Final Model
     ↓
Untouched Test Set
     ↓
Final Evaluation
```

---

# Important Interview Question

## Why can't I keep using the test set?

Because every time you change the model based on test performance, you're indirectly optimizing against the test set.

Eventually:

```text
Test performance
        ↓
Model changes
        ↓
Test performance
        ↓
More model changes
```

The test set is no longer independent.

---

# RAG Example

Suppose you have 100 PDFs.

Instead of randomly splitting chunks:

```text
PDF 1 chunks → Train + Test
```

consider splitting at the document or other meaningful independent unit:

```text
80 PDFs → Development
10 PDFs → Validation
10 PDFs → Test
```

The exact split should depend on what you want the test to represent.

---

# Interview-Ready Answer

> "Training is used to fit the model, validation is used for model and configuration decisions, and the test set is reserved for estimating final generalization. The split strategy should reflect the independence assumptions of the problem. For correlated records, such as chunks from the same document, a random row-level split can cause leakage."

---

# 6. Cross-Validation

## What Is Cross-Validation?

Cross-validation evaluates a model over multiple train-validation splits.

For example:

```text
Fold 1 → 91%
Fold 2 → 93%
Fold 3 → 90%
Fold 4 → 94%
Fold 5 → 92%
```

We can calculate:

```text
Average ≈ 92%
```

But we should also consider the variation between folds.

---

# Why Is This Useful?

Suppose one random split gives:

```text
95%
```

You might think the model is excellent.

But another split might give:

```text
82%
```

Cross-validation helps reveal whether the performance is stable.

---

# Group Cross-Validation

Suppose each user generates multiple records:

```text
User A
 ├── Query 1
 ├── Query 2
 └── Query 3
```

If you randomly split rows, User A could appear in both training and validation.

That may make the evaluation overly optimistic.

Instead, group by user:

```text
User A → Fold 1
User B → Fold 2
User C → Fold 3
```

---

# Time-Based Validation

For systems that predict the future:

```text
January → Training
February → Validation
March → Test
```

This better represents deployment where we train on the past and predict the future.

---

# Interview-Ready Answer

> "Cross-validation repeatedly evaluates a model across different folds to estimate performance variability. I would use grouped cross-validation when related records must remain together and time-based validation when deployment involves predicting future data. However, I would still keep a final untouched benchmark for the final evaluation."

---

# 7. Precision, Recall and F1

These are among the most frequently discussed classification metrics.

---

## Precision

Precision answers:

> "When the model predicts positive, how often is it correct?"

Formula:

```text
Precision = TP / (TP + FP)
```

Suppose:

```text
Model predicts 100 attacks

80 → Actually attacks
20 → Actually legitimate
```

Then:

```text
Precision = 80 / 100
          = 80%
```

---

# Recall

Recall answers:

> "Of all the actual positive cases, how many did the model detect?"

Formula:

```text
Recall = TP / (TP + FN)
```

Suppose:

```text
Actual attacks = 100
Detected = 80
Missed = 20
```

Then:

```text
Recall = 80 / 100
       = 80%
```

---

# F1 Score

F1 combines precision and recall.

```text
F1 = 2 × Precision × Recall
     -----------------------
      Precision + Recall
```

F1 is useful when we want a balance between precision and recall.

---

# Real-World Prompt Injection Example

Suppose:

```text
10,000 requests
100 actual attacks
```

Your model detects:

```text
90 attacks
```

but also incorrectly blocks:

```text
300 legitimate requests
```

Then:

```text
TP = 90
FN = 10
FP = 300
```

Precision:

```text
90 / (90 + 300)
≈ 23.1%
```

Recall:

```text
90 / (90 + 10)
= 90%
```

This tells us something important:

> The model catches most attacks, but it blocks many legitimate requests.

That is much more informative than saying:

```text
"Accuracy = 96%"
```

---

# Interview Question

## Which is more important: precision or recall?

### Strong Answer

> "It depends on the cost of the errors. If missing a positive case is extremely costly, I would prioritize recall. If false positives are very expensive, I would prioritize precision. I would choose the threshold based on the actual business or safety requirements rather than assuming 0.5 is always correct."

---

# 8. ROC-AUC and Imbalanced Data

## What Is Class Imbalance?

Suppose:

```text
10,000 requests

9,900 → Normal
100 → Attack
```

The classes are highly imbalanced.

---

# Why Is Accuracy Dangerous?

A model that predicts:

```text
Everything = Normal
```

gets:

```text
99% accuracy
```

But:

```text
Attack recall = 0%
```

Therefore, the model is useless for attack detection despite high accuracy.

---

# ROC-AUC

ROC-AUC measures the model's ability to rank positive examples above negative examples across thresholds using:

```text
True Positive Rate
False Positive Rate
```

It is useful as a threshold-independent ranking metric.

But for highly rare positives, I would also examine the precision-recall curve because it gives a more direct view of positive-class performance.

---

# Interview-Ready Answer

> "For imbalanced classification, accuracy can hide poor minority-class performance. I would inspect the confusion matrix and metrics such as precision, recall, F1, ROC-AUC, and especially the precision-recall curve when positives are rare. I would also evaluate important slices rather than relying on one aggregate metric."

---

# 9. Embeddings

## What Is an Embedding?

An embedding is a numerical representation of an item, such as text.

For example:

```text
"I like Python"
       ↓
Embedding Model
       ↓
[0.21, -0.43, 0.72, 0.18, ...]
```

The vector is designed so that useful relationships between items can be represented geometrically.

---

# Why Are Embeddings Important in GenAI?

Embeddings are heavily used in:

```text
Semantic Search
RAG
Document Retrieval
Recommendation
Clustering
Classification
Duplicate Detection
```

---

# RAG Example

Suppose we have:

```text
Document A:
"Python is a programming language."

Document B:
"India is located in South Asia."

Document C:
"Machine learning learns patterns from data."
```

We convert documents into embeddings:

```text
Document
   ↓
Embedding Model
   ↓
Vector
   ↓
Vector Database
```

User asks:

```text
"What is Python?"
```

The query is embedded:

```text
Question
   ↓
Query Embedding
```

Then we search for similar vectors.

```text
Query Vector
      ↓
Vector Search
      ↓
Document A
```

The retrieved document is passed to the LLM.

---

# Important Interview Question

## Does an embedding prove that two statements are factually related?

No.

An embedding provides a similarity signal.

It doesn't guarantee:

```text
Truth
Correctness
Authorization
Freshness
```

For example, an incorrect document can still be semantically similar to the query.

---

# Interview-Ready Answer

> "Embeddings convert data such as text into vector representations that capture useful semantic relationships. In RAG, we embed documents and queries and use vector similarity to retrieve relevant context. However, similarity is only a retrieval signal; it doesn't guarantee factual correctness, freshness, or authorization."

---

# 10. Dimensionality Reduction

## What Is Dimensionality?

Suppose an embedding has:

```text
768 numbers
```

We call this a 768-dimensional vector.

Working with high-dimensional data can be expensive and difficult to visualize.

Dimensionality reduction transforms:

```text
768 dimensions
      ↓
Lower-dimensional representation
```

---

# PCA

PCA stands for:

> Principal Component Analysis.

PCA finds directions in the data that capture large amounts of variance and represents the data using selected principal components.

For example:

```text
100 features
      ↓
PCA
      ↓
20 components
```

---

# Why Use PCA?

Possible reasons:

```text
Reduce dimensionality
Reduce storage
Reduce computation
Visualize data
Remove some redundant variation
```

But it is not automatically beneficial.

If reducing dimensions hurts the actual downstream task, then the compression is not useful.

---

# RAG Example

Suppose:

```text
Original embedding = 768 dimensions
```

You reduce it:

```text
768
 ↓
256
```

You then compare retrieval performance.

Before:

```text
Recall@10 = 94%
```

After:

```text
Recall@10 = 86%
```

You have reduced dimensionality but lost retrieval quality.

Therefore you need to evaluate the actual task, not just storage savings.

---

# Interview Question

## Why should PCA be fitted only on training data?

### Strong Answer

> "PCA learns a transformation from the data distribution. If I fit PCA using validation or test data, information from those datasets influences the transformation. That creates leakage. I should fit PCA on training data and then use the learned transformation for validation, test, and production."

---

# Complete Interview Scenario

## Scenario

You are building a RAG system for a company.

The system sometimes returns incorrect answers.

The interviewer asks:

> "How would you debug it?"

### Strong Answer

I would break the pipeline into stages:

```text
User Query
    ↓
Query Processing
    ↓
Embedding
    ↓
Retriever
    ↓
Retrieved Documents
    ↓
Prompt Construction
    ↓
LLM
    ↓
Answer
```

I would evaluate each stage separately.

### Step 1 — Check the Documents

Are the source documents:

```text
Correct?
Current?
Complete?
Accessible?
```

### Step 2 — Check Chunking

I would inspect:

```text
Chunk size
Chunk overlap
Document boundaries
Metadata
```

### Step 3 — Check Retrieval

I would measure:

```text
Recall@K
Precision@K
MRR
```

and manually inspect retrieved documents.

### Step 4 — Check Embeddings

I would verify:

```text
Embedding model
Embedding consistency
Query/document preprocessing
Vector index
Similarity metric
```

### Step 5 — Check Generation

If retrieval is correct but the final answer is wrong, I would investigate:

```text
Prompt
Context formatting
Context length
Model behavior
Instruction hierarchy
```

### Step 6 — Evaluate

I would maintain a representative held-out evaluation set and compare every change against a fixed baseline.

---

# Senior-Level Answer

> "I would avoid treating the RAG system as one black box. I would instrument the pipeline so that I can independently inspect query processing, retrieval, retrieved context, prompt construction, model output, and final evaluation. I would first determine whether the failure is retrieval-related or generation-related. For retrieval, I would measure metrics such as Recall@K and MRR and inspect failure slices. For generation, I would evaluate relevance and faithfulness against the retrieved context. I would then compare any change against a fixed held-out benchmark and monitor latency, token cost, and failure rates."

---

# Production Thinking

A production ML system is not just:

```text
Data → Model → Prediction
```

It is:

```text
                Data
                  ↓
              Features
                  ↓
                Model
                  ↓
             Evaluation
                  ↓
        ┌─────────┴─────────┐
        ↓                   ↓
     Quality              Cost
        ↓                   ↓
    Reliability          Latency
        ↓                   ↓
       Security
        ↓
      Monitoring
        ↓
      Rollback
```

---

# Final Interview Principle

When answering an ML interview question, don't stop after the definition.

Use this structure:

```text
1. Define the concept
        ↓
2. Explain why it matters
        ↓
3. Give a simple example
        ↓
4. Give a real-world GenAI example
        ↓
5. Explain how you would measure it
        ↓
6. Explain failure cases
        ↓
7. Explain production considerations
```

For example, don't simply say:

> "Recall is TP divided by TP plus FN."

Instead say:

> "Recall measures how many of the actual positive cases we successfully detect. For a prompt-injection detector, if there are 100 actual attacks and we detect 90, recall is 90%. Recall becomes particularly important when missing an attack is much more expensive than incorrectly flagging a legitimate request. However, increasing recall can reduce precision, so I would select the threshold using validation data based on the actual cost of both error types."

That is the level of explanation you should target in a **GenAI/ML engineering interview**.
