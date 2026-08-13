# AI Engineering Journey — Dependency Map

## Purpose

This file tracks how the major learning topics depend on one another.

The goal is to avoid two problems:

1. Starting a topic before its foundations are ready.
2. Relearning the same concept in multiple tracks without connecting them.

The learning tracks are independent enough to study in parallel, but they are connected by prerequisite gates.

---

# Core Learning Tracks

Current active tracks:

1. Model Learning
2. Tokenizer
3. Math for AI
4. Tensors & Data

Future tracks:

5. Neural Networks
6. PyTorch
7. Embeddings
8. Transformers
9. Language Models
10. Training & Evaluation
11. LLM Engineering
12. Inference & Deployment

---

# High-Level Dependency Flow

```text
Math ───────────────┐
                    │
Tensors & Data ─────┼────→ Neural Networks ─────→ Transformers
                    │              │                    │
Model Learning ─────┘              │                    │
                                   │                    │
Tokenizer ─────────────→ Embeddings┘                    │
                                                        ↓
                                                Language Models
                                                        ↓
                                                 GPT From Scratch
                                                        ↓
                                         Training / Inference / Serving
```

---

# 1. Model Learning Dependencies

## Current Path

```text
Prediction
↓
Error
↓
Loss
↓
Learning Rate
↓
Derivative
↓
Gradient
↓
Gradient Descent
↓
Multiple Parameters
↓
Partial Derivatives
↓
Chain Rule
↓
Computational Graph
↓
Backpropagation
```

---

## Gradient Depends On

Required:

* Functions
* Input/output relationships
* Error
* Loss
* Basic derivative intuition

Helpful:

* Graphs
* Slope
* Rate of change

---

## Gradient Descent Depends On

Required:

* Gradient
* Learning rate
* Parameters
* Loss

Conceptual relationship:

```text
Current parameters
↓
Calculate loss
↓
Calculate gradient
↓
Scale gradient using learning rate
↓
Update parameters
↓
Repeat
```

---

## Multiple Parameters Depends On

Required:

* Single-parameter learning
* Vectors
* NumPy arrays
* Basic gradient understanding

Unlocks:

* Gradient vectors
* Neurons
* Weight vectors
* Matrix-based layers

---

## Partial Derivatives Depend On

Required:

* Functions
* Derivatives
* Multiple variables

Unlocks:

* Multiple-parameter optimization
* Gradient vectors
* Backpropagation

---

## Chain Rule Depends On

Required:

* Derivatives
* Functions composed of other functions
* Basic computational-flow intuition

Unlocks:

* Backpropagation
* Deep neural networks
* Automatic differentiation

---

## Backpropagation Depends On

Required:

* Loss
* Derivatives
* Partial derivatives
* Chain rule
* Computational graphs
* Multiple parameters

Unlocks:

* Trainable neural networks
* PyTorch autograd understanding
* Transformer training

---

# 2. Tokenizer Dependencies

## Basic Tokenization Path

```text
Text
↓
Tokens
↓
Vocabulary
↓
Token IDs
↓
Encoding / Decoding
```

These are already understood.

---

## Subword Tokenization Depends On

Required:

* Token
* Vocabulary
* Token IDs
* Unknown-word problem
* Character-level tokenization intuition

Unlocks:

* BPE
* WordPiece
* Unigram tokenization
* Modern tokenizer understanding

---

## BPE Depends On

Required:

* Corpus
* Character splitting
* Frequency counting
* Adjacent pairs
* Repeated merging
* Vocabulary construction

Current state:

Core BPE training mechanism implemented.

---

## Reusable BPE Tokenizer Depends On

Required:

* Saved merge rules
* Merge-rule order
* Vocabulary
* Token IDs

Next step:

```text
Unseen text
↓
Split into initial units
↓
Apply saved merge rules in order
↓
Produce subword tokens
↓
Map to token IDs
```

Unlocks:

* Practical tokenizer use
* Production tokenizer comparison

---

## Byte-Level Tokenization Depends On

Required:

* Character-level BPE understanding
* Basic Unicode awareness
* Bytes
* UTF-8 intuition

Unlocks:

* Understanding GPT-style tokenization
* Robust arbitrary-text tokenization
* Better handling of unseen text

---

## Special Tokens Depend On

Required:

* Vocabulary
* Token IDs

Topics:

* BOS
* EOS
* PAD
* UNK
* MASK

Unlocks:

* Sequence batching
* Model input formatting
* Training pipelines

---

## Padding and Truncation Depend On

Required:

* Sequence length
* Token IDs
* Batches
* Tensor shapes

Unlocks:

* DataLoader sequence batches
* Attention masks
* Transformer training

---

# 3. Math Dependencies

Math should be studied only as deeply as needed for the AI concepts it unlocks.

---

## Functions

Required before:

* Derivatives
* Loss functions
* Activation functions

---

## Slope

Depends on:

* Basic algebra
* Coordinates
* Change in x and y

Unlocks:

* Derivative intuition
* Gradient intuition

---

## Derivatives

Depends on:

* Functions
* Slope
* Rate of change

Unlocks:

* Gradient
* Chain rule
* Backpropagation
* Optimization

---

## Partial Derivatives

Depends on:

* Derivatives
* Multivariable functions

Unlocks:

* Gradient vectors
* Neural-network parameter updates

---

## Vectors

Depends on:

* Basic arithmetic

Unlocks:

* Multiple weights
* Embeddings
* Dot products
* Neural inputs
* Attention

---

## Dot Product

Depends on:

* Vectors
* Multiplication
* Summation

Unlocks:

* Neuron weighted sums
* Similarity
* Embedding comparison
* Attention scores

Critical connection:

```text
Neuron weighted sum
=
Input vector · Weight vector
```

---

## Matrices

Depends on:

* Vectors
* Rows and columns
* Shape

Unlocks:

* Neural-network layers
* Embedding tables
* Attention
* Transformer operations

---

## Matrix Multiplication

Depends on:

* Vectors
* Dot product
* Matrix shapes

Unlocks:

* Dense layers
* Q/K/V projections
* Attention
* Transformer blocks

---

## Probability Distributions

Depends on:

* Basic probability
* Normalization
* Functions

Unlocks:

* Softmax
* Token probabilities
* Sampling

---

## Softmax

Depends on:

* Exponentials
* Probability distributions
* Vectors

Unlocks:

* Attention weights
* Next-token probabilities

---

## Logarithms

Depends on:

* Exponents

Unlocks:

* Log probabilities
* Cross-entropy
* Perplexity
* Numerical stability

---

# 4. Tensors & Data Dependencies

## NumPy Arrays

Depends on:

* Python lists
* Basic indexing

Unlocks:

* Vectorized model operations
* Vectors
* Matrices
* Tensor intuition

---

## Scalar → Vector → Matrix → Tensor

Recommended order:

```text
Scalar
↓
Vector
↓
Matrix
↓
Higher-dimensional tensor
```

Unlocks:

* Tensor shapes
* Model data representation
* PyTorch

---

## Shape Depends On

Required:

* Arrays
* Dimensions

Unlocks:

* Matrix multiplication
* Batch processing
* Transformer tensor reasoning

---

## Axis Depends On

Required:

* Shape
* Dimensions

Unlocks:

* Mean across specific dimensions
* Softmax dimensions
* Tensor reductions

---

## Broadcasting Depends On

Required:

* Shapes
* Element-wise operations

Unlocks:

* Efficient tensor math
* Bias addition
* Batch calculations

---

## Batches Depend On

Required:

* Dataset
* Samples
* Arrays
* Shape

Unlocks:

* Mini-batch training
* DataLoaders
* GPU training

---

## Sequence Tensors Depend On

Required:

* Batches
* Sequence length
* Token IDs
* Shapes

Critical shape:

```text
[batch, sequence]
```

After embeddings:

```text
[batch, sequence, embedding]
```

This shape becomes central in transformer work.

---

# 5. Neural Network Dependencies

## First Neuron Unlock

Requires:

Model Learning:

* Parameters
* Multiple weights
* Gradient descent

Math:

* Vectors
* Dot product

Tensors:

* NumPy arrays
* Vector operations

Then:

```text
inputs
×
weights
↓
weighted sum
+
bias
↓
activation
```

---

## Activation Functions Depend On

Required:

* Functions
* Neuron output

Unlocks:

* Nonlinear neural networks
* Multi-layer learning

---

## Neural Layer Depends On

Required:

* Multiple neurons
* Vectors
* Matrices
* Matrix multiplication

Unlocks:

* Multi-layer neural networks

---

## Multi-Layer Network Depends On

Required:

* Layers
* Activation functions
* Forward pass
* Backpropagation

Unlocks:

* Deep learning
* Transformer feed-forward networks

---

# 6. PyTorch Dependencies

PyTorch should come after manual understanding of the concept it automates.

---

## PyTorch Tensors Unlock

Requires:

* NumPy arrays
* Scalars
* Vectors
* Matrices
* Tensor shapes

---

## Autograd Unlock

Requires:

* Derivatives
* Gradients
* Chain rule
* Backpropagation intuition

Manual understanding first:

```text
calculate gradient manually
↓
understand chain rule
↓
then use .backward()
```

---

## nn.Linear Unlock

Requires:

* Neuron
* Weight matrix
* Bias
* Matrix multiplication

---

## Optimizers Unlock

Requires:

* Gradient descent
* Parameter updates
* Learning rate

---

## Dataset / DataLoader Unlock

Requires:

* Dataset
* Samples
* Batch
* Tensor shapes
* Sequence padding

---

# 7. Embedding Dependencies

## Embeddings Unlock

Requires:

Tokenizer:

* Token IDs
* Vocabulary

Math:

* Vectors
* Matrices

Tensors:

* Tensor indexing
* Shapes

Then:

```text
Token ID
↓
Embedding-table row lookup
↓
Embedding vector
```

---

## Embedding Similarity Depends On

Required:

* Vectors
* Dot product
* Vector magnitude

Optional:

* Cosine similarity

---

# 8. Transformer Dependencies

## Positional Information Unlock

Requires:

* Token embeddings
* Sequence positions
* Vector addition / representation

---

## Attention Unlock

Requires:

Math:

* Vectors
* Dot product
* Matrices
* Matrix multiplication
* Softmax

Tensors:

* Shapes
* Sequence dimension
* Batch dimension

Neural Networks:

* Learned weights
* Linear projections

Embeddings:

* Token vectors

---

## Query / Key / Value Depends On

Required:

* Embeddings
* Matrix multiplication
* Linear layers

Conceptual flow:

```text
Embedding
↓
Linear projections
↓
Q, K, V
```

---

## Self-Attention Depends On

Required:

* Query
* Key
* Value
* Dot products
* Softmax
* Weighted sums

---

## Causal Masking Depends On

Required:

* Attention matrix
* Sequence order
* Next-token prediction

---

## Multi-Head Attention Depends On

Required:

* Self-attention
* Tensor reshaping
* Multiple projections
* Concatenation

---

## Transformer Block Depends On

Required:

* Multi-head attention
* Feed-forward network
* Residual connections
* Layer normalization

---

# 9. Language Model Dependencies

## Next-Token Prediction Unlock

Requires:

* Tokenizer
* Vocabulary
* Embeddings
* Transformer output
* Probability distribution

---

## Cross-Entropy Loss Depends On

Required:

* Softmax / probabilities
* Logarithms
* Target token

Unlocks:

* Language-model training

---

## Text Generation Depends On

Required:

* Model logits
* Probability distributions
* Tokenizer decoding

Unlocks:

* Greedy decoding
* Temperature
* Top-k
* Top-p

---

# 10. GPT From Scratch Dependencies

GPT from scratch should begin only when these are ready:

Tokenizer:

* [ ] Reusable tokenizer
* [ ] Token IDs

Math:

* [ ] Vectors
* [ ] Dot products
* [ ] Matrices
* [ ] Softmax
* [ ] Logarithms

Tensors:

* [ ] Tensor shapes
* [ ] Batches
* [ ] Matrix multiplication

Model Learning:

* [ ] Backpropagation

Neural Networks:

* [ ] Layers
* [ ] Activations
* [ ] Forward pass

PyTorch:

* [ ] Tensors
* [ ] Autograd
* [ ] nn.Module
* [ ] Optimizers

Transformers:

* [ ] Embeddings
* [ ] Self-attention
* [ ] Multi-head attention
* [ ] Transformer block

Language Modeling:

* [ ] Next-token prediction
* [ ] Cross-entropy

---

# 11. Training & Evaluation Dependencies

## Mini-Batch Training Depends On

* Dataset
* Batch
* Tensor shapes
* Gradient descent

---

## Validation Depends On

* Training loop
* Dataset splitting
* Loss

---

## Overfitting Depends On

* Training loss
* Validation loss
* Generalization

---

## Regularization Depends On

* Overfitting
* Model capacity

Unlocks:

* Weight decay
* Dropout
* Early stopping

---

# 12. Inference Dependencies

## Inference Unlock

Requires:

* Trained model
* Tokenizer
* Forward pass
* Text generation

---

## KV Cache Depends On

* Self-attention
* Autoregressive generation
* Keys and values

---

## Quantization Depends On

* Numerical precision
* Tensors
* Model weights
* Inference

---

## Efficient Serving Depends On

* Batching
* GPU memory
* Latency
* Throughput
* Model inference

---

# Cross-Track Connection Examples

## Connection 1 — Multiple Weights

Model Learning says:

Multiple parameters

Math says:

Vector

Tensors says:

1D array

Neural Network says:

Weight vector

These are not four unrelated ideas.

They describe the same structure from different perspectives.

---

## Connection 2 — First Neuron

Model:

Prediction using parameters

Math:

Dot product

Tensor:

Vector operation

Neural Network:

Neuron

Combined:

```text
input vector · weight vector + bias
```

---

## Connection 3 — Embeddings

Tokenizer:

Token ID

Math:

Vector

Tensor:

Embedding matrix

Transformer:

Token representation

Combined:

```text
token ID
↓
lookup row in embedding matrix
↓
embedding vector
```

---

## Connection 4 — Attention

Tokenizer:

Sequence of token IDs

Embeddings:

Sequence of vectors

Math:

Dot products + matrices + softmax

Tensor:

[batch, sequence, embedding]

Neural Networks:

Learned projections

Transformer:

Self-attention

---

# Dependency Rules for Parallel Learning

## Rule 1

A topic can begin when its minimum prerequisites are understood.

Do not wait for an entire track to finish.

---

## Rule 2

When two tracks encounter the same concept, connect them instead of teaching them independently.

Example:

Dot product should be learned once and then reused in:

* Math
* Tensors
* Neurons
* Embeddings
* Attention

---

## Rule 3

Manual understanding should usually come before framework automation.

Example:

```text
Manual gradient
↓
Backpropagation
↓
PyTorch autograd
```

---

## Rule 4

Do not introduce advanced mathematics unless it supports a current or near-future AI concept.

---

## Rule 5

When a prerequisite becomes ready, update the roadmap and unlock the dependent topic.

---

# Current Unlock State

## Ready Now

* Model Learning continuation
* BPE tokenizer continuation
* Functions
* Slope
* Derivatives
* Scalar / vector / matrix
* NumPy array fundamentals

---

## Nearly Ready

### Multiple-Weight Model

Needs:

* Vectors
* Basic array shape understanding

### First Neuron

Needs:

* Multiple weights
* Dot product

### Embeddings

Needs:

* Vectors
* Matrices
* Tensor indexing

---

## Locked for Now

### Backpropagation

Needs:

* Derivatives
* Partial derivatives
* Chain rule

### PyTorch Autograd

Needs:

* Backpropagation understanding

### Self-Attention

Needs:

* Embeddings
* Matrix multiplication
* Softmax

### GPT From Scratch

Needs:

* All major transformer prerequisites

---

# Current Parallel Study Strategy

## Model Learning

Study:

Gradient descent → multiple parameters → chain rule → backpropagation

## Tokenizer

Study:

BPE → unseen-text tokenization → byte-level concepts

## Math

Study:

Functions → slope → derivatives → vectors → dot product → matrices

## Tensors & Data

Study:

NumPy arrays → scalar/vector/matrix/tensor → shapes → operations → batches

These four tracks should progress together until they converge into:

Neural Networks

↓

PyTorch

↓

Embeddings

↓

Transformers
