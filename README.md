# Engineering Journey

> Building Artificial Intelligence from first principles.

This repository documents my journey toward becoming an AI Engineer.

The goal is **not** to memorize APIs or rely on machine learning libraries. Instead, the goal is to understand every important concept by building it from scratch.

Everything in this repository is written as a learning artifact, starting from simple mathematical models and progressing toward neural networks, transformers, and eventually large language models.

---

# Learning Philosophy

This repository follows one principle:

> **Understand before using.**

Rather than importing libraries and calling `fit()` or `train()`, every important idea is first derived, discussed, implemented, and tested manually.

For every topic I learn, I try to answer:

- Why does this exist?
- What problem does it solve?
- How would I build it myself?
- How is it implemented mathematically?
- How is it implemented in code?

---

# Repository Structure

```
Engineering Journey/
│
├── Exercises/
│   ├── 001_learning_model.py
│   ├── 002_first_learner.py
│   └── ...
│
├── Experiments/
│   ├── embedding_visualization.py
│   ├── optimizer_comparison.py
│   └── ...
│
├── Notes/
│   ├── day001.md
│   ├── day002.md
│   ├── day003.md
│   └── ...
│
├── Projects/
│   ├── tokenizer/
│   ├── neural_network/
│   ├── transformer/
│   └── ...
│
├── Resources/
│
├── ROADMAP.md
│
└── README.md
```

---

# Progress

## Foundations

- [x] What is Machine Learning?
- [x] What is a Model?
- [x] Learnable Parameters
- [x] Error
- [x] Loss
- [x] Learning Rate
- [x] First Self-Learning Model
- [ ] Derivatives
- [ ] Gradients
- [ ] Gradient Descent
- [ ] Chain Rule
- [ ] Backpropagation

## Linear Algebra

- [ ] Scalars
- [ ] Vectors
- [ ] Matrices
- [ ] Matrix Multiplication
- [ ] Dot Product
- [ ] Norms
- [ ] Eigenvalues & Eigenvectors

## Probability & Statistics

- [ ] Probability
- [ ] Distributions
- [ ] Mean & Variance
- [ ] Bayes' Rule

## Neural Networks

- [ ] Artificial Neuron
- [ ] Activation Functions
- [ ] Dense Layers
- [ ] Feedforward Networks
- [ ] Backpropagation
- [ ] Optimizers

## Natural Language Processing

- [ ] Tokenization
- [ ] Vocabulary
- [ ] Embeddings
- [ ] Positional Encoding

## Transformers

- [ ] Attention
- [ ] Self-Attention
- [ ] Multi-Head Attention
- [ ] Transformer Block
- [ ] Decoder Architecture

## Large Language Models

- [ ] GPT
- [ ] Training
- [ ] Fine-Tuning
- [ ] RAG
- [ ] Tool Calling
- [ ] Agents

---

# Current Milestone

Current focus:

Building a machine learning model that can learn from its own mistakes.

Completed:

- Built a mathematical model.
- Implemented prediction.
- Calculated error.
- Calculated loss.
- Built a simple feedback loop that updates its own parameter.

Next:

Learn how mathematics determines the correct update direction using derivatives and gradients.

---

# Rules I Follow

1. Build every important concept from scratch before using libraries.
2. Prefer understanding over memorization.
3. Write notes in my own words.
4. Keep every experiment, even failed ones.
5. Use AI as a mentor—not as someone who solves every problem.
6. Every coding exercise should teach a concept.
7. Every day should produce at least one tangible artifact.

---

# Learning Workflow

Every study session follows the same process:

1. Understand the problem.
2. Discuss the theory.
3. Design the algorithm.
4. Write pseudocode.
5. Implement it.
6. Test it.
7. Reflect on what was learned.
8. Document the day's insights.

---

# Long-Term Goal

By the end of this journey, I aim to understand and implement:

- Tokenizers
- Embeddings
- Gradient Descent
- Neural Networks
- Backpropagation
- Attention
- Transformers
- GPT-style Language Models

from first principles.

---

# Disclaimer

This repository is intentionally educational.

Many implementations prioritize clarity and understanding over efficiency or production-ready code.

The objective is to understand how modern AI systems work internally before relying on high-level frameworks.