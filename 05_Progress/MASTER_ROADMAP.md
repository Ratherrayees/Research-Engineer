# AI Engineering Journey — Master Roadmap

> Goal: Build a deep, engineering-level understanding of AI systems from first principles, then connect that understanding to modern tools such as NumPy, PyTorch, neural networks, transformers, LLM training, inference, and deployment.

---

# How This Roadmap Works

The journey is divided into parallel learning tracks.

Current active tracks:

1. Model Learning
2. Tokenization
3. Math for AI
4. Tensors & Data

Later tracks unlock when their prerequisites are understood:

5. Neural Networks
6. PyTorch
7. Transformers
8. Training & Evaluation
9. LLM Engineering
10. Inference & Deployment
11. Systems & Performance
12. Projects

The purpose of parallel learning is to study related foundations independently and then connect them when they naturally meet.

---

# Phase 1 — Core Foundations

## 1. Model Learning

### Basic Model Concepts

* [x] What is a model?
* [x] Inputs
* [x] Outputs
* [x] Parameters
* [x] Weights
* [x] Prediction
* [x] Actual / target value
* [x] Error
* [x] Loss
* [x] Squared error
* [x] Mean loss
* [x] Mean Squared Error intuition
* [x] Learning rate
* [x] First learning model
* [x] Iterative parameter updates

### Gradient-Based Learning

* [x] Basic derivative intuition
* [x] Basic gradient intuition
* [x] Gradient sign
* [x] Gradient magnitude
* [x] Gradient descent intuition
* [x] Gradient descent implementation
* [x] Batch gradient from multiple observations
* [x] Mean gradient across a dataset
* [ ] Derivatives in depth
* [ ] Partial derivatives
* [ ] Multiple parameters
* [ ] Gradient vector
* [ ] Loss surface
* [ ] Local minima intuition
* [ ] Learning-rate behavior
* [ ] Convergence
* [ ] Divergence
* [ ] Chain rule
* [ ] Computational graphs
* [ ] Backpropagation
* [ ] Automatic differentiation intuition

### Optimization

* [ ] Batch Gradient Descent
* [ ] Stochastic Gradient Descent
* [ ] Mini-batch Gradient Descent
* [ ] Momentum
* [ ] RMSProp
* [ ] Adam
* [ ] Weight decay
* [ ] Gradient clipping
* [ ] Learning-rate schedules
* [ ] Optimization stability

---

# 2. Tokenization

## Tokenizer Fundamentals

* [x] What is a token?
* [x] What is a tokenizer?
* [x] Text → tokens
* [x] Vocabulary
* [x] Token IDs
* [x] Encoding
* [x] Decoding
* [x] Reverse vocabulary
* [x] Reconstructing text
* [x] Repeated tokens sharing IDs
* [x] Token IDs are identifiers, not meaning
* [x] Word-level tokenizer from scratch

## Word-Level Tokenizer Limitations

* [x] Punctuation creates separate tokens
* [x] Case sensitivity
* [x] Unknown-word problem
* [x] Vocabulary explosion
* [x] Word-level vs character-level tokenization
* [x] Why subword tokenization exists

## Subword Tokenization

* [x] Subword concept
* [x] Reusable text pieces
* [x] Vocabulary-size vs sequence-length trade-off
* [x] Basic BPE intuition
* [x] Character-level starting units
* [x] Pair frequency counting
* [x] Finding most frequent pair
* [x] Pair merging
* [x] Repeated merge rounds
* [x] Preserving word boundaries in simplified BPE
* [x] Saving BPE merge rules
* [x] Building BPE vocabulary
* [x] Encoding BPE pieces into IDs
* [ ] Apply trained merge rules to unseen words
* [ ] Apply trained tokenizer to unseen sentences
* [ ] Decode BPE token IDs
* [ ] Preserve exact word boundaries
* [ ] Handle whitespace explicitly
* [ ] Handle punctuation cleanly
* [ ] Unknown character handling

## Production Tokenization Concepts

* [ ] Byte-level tokenization
* [ ] Byte-level BPE
* [ ] Unicode
* [ ] UTF-8 intuition
* [ ] Special tokens
* [ ] BOS token
* [ ] EOS token
* [ ] PAD token
* [ ] UNK token
* [ ] MASK token
* [ ] Padding
* [ ] Truncation
* [ ] Attention masks
* [ ] Vocabulary size choices
* [ ] Tokenizer training corpus
* [ ] Token frequency
* [ ] BPE merge ranking
* [ ] WordPiece intuition
* [ ] Unigram tokenizer intuition
* [ ] Compare BPE vs WordPiece vs Unigram
* [ ] Hugging Face tokenizer basics
* [ ] Inspect a real LLM tokenizer
* [ ] Token-count differences across languages
* [ ] Tokenization of code
* [ ] Tokenization of numbers
* [ ] Tokenization and context-window efficiency

---

# 3. Math for AI

## Arithmetic Foundations

* [ ] Variables
* [ ] Constants
* [ ] Expressions
* [ ] Equations
* [ ] Functions
* [ ] Inputs and outputs of functions
* [ ] Order of operations
* [ ] Powers
* [ ] Roots
* [ ] Fractions
* [ ] Ratios
* [ ] Percentages

## Algebra

* [ ] Rearranging equations
* [ ] Solving simple equations
* [ ] Linear equations
* [ ] Slope
* [ ] Intercept
* [ ] Linear functions
* [ ] Polynomial intuition
* [ ] Exponents
* [ ] Logarithms

## Calculus

* [ ] Rate of change
* [ ] Slope of a curve
* [ ] Derivative intuition
* [ ] Derivative notation
* [ ] Derivative of simple functions
* [ ] Power rule intuition
* [ ] Partial derivatives
* [ ] Multivariable functions
* [ ] Gradient
* [ ] Gradient vector
* [ ] Chain rule
* [ ] Computational graph interpretation
* [ ] Derivatives in neural networks

## Linear Algebra

* [ ] Scalar
* [ ] Vector
* [ ] Vector components
* [ ] Vector magnitude intuition
* [ ] Vector addition
* [ ] Scalar multiplication
* [ ] Dot product
* [ ] Dot-product geometric intuition
* [ ] Matrix
* [ ] Rows and columns
* [ ] Matrix shape
* [ ] Matrix-vector multiplication
* [ ] Matrix-matrix multiplication
* [ ] Transpose
* [ ] Identity matrix
* [ ] Batch matrix multiplication
* [ ] Linear transformations
* [ ] Basis intuition
* [ ] High-dimensional spaces

## Probability & Statistics

* [ ] Mean
* [ ] Median
* [ ] Variance
* [ ] Standard deviation
* [ ] Probability
* [ ] Probability distributions
* [ ] Conditional probability
* [ ] Random variables
* [ ] Expected value
* [ ] Normal distribution
* [ ] Log probabilities
* [ ] Softmax intuition
* [ ] Cross-entropy intuition
* [ ] Entropy
* [ ] Sampling

## Optional Advanced Math

* [ ] Jacobian intuition
* [ ] Hessian intuition
* [ ] Eigenvalues intuition
* [ ] Eigenvectors intuition
* [ ] Singular Value Decomposition intuition
* [ ] Numerical stability
* [ ] Floating-point precision

---

# 4. Tensors & Data

## Python Numerical Foundations

* [x] Python lists
* [x] NumPy introduction
* [x] `np.array`
* [x] `np.mean`
* [ ] Python list vs NumPy array
* [ ] Vectorized operations
* [ ] NumPy dtypes
* [ ] NumPy indexing
* [ ] NumPy slicing

## Tensor Concepts

* [ ] Scalar
* [ ] Vector
* [ ] Matrix
* [ ] Tensor
* [ ] Rank / number of dimensions
* [ ] Shape
* [ ] Axis
* [ ] Size
* [ ] Dtype
* [ ] Tensor indexing
* [ ] Tensor slicing

## Tensor Operations

* [ ] Element-wise addition
* [ ] Element-wise subtraction
* [ ] Element-wise multiplication
* [ ] Element-wise division
* [ ] Sum
* [ ] Mean
* [ ] Min / max
* [ ] Reshape
* [ ] Flatten
* [ ] Transpose
* [ ] Concatenation
* [ ] Stacking
* [ ] Broadcasting
* [ ] Dot product
* [ ] Matrix multiplication

## Data Organization

* [ ] Sample
* [ ] Feature
* [ ] Target
* [ ] Dataset
* [ ] Batch
* [ ] Batch size
* [ ] Epoch
* [ ] Iteration / step
* [ ] Feature matrix
* [ ] Target vector
* [ ] Sequence data
* [ ] Variable-length sequences

## Dataset Preparation

* [ ] Training set
* [ ] Validation set
* [ ] Test set
* [ ] Data splitting
* [ ] Shuffling
* [ ] Batching
* [ ] Normalization
* [ ] Standardization
* [ ] Missing data
* [ ] Categorical data
* [ ] Data leakage
* [ ] Dataset bias
* [ ] Sampling

## AI Tensor Shapes

* [ ] Batch dimension
* [ ] Sequence dimension
* [ ] Feature dimension
* [ ] Embedding dimension
* [ ] Vocabulary dimension
* [ ] Hidden dimension
* [ ] Understanding `[batch, sequence, embedding]`
* [ ] Shape tracking through a model

---

# Phase 2 — Neural Networks

## 5. Neural Network Foundations

### First Neuron

* [ ] Biological analogy vs mathematical neuron
* [ ] Multiple inputs
* [ ] Multiple weights
* [ ] Bias
* [ ] Weighted sum
* [ ] Dot product connection
* [ ] First neuron from scratch
* [ ] Neuron prediction
* [ ] Neuron loss
* [ ] Updating neuron parameters

### Activation Functions

* [ ] Why nonlinear activation is necessary
* [ ] Step function
* [ ] Sigmoid
* [ ] Tanh
* [ ] ReLU
* [ ] Leaky ReLU
* [ ] GELU
* [ ] Activation-function trade-offs

### Layers

* [ ] Multiple neurons
* [ ] Dense / linear layer
* [ ] Input layer
* [ ] Hidden layer
* [ ] Output layer
* [ ] Weight matrix
* [ ] Bias vector
* [ ] Layer dimensions
* [ ] Forward pass

### Network Training

* [ ] Loss across multiple outputs
* [ ] Backpropagation through a layer
* [ ] Backpropagation through multiple layers
* [ ] Gradient accumulation
* [ ] Vanishing gradients
* [ ] Exploding gradients
* [ ] Weight initialization
* [ ] Xavier initialization intuition
* [ ] He initialization intuition

### First Neural Network From Scratch

* [ ] Build neuron using NumPy
* [ ] Build layer using NumPy
* [ ] Build multi-layer network
* [ ] Forward propagation
* [ ] Loss
* [ ] Manual backpropagation
* [ ] Train the network

---

# Phase 3 — PyTorch

## 6. PyTorch Foundations

### PyTorch Tensors

* [ ] Install PyTorch
* [ ] Create tensors
* [ ] Tensor dtype
* [ ] Tensor shape
* [ ] Tensor operations
* [ ] NumPy ↔ PyTorch
* [ ] CPU tensors
* [ ] GPU tensors
* [ ] Device management

### Autograd

* [ ] `requires_grad`
* [ ] Computational graph
* [ ] `.backward()`
* [ ] `.grad`
* [ ] Gradient accumulation
* [ ] `zero_grad`
* [ ] Detaching tensors
* [ ] Automatic differentiation vs manual derivatives

### Building Models

* [ ] `nn.Module`
* [ ] `nn.Linear`
* [ ] Parameters
* [ ] Forward method
* [ ] Loss functions
* [ ] Optimizers
* [ ] `optimizer.step()`
* [ ] Training mode
* [ ] Evaluation mode

### Data Pipeline

* [ ] Dataset
* [ ] DataLoader
* [ ] Batch loading
* [ ] Shuffling
* [ ] Custom Dataset
* [ ] Collation
* [ ] Padding sequences

### Training Loop

* [ ] Forward pass
* [ ] Loss calculation
* [ ] Backward pass
* [ ] Parameter update
* [ ] Epoch loop
* [ ] Validation loop
* [ ] Metrics
* [ ] Saving checkpoints
* [ ] Loading checkpoints

---

# Phase 4 — Embeddings and Language Representation

## 7. Embeddings

* [ ] Why token IDs are insufficient
* [ ] Embedding table
* [ ] Token ID as lookup index
* [ ] Embedding vector
* [ ] Embedding dimensions
* [ ] Learned embeddings
* [ ] Similarity between vectors
* [ ] Dot product similarity
* [ ] Cosine similarity
* [ ] Embedding matrix
* [ ] Embedding lookup in PyTorch
* [ ] Training embeddings
* [ ] Input embeddings
* [ ] Output embeddings
* [ ] Weight tying

## Optional Embedding Topics

* [ ] Word2Vec intuition
* [ ] CBOW
* [ ] Skip-gram
* [ ] Static vs contextual embeddings

---

# Phase 5 — Transformers

## 8. Transformer Foundations

### Sequence Representation

* [ ] Sequence of token embeddings
* [ ] Sequence length
* [ ] Context
* [ ] Why order matters
* [ ] Positional information
* [ ] Positional encoding
* [ ] Learned positional embeddings
* [ ] Rotary Position Embeddings intuition

### Attention Foundations

* [ ] Why attention exists
* [ ] Query
* [ ] Key
* [ ] Value
* [ ] Query projection
* [ ] Key projection
* [ ] Value projection
* [ ] Dot-product similarity
* [ ] Attention scores
* [ ] Scaling attention scores
* [ ] Softmax
* [ ] Weighted value combination
* [ ] Attention matrix

### Self-Attention

* [ ] Self-attention intuition
* [ ] Self-attention dimensions
* [ ] Causal masking
* [ ] Padding masks
* [ ] Attention from scratch
* [ ] NumPy implementation
* [ ] PyTorch implementation

### Multi-Head Attention

* [ ] Why multiple heads?
* [ ] Head dimensions
* [ ] Independent projections
* [ ] Concatenating heads
* [ ] Output projection
* [ ] Multi-head attention implementation

### Transformer Block

* [ ] Attention layer
* [ ] Feed-forward network
* [ ] Residual connections
* [ ] Layer normalization
* [ ] Dropout
* [ ] Pre-norm vs post-norm intuition
* [ ] Complete transformer block

---

# Phase 6 — Language Models

## 9. Language Modeling

* [ ] What is a language model?
* [ ] Autoregressive modeling
* [ ] Next-token prediction
* [ ] Context → next token
* [ ] Vocabulary logits
* [ ] Softmax over vocabulary
* [ ] Target token
* [ ] Cross-entropy loss
* [ ] Teacher forcing
* [ ] Shifted input/target sequences
* [ ] Training sequences
* [ ] Inference sequences

## Text Generation

* [ ] Greedy decoding
* [ ] Temperature
* [ ] Top-k sampling
* [ ] Top-p / nucleus sampling
* [ ] Repetition
* [ ] Stop tokens
* [ ] EOS handling
* [ ] Generation loop

---

# Phase 7 — GPT From Scratch

## 10. Tiny GPT

* [ ] Tokenizer
* [ ] Training corpus
* [ ] Token embeddings
* [ ] Positional information
* [ ] Self-attention
* [ ] Multi-head attention
* [ ] Transformer block
* [ ] Multiple transformer blocks
* [ ] Layer normalization
* [ ] Language-model head
* [ ] Cross-entropy loss
* [ ] Backpropagation
* [ ] Optimizer
* [ ] Training loop
* [ ] Validation
* [ ] Text generation
* [ ] Save model
* [ ] Load model

## Goal

Build and understand a small GPT-style language model rather than merely calling a prebuilt API.

---

# Phase 8 — Training & Evaluation

## 11. Training Fundamentals

* [ ] Training / validation / test split
* [ ] Epoch
* [ ] Step
* [ ] Batch
* [ ] Training loss
* [ ] Validation loss
* [ ] Generalization
* [ ] Underfitting
* [ ] Overfitting
* [ ] Regularization
* [ ] Dropout
* [ ] Weight decay
* [ ] Early stopping
* [ ] Hyperparameters

## Evaluation

* [ ] Accuracy
* [ ] Precision
* [ ] Recall
* [ ] F1
* [ ] Regression metrics
* [ ] Perplexity
* [ ] Language-model evaluation
* [ ] Benchmark limitations
* [ ] Train/test contamination
* [ ] Human evaluation

## Experimentation

* [ ] Baselines
* [ ] Controlled experiments
* [ ] Change one variable at a time
* [ ] Track experiments
* [ ] Reproducibility
* [ ] Random seeds
* [ ] Logging
* [ ] Compare learning rates
* [ ] Compare optimizers
* [ ] Compare architectures

---

# Phase 9 — Modern LLM Engineering

## 12. Pretraining

* [ ] Pretraining objective
* [ ] Corpus construction
* [ ] Dataset cleaning
* [ ] Deduplication
* [ ] Data mixtures
* [ ] Token budgets
* [ ] Scaling intuition
* [ ] Checkpoints
* [ ] Distributed training overview

## Fine-Tuning

* [ ] Supervised Fine-Tuning
* [ ] Instruction tuning
* [ ] Dataset formatting
* [ ] Fine-tuning loss
* [ ] Full fine-tuning
* [ ] Parameter-efficient fine-tuning
* [ ] LoRA
* [ ] QLoRA
* [ ] Adapter intuition

## Preference Optimization

* [ ] Preference data
* [ ] Reward models
* [ ] RLHF intuition
* [ ] PPO overview
* [ ] DPO intuition
* [ ] Modern preference optimization overview

## Retrieval-Augmented Generation

* [ ] Why RAG?
* [ ] Documents
* [ ] Chunking
* [ ] Embeddings
* [ ] Vector databases
* [ ] Similarity search
* [ ] Retrieval
* [ ] Context construction
* [ ] Grounded generation
* [ ] Reranking
* [ ] RAG evaluation

---

# Phase 10 — Inference & Deployment

## 13. LLM Inference

* [ ] Training vs inference
* [ ] Prefill
* [ ] Decode
* [ ] KV cache
* [ ] Batch inference
* [ ] Dynamic batching
* [ ] Memory usage
* [ ] Latency
* [ ] Throughput
* [ ] Context length
* [ ] Quantization
* [ ] FP32
* [ ] FP16
* [ ] BF16
* [ ] INT8
* [ ] INT4

## Model Serving

* [ ] Inference API
* [ ] Model server
* [ ] Request batching
* [ ] Streaming responses
* [ ] Concurrency
* [ ] Rate limiting
* [ ] Load testing
* [ ] Monitoring
* [ ] Logging
* [ ] Failure handling

## Optional Inference Engines

* [ ] Hugging Face Transformers
* [ ] vLLM
* [ ] llama.cpp
* [ ] TensorRT-LLM overview
* [ ] ONNX overview

---

# Phase 11 — AI Systems Engineering

## 14. Compute Foundations

* [ ] CPU vs GPU
* [ ] GPU architecture intuition
* [ ] GPU memory
* [ ] VRAM
* [ ] Memory bandwidth
* [ ] Parallel computation
* [ ] CUDA overview
* [ ] Kernel intuition
* [ ] Host ↔ device transfer
* [ ] Compute-bound vs memory-bound workloads

## Performance

* [ ] Profiling
* [ ] Vectorization
* [ ] Batch size effects
* [ ] Memory allocation
* [ ] Mixed precision
* [ ] Gradient accumulation
* [ ] Gradient checkpointing
* [ ] FlashAttention intuition
* [ ] Efficient attention

## Distributed Training

* [ ] Data parallelism
* [ ] Model parallelism
* [ ] Tensor parallelism
* [ ] Pipeline parallelism
* [ ] Distributed Data Parallel
* [ ] All-reduce intuition
* [ ] Multi-GPU training
* [ ] Distributed checkpoints

---

# Phase 12 — AI Engineering Tools

## 15. Development Environment

* [x] Python
* [x] Virtual environments
* [x] `pip`
* [x] Project-local dependencies
* [ ] Requirements files
* [ ] `pyproject.toml`
* [ ] Environment variables
* [ ] Configuration files

## Git & GitHub

* [x] Git repository
* [x] Commits
* [x] Commit messages
* [ ] Branches
* [ ] Merge
* [ ] Pull requests
* [ ] Issues
* [ ] Tags / releases
* [ ] `.gitignore`
* [ ] Reproducible repositories

## Engineering Practices

* [ ] Functions
* [ ] Modules
* [ ] Packages
* [ ] Classes
* [ ] Type hints
* [ ] Error handling
* [ ] Logging
* [ ] Unit tests
* [ ] Integration tests
* [ ] Debugging
* [ ] Profiling
* [ ] Documentation

---

# Phase 13 — Research Skills

## 16. Reading AI Research

* [ ] How to read an AI paper
* [ ] Abstract
* [ ] Introduction
* [ ] Related work
* [ ] Method
* [ ] Experiments
* [ ] Ablation studies
* [ ] Limitations
* [ ] References
* [ ] Reproduce paper results
* [ ] Identify assumptions
* [ ] Critically evaluate claims

## Experiment Design

* [ ] Research question
* [ ] Hypothesis
* [ ] Baseline
* [ ] Independent variable
* [ ] Dependent variable
* [ ] Controlled variables
* [ ] Ablation
* [ ] Reproducibility
* [ ] Statistical uncertainty
* [ ] Document results

---

# Phase 14 — AI Safety & Reliability

## 17. Reliability

* [ ] Hallucinations
* [ ] Calibration
* [ ] Distribution shift
* [ ] Robustness
* [ ] Evaluation failures
* [ ] Data quality
* [ ] Prompt sensitivity

## Safety

* [ ] AI safety fundamentals
* [ ] Dataset risks
* [ ] Bias
* [ ] Privacy
* [ ] Adversarial inputs
* [ ] Prompt injection
* [ ] Jailbreak concepts
* [ ] Model misuse
* [ ] Safe deployment practices

---

# Phase 15 — Projects

## 18. Progressive Projects

### Project 1 — Linear Learner From Scratch

* [x] Single parameter
* [x] Prediction
* [x] Loss
* [x] Gradient
* [x] Gradient descent
* [x] Multiple training samples

### Project 2 — BPE Tokenizer From Scratch

* [x] Character splitting
* [x] Pair frequencies
* [x] Pair merging
* [x] Merge rules
* [x] Vocabulary
* [x] Token IDs
* [ ] Tokenize unseen text
* [ ] Decode unseen text

### Project 3 — First Neural Network From Scratch

* [ ] Multiple inputs
* [ ] Multiple weights
* [ ] Neuron
* [ ] Layers
* [ ] Activation
* [ ] Backpropagation
* [ ] Training

### Project 4 — PyTorch Neural Network

* [ ] Dataset
* [ ] DataLoader
* [ ] Model
* [ ] Loss
* [ ] Optimizer
* [ ] Training
* [ ] Evaluation

### Project 5 — Tiny Language Model

* [ ] Character/subword dataset
* [ ] Embeddings
* [ ] Context windows
* [ ] Next-token prediction
* [ ] Generation

### Project 6 — GPT From Scratch

* [ ] Tokenizer
* [ ] Attention
* [ ] Transformer blocks
* [ ] Training
* [ ] Inference

### Project 7 — RAG System

* [ ] Document ingestion
* [ ] Chunking
* [ ] Embeddings
* [ ] Retrieval
* [ ] Generation
* [ ] Evaluation

### Project 8 — Fine-Tuned Model

* [ ] Dataset
* [ ] Fine-tuning
* [ ] LoRA
* [ ] Evaluation
* [ ] Inference

### Project 9 — Production AI Service

* [ ] Model serving
* [ ] API
* [ ] Streaming
* [ ] Monitoring
* [ ] Evaluation
* [ ] Deployment

---

# Current Active Learning Tracks

## Model Learning

Current focus:

Gradient descent → multiple parameters → derivatives → chain rule → backpropagation

---

## Tokenizer

Current focus:

BPE training → saved merge rules → unseen-text tokenization

---

## Math for AI

Starting focus:

Functions → slope → derivatives → vectors → dot product

---

## Tensors & Data

Starting focus:

NumPy arrays → scalars/vectors/matrices/tensors → shape → dimensions → operations

---

# Dependency Unlocks

Some later topics should not begin until necessary prerequisites are understood.

## First Neuron Unlock

Requires:

* Multiple weights
* Vectors
* Dot product
* Basic tensor operations

---

## Backpropagation Unlock

Requires:

* Derivatives
* Partial derivatives
* Chain rule
* Computational graphs
* Gradients

---

## Embeddings Unlock

Requires:

* Token IDs
* Vectors
* Matrices
* Tensor indexing

---

## Self-Attention Unlock

Requires:

* Embeddings
* Dot product
* Matrix multiplication
* Softmax
* Tensor shapes

---

## Transformer Block Unlock

Requires:

* Self-attention
* Multi-head attention
* Feed-forward networks
* Residual connections
* Layer normalization

---

## GPT From Scratch Unlock

Requires:

* Tokenizer
* Embeddings
* Neural networks
* Backpropagation
* PyTorch
* Self-attention
* Transformer blocks
* Next-token prediction
* Cross-entropy

---

# Guiding Learning Principle

Whenever possible:

1. Understand the problem.
2. Understand why the concept exists.
3. Build the simplest version manually.
4. Inspect what happens internally.
5. Connect it to the mathematics.
6. Rebuild it using NumPy where appropriate.
7. Learn how PyTorch automates it.
8. Connect it to modern AI systems.
9. Experiment with it.
10. Use it in a project.

Avoid treating libraries or formulas as magic.

The goal is not merely to know how to call AI tools.

The goal is to understand what those tools are doing underneath.
