# AI Engineering Journey

> Building artificial intelligence from first principles.

This repository documents my journey toward becoming an AI Engineer by understanding how modern AI systems work internally rather than treating frameworks as magic.

The goal is not to memorize APIs or jump directly to high-level libraries. Important ideas are first understood conceptually, connected to the mathematics, implemented manually where practical, tested, and only then mapped to tools such as NumPy, PyTorch, and modern LLM frameworks.

---

## Learning Philosophy

The core principle of this repository is:

> **Understand before using.**

For every important topic, I try to answer:

- Why does this concept exist?
- What problem does it solve?
- What does the mathematics actually mean?
- How would I implement a simple version myself?
- How does the concept behave in code?
- How does it connect to the rest of an AI system?
- What does a framework automate for me later?

The aim is to build engineering intuition, not just collect syntax.

---

## Repository Structure

```text
Research-Engineer/
│
├── 01_Models/
│   ├── Model_Learning.md
│   ├── Exercises/
│   └── Notes/
│
├── 02_Tokenizer/
│   ├── Tokenizer.md
│   ├── Exercises/
│   └── Notes/
│
├── 03_Math/
│   ├── Math.md
│   └── Notes/
│
├── 04_Tensors_and_Data/
│   └── Tensors_and_Data.md
│
├── 05_Progress/
│   ├── MASTER_ROADMAP.md
│   ├── CURRENT_STATUS.md
│   └── DEPENDENCIES.md
│
├── 06_Concepts/
│   └── concept notes such as Gradient Descent.md
│
├── 08_Resources/
│
├── AI Engineering Home.md
├── README.md
└── .gitignore
```

### What each area is for

- **Subject curriculum files** describe what needs to be learned in each active track.
- **Notes/** contain chronological study notes and explanations from individual learning days.
- **Exercises/** contain implementations written to understand concepts through code.
- **06_Concepts/** contains durable notes representing my current understanding of individual ideas.
- **05_Progress/** tracks the complete roadmap, current position, and prerequisites between topics.
- **AI Engineering Home.md** acts as the main navigation page when the repository is opened as an Obsidian vault.
- **08_Resources/** contains supporting references rather than my own learning notes.

---

## Current Active Learning Tracks

The journey is currently split into four parallel foundation tracks.

### 1. Model Learning

Current foundation completed:

- model, input, output, target, and parameter intuition
- prediction, error, squared loss, and mean loss
- learning rate
- basic derivative and gradient intuition
- gradient sign and magnitude
- gradient descent from scratch
- NumPy arrays across multiple training samples
- Mean Squared Error intuition
- batch gradient across multiple samples
- iterative parameter updates and convergence toward the correct weight

Current transition:

```text
single learned weight
→ multiple inputs
→ multiple weights
→ gradient vector
→ chain rule
→ backpropagation
```

See: [01_Models/Model_Learning.md](01_Models/Model_Learning.md)

---

### 2. Tokenization

Current foundation completed:

- whitespace/word-level tokenization
- vocabulary construction
- token IDs
- encoding and decoding
- reverse vocabulary
- limitations of whole-word tokenization
- subword-tokenization motivation
- simplified character-starting BPE
- adjacent-pair frequency counting
- repeated BPE merge rounds
- ordered merge-rule storage
- subword vocabulary and token IDs

Current transition:

```text
trained BPE rules
→ unseen text
→ apply stored merges in order
→ reusable subword encoder
→ robust decoding / boundaries
→ byte-level concepts
```

See: [02_Tokenizer/Tokenizer.md](02_Tokenizer/Tokenizer.md)

---

### 3. Math for AI

Math is being learned only as deeply as needed to understand the AI systems being built.

Topics already studied include foundations around:

- variables and expressions
- equations and relationships
- functions and function inputs/outputs
- graphs and coordinates
- change and delta
- slope and rate of change
- intercepts
- the relationship between weight, bias, and the linear model `z = wx + b`
- basic derivative and gradient intuition encountered through Model Learning

Near-term direction:

```text
functions and slope
→ derivatives
→ vectors
→ dot product
→ matrices
→ partial derivatives
→ chain rule
```

See: [03_Math/Math.md](03_Math/Math.md)

---

### 4. Tensors & Data

Some tensor concepts have already appeared indirectly through NumPy-based model exercises, including:

- Python lists
- `np.array`
- vectorized arithmetic
- element-wise operations
- `np.mean`
- operating on multiple training samples together

The systematic tensor track is now beginning with:

```text
Python list vs NumPy array
→ scalar
→ vector
→ matrix
→ tensor
→ dimensions
→ shape
→ axis
→ broadcasting
→ dot product
→ matrix multiplication
→ batches
```

See: [04_Tensors_and_Data/Tensors_and_Data.md](04_Tensors_and_Data/Tensors_and_Data.md)

---

## Current Milestone

The current goal is to bring the four foundation tracks to their first convergence point.

```text
Model Learning
    multiple weights
          │
          ├─────────────┐
                        │
Math                    │
    vectors + dot       ├──→ first neuron
                        │
Tensors & Data          │
    vectors + matrices  │
    + shape reasoning ──┘

Tokenizer
    reusable BPE encoder
```

Once vectors, multiple weights, dot products, and basic tensor shape reasoning are comfortable, the next major block will be **Neural Networks**.

---

## Progress and Dependency Tracking

The detailed roadmap is deliberately separated from this README so that progress can evolve without turning this page into a giant checklist.

- [Master Roadmap](05_Progress/MASTER_ROADMAP.md) — the complete long-term AI engineering path
- [Current Status](05_Progress/CURRENT_STATUS.md) — what is completed, active, and next
- [Dependencies](05_Progress/DEPENDENCIES.md) — which concepts unlock later topics

The broader journey eventually progresses through:

```text
Foundations
→ Neural Networks
→ PyTorch
→ Embeddings
→ Transformers
→ Language Models
→ GPT from scratch
→ Training & Evaluation
→ Modern LLM Engineering
→ Inference & Deployment
→ Systems & Performance
```

---

## Knowledge System and Obsidian

This repository also acts as an Obsidian knowledge base.

The main navigation entry is:

[AI Engineering Home.md](AI%20Engineering%20Home.md)

The learning material is intentionally separated into three complementary forms:

```text
Daily Notes
= what I learned during a study session

Concept Notes
= my current durable understanding of one idea

Exercises
= code proving that I can implement and experiment with the idea
```

This lets the repository function both as a chronological learning journal and as an interconnected long-term reference.

---

## Learning Workflow

A typical study session follows this process:

1. Understand the problem a concept is solving.
2. Build an intuitive mental model.
3. Connect the intuition to the mathematics.
4. Design the algorithm or process.
5. Write pseudocode where useful.
6. Implement the concept manually.
7. Test and experiment with the implementation.
8. Investigate mistakes and confusing behavior.
9. Write the understanding in my own words.
10. Update progress only after the concept is genuinely understood.

---

## Rules I Follow

1. Build important concepts from scratch before relying on high-level abstractions.
2. Prefer understanding over memorization.
3. Write learning notes in my own words.
4. Keep useful experiments, including failed ones.
5. Use AI as a mentor and debugging partner rather than as a substitute for thinking.
6. Every coding exercise should exist to teach or test a concept.
7. Connect mathematics, code, and engineering rather than learning them as isolated subjects.
8. Frameworks should eventually feel like automation of processes I already understand.

---

## Long-Term Goal

The long-term objective is to understand and build the major pieces of modern AI systems from first principles, including:

- tokenizers
- embeddings
- gradient-based learning
- neural networks
- backpropagation
- tensor computation
- attention and self-attention
- transformer blocks
- GPT-style language models
- model training and evaluation
- fine-tuning and RAG
- inference and deployment
- AI systems engineering

The desired end state is not merely being able to call a model API. It is being able to reason about what is happening underneath it.

---

## Educational Scope

This repository is intentionally educational.

Early implementations prioritize clarity, experimentation, and conceptual understanding over production efficiency. More optimized libraries and engineering techniques are introduced only after the underlying mechanisms are understood.