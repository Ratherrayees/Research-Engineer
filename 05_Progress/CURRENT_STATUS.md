# AI Engineering Journey — Current Status

Last updated: Day 003

---

# Overall Status

Current active learning tracks:

* Model Learning
* Tokenizer
* Math for AI
* Tensors & Data

Later tracks such as Neural Networks, PyTorch, and Transformers are not active yet. They will unlock when their prerequisites are ready.

---

# 1. Model Learning

## Completed

* [x] What is a model?
* [x] Inputs and outputs
* [x] Parameters
* [x] Weight
* [x] Prediction
* [x] Actual target
* [x] Error
* [x] Loss
* [x] Squared loss
* [x] Learning rate
* [x] First learning loop
* [x] Basic derivative intuition
* [x] Basic gradient intuition
* [x] Gradient sign
* [x] Gradient magnitude
* [x] Gradient descent
* [x] Manual parameter updates
* [x] NumPy arrays for multiple training samples
* [x] Mean loss
* [x] Mean Squared Error intuition
* [x] Batch gradient across multiple samples
* [x] Model convergence toward the correct weight

## Current Understanding

Current simple model:

Input data

↓

Prediction using a weight

↓

Compare prediction with target

↓

Calculate error

↓

Square error

↓

Take mean loss across the dataset

↓

Calculate gradient

↓

Use learning rate to control update size

↓

Update weight

↓

Repeat

The current model successfully learns approximately:

w = 2

from training data where:

y = 2x

without being explicitly given that weight.

## Current Focus

* [ ] Derivatives in deeper detail
* [ ] Multiple parameters / weights
* [ ] Gradient vector

## Next

* [ ] Partial derivatives
* [ ] Chain rule
* [ ] Computational graphs
* [ ] Backpropagation

## Unlock Goal

Once multiple weights, chain rule, and backpropagation are understood:

First neuron → Neural Network track

---

# 2. Tokenizer

## Completed

### Day 001

* [x] Split text into tokens
* [x] Build vocabulary
* [x] Assign token IDs
* [x] Encode tokens
* [x] Decode IDs
* [x] Understand repeated tokens sharing one ID

### Day 002

* [x] Reverse vocabulary
* [x] Direct ID → token lookup
* [x] Reconstruct original sentence
* [x] Discover punctuation problem
* [x] Understand limitations of whitespace tokenization

### Day 003

* [x] Understand subword tokenization
* [x] Understand why BPE exists
* [x] Split corpus into words
* [x] Split words into characters
* [x] Preserve word boundaries
* [x] Count neighboring token pairs
* [x] Find most frequent pair
* [x] Merge pair everywhere
* [x] Repeat BPE merge rounds
* [x] Add maximum merge rounds
* [x] Observe subwords growing over time
* [x] Save learned merge rules
* [x] Build vocabulary from resulting pieces
* [x] Assign integer IDs
* [x] Encode BPE pieces

## Important Observations

BPE was observed building progressively larger pieces such as:

t + o

↓

to

↓

to + k

↓

tok

↓

tok + en

↓

token

↓

token + iz

↓

tokeniz

↓

tokeniz + er

↓

tokenizer

This confirms the core BPE behavior:

Characters → frequent pairs → subwords → sometimes complete words

## Current Focus

* [ ] Apply saved BPE merge rules to unseen text
* [ ] Test unseen words

## Next

* [ ] Decode BPE output
* [ ] Handle word boundaries during decoding
* [ ] Handle whitespace explicitly
* [ ] Byte-level tokenization
* [ ] Special tokens
* [ ] Padding
* [ ] Truncation
* [ ] Attention masks

## Unlock Goal

Once token IDs and tensor/vector concepts are comfortable:

Embeddings → Transformer foundations

---

# 3. Math for AI

## Current Status

Track created but systematic study has not started yet.

Some mathematics has already appeared naturally during Model Learning.

## Already Encountered

* [x] Basic arithmetic
* [x] Variables
* [x] Multiplication
* [x] Squaring
* [x] Mean
* [x] Basic function-like relationships
* [x] Basic derivative intuition
* [x] Basic gradient intuition

## Current Focus

Begin from the mathematics directly required by current AI work.

Recommended order:

* [ ] Functions
* [ ] Inputs and outputs of functions
* [ ] Graphs
* [ ] Slope
* [ ] Rate of change
* [ ] Derivative intuition
* [ ] Derivatives
* [ ] Vectors
* [ ] Dot product
* [ ] Matrices
* [ ] Matrix multiplication

## Near-Term Goal

Understand enough calculus to support:

Gradient → Chain Rule → Backpropagation

Understand enough linear algebra to support:

Multiple weights → Neuron → Embeddings → Attention

---

# 4. Tensors & Data

## Already Encountered

* [x] Python lists
* [x] NumPy installation
* [x] NumPy import
* [x] `np.array`
* [x] Arrays containing multiple training samples
* [x] Element-wise multiplication
* [x] Element-wise subtraction
* [x] Squaring array values
* [x] `np.mean`

## Current Understanding

NumPy allows operations over collections of numerical data at once.

Instead of manually processing one training observation at a time, the learning model can operate across an entire dataset.

Example conceptual flow:

Dataset arrays

↓

Vectorized prediction

↓

Vectorized errors

↓

Vectorized losses

↓

Mean loss

↓

Mean gradient

## Current Focus

* [ ] Python list vs NumPy array
* [ ] Scalar
* [ ] Vector
* [ ] Matrix
* [ ] Tensor
* [ ] Shape
* [ ] Dimension
* [ ] Axis

## Next

* [ ] Indexing
* [ ] Slicing
* [ ] Element-wise operations
* [ ] Broadcasting
* [ ] Reshaping
* [ ] Dot products
* [ ] Matrix multiplication
* [ ] Batches
* [ ] Batch dimensions

## Unlock Goal

Once vectors, matrices, and shapes are comfortable:

Multiple-weight models → First neuron → Embeddings → PyTorch tensors

---

# Cross-Track Dependencies

## Model Learning Needs

Math:

* Derivatives
* Partial derivatives
* Chain rule

Tensors & Data:

* Vectors
* Arrays
* Multiple parameters

---

## Tokenizer Needs

Tensors & Data:

* Arrays
* Sequence representation

Later Math:

* Vectors for embeddings

---

## Neural Networks Will Need

Model Learning:

* Gradients
* Chain rule
* Backpropagation

Math:

* Vectors
* Dot product
* Matrices

Tensors & Data:

* Shapes
* Matrix operations
* Batches

---

## Transformers Will Need

Tokenizer:

* Token IDs
* Subword tokenization

Math:

* Vectors
* Dot products
* Matrices
* Softmax

Tensors & Data:

* Tensor shapes
* Batch dimension
* Sequence dimension

Neural Networks:

* Layers
* Parameters
* Forward pass
* Backpropagation

---

# Current Priority

Recommended active sequence:

## Model Learning

Multiple weights → derivatives → gradient vector → chain rule

## Tokenizer

Apply BPE merge rules to unseen text

## Math for AI

Functions → slope → derivatives → vectors

## Tensors & Data

Arrays → scalar → vector → matrix → tensor → shape

---

# Current Project Milestones

## Linear Learner From Scratch

Status:

Completed basic version

Features:

* single learned weight
* multiple training samples
* Mean Squared Error
* batch gradient
* learning rate
* iterative gradient descent

Next evolution:

multiple weights

---

## BPE Tokenizer From Scratch

Status:

Core training mechanism completed

Features:

* character initialization
* pair frequency counting
* most-common-pair selection
* repeated merging
* merge-rule storage
* vocabulary construction
* token IDs

Next evolution:

apply learned rules to unseen text

---

# Immediate Next Milestones

* [ ] Tokenize unseen text using saved BPE rules
* [ ] Start Math track with functions and slope
* [ ] Start Tensors & Data with scalar/vector/matrix/tensor
* [ ] Extend learning model from one weight to multiple weights

---

# Current Mental Model

The AI system being built piece by piece is beginning to look like:

Human text

↓

Tokenizer

↓

Token IDs

↓

Embeddings

↓

Neural network

↓

Prediction

↓

Loss

↓

Gradients

↓

Parameter updates

The current four active tracks are independently building the knowledge needed to understand each part of this pipeline.
