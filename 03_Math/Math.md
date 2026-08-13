# Math for AI — Curriculum & Progress

## Purpose

This track covers the mathematics needed to understand how machine-learning models, neural networks, and transformers actually work.

The goal is **not** to complete mathematics as a separate academic subject.

The goal is to understand each mathematical idea deeply enough to answer:

* what problem does this concept solve?
* why does AI need it?
* what does the formula mean?
* what changes when one quantity changes?
* how does this connect to code?
* where will this appear later in neural networks or transformers?

This track should progress alongside Model Learning and Tensors & Data.

---

# Stage 1 — Mathematical Language

## Concepts

* [ ] Variable
* [ ] Constant
* [ ] Expression
* [ ] Equation
* [ ] Term
* [ ] Coefficient
* [ ] Operator
* [ ] Function notation

## Goal

Become comfortable reading expressions such as:

```text
y = wx + b
```

and understanding:

* `x` = input
* `w` = weight
* `b` = bias
* `y` = output

without treating the equation as something to memorize.

---

# Stage 2 — Functions

## Major Foundation

A machine-learning model can be viewed as a function.

Conceptually:

```text
input
↓
function
↓
output
```

## Topics

* [ ] What is a function?
* [ ] Input
* [ ] Output
* [ ] Independent variable
* [ ] Dependent variable
* [ ] Function notation
* [ ] `f(x)`
* [ ] Evaluating a function
* [ ] Functions with parameters
* [ ] Functions with multiple inputs
* [ ] Functions inside other functions

## AI Connection

A model can be represented as:

```text
prediction = f(input, parameters)
```

A loss function can be represented as:

```text
loss = L(prediction, target)
```

Later:

```text
loss = L(f(x, w), y)
```

This becomes important for derivatives and the chain rule.

---

# Stage 3 — Coordinates and Graphs

## Topics

* [ ] x-axis
* [ ] y-axis
* [ ] Coordinates
* [ ] Plotting points
* [ ] Graph of a function
* [ ] Increasing function
* [ ] Decreasing function
* [ ] Flat region
* [ ] Curved function

## Why It Matters

Graphs allow us to visualize relationships such as:

```text
weight
↓
loss
```

Later we can think of:

```text
Loss = function of weight
```

and ask:

> If the weight changes, does the loss go up or down?

That question leads directly to derivatives.

---

# Stage 4 — Slope

## Topics

* [ ] Change in x
* [ ] Change in y
* [ ] Rise over run
* [ ] Positive slope
* [ ] Negative slope
* [ ] Zero slope
* [ ] Steep slope
* [ ] Shallow slope

## Core Idea

Slope describes:

> how much one quantity changes when another quantity changes.

Conceptually:

```text
change in output
----------------
change in input
```

## AI Connection

Instead of asking:

> How does `y` change when `x` changes?

we will eventually ask:

> How does loss change when a model parameter changes?

That is the core idea behind a derivative.

---

# Stage 5 — Rate of Change

## Topics

* [ ] Average rate of change
* [ ] Local rate of change
* [ ] Difference between overall and local change
* [ ] Small changes
* [ ] Sensitivity

## Example Intuition

Suppose:

```text
weight changes slightly
↓
loss changes significantly
```

Then the loss is very sensitive to that weight.

If:

```text
weight changes slightly
↓
loss barely changes
```

then the sensitivity is smaller.

This sensitivity becomes the derivative.

---

# Stage 6 — Derivative Intuition

## Current Status

Basic intuition has already been encountered in Model Learning.

Now we study it systematically.

## Topics

* [x] Basic derivative intuition
* [ ] Derivative as local slope
* [ ] Derivative as sensitivity
* [ ] Derivative as rate of change
* [ ] Positive derivative
* [ ] Negative derivative
* [ ] Zero derivative
* [ ] Large derivative
* [ ] Small derivative

## Core Question

A derivative answers:

> If I change this input slightly, how does the output change?

In model learning:

> If I change this weight slightly, how does the loss change?

---

# Stage 7 — Derivative Notation

## Topics

* [ ] `dy/dx`
* [ ] `df/dx`
* [ ] `f'(x)`
* [ ] What "with respect to" means
* [ ] Read derivative notation aloud
* [ ] Input variable vs output function

## Goal

Be able to read:

```text
dL/dw
```

as:

> How does loss `L` change with respect to weight `w`?

This is far more important than memorizing notation mechanically.

---

# Stage 8 — Derivatives of Simple Functions

## Topics

* [ ] Constant function
* [ ] Linear function
* [ ] Square function
* [ ] Cubic function
* [ ] Power functions
* [ ] Basic power rule
* [ ] Multiplication by constants
* [ ] Addition of terms

## Example Progression

Understand derivatives of:

```text
y = x
y = 2x
y = x²
y = 3x²
```

before applying them to loss functions.

---

# Stage 9 — Squared Error Derivative

## Important AI Connection

Our model already uses squared error.

Conceptually:

```text
error = prediction - target

loss = error²
```

## Topics

* [ ] Why squaring changes the derivative
* [ ] Derivative of squared error
* [ ] Error magnitude
* [ ] Error direction
* [ ] Why larger errors create larger gradients

## Goal

Connect the derivative formula directly to the gradient code already used in Model Learning.

---

# Stage 10 — Numerical Derivatives

## Practical Intuition

Before trusting symbolic derivatives, we can approximate them.

Conceptually:

```text
loss at weight
vs
loss at slightly changed weight
```

## Topics

* [ ] Small perturbation
* [ ] Finite difference
* [ ] Numerical slope
* [ ] Compare analytical and numerical derivative
* [ ] Numerical derivative limitations

## Why Useful

This is an excellent debugging technique later when implementing backpropagation manually.

---

# Stage 11 — Multiple Variables

## Transition

Current learning model:

```text
loss = function(weight)
```

Later:

```text
loss = function(w1, w2, w3, bias)
```

## Topics

* [ ] Function of two variables
* [ ] Function of many variables
* [ ] Independent parameter changes
* [ ] Hold other variables constant

This prepares us for partial derivatives.

---

# Stage 12 — Partial Derivatives

## Topics

* [ ] What is a partial derivative?
* [ ] "With respect to one variable"
* [ ] Hold other variables fixed
* [ ] `∂L/∂w1`
* [ ] `∂L/∂w2`
* [ ] Bias derivative
* [ ] One derivative per parameter

## Mental Model

If a model contains:

```text
w1
w2
w3
b
```

we ask four separate questions:

```text
How does loss change if w1 changes?
How does loss change if w2 changes?
How does loss change if w3 changes?
How does loss change if b changes?
```

These answers combine into the gradient.

---

# Stage 13 — Gradient

## Topics

* [x] Basic gradient intuition
* [x] Gradient sign
* [x] Gradient magnitude
* [ ] Gradient as collection of partial derivatives
* [ ] Gradient vector
* [ ] Direction of steepest increase
* [ ] Negative gradient
* [ ] Gradient descent connection

## Single Parameter

```text
one parameter
↓
one derivative
```

## Multiple Parameters

```text
many parameters
↓
many partial derivatives
↓
gradient vector
```

---

# Stage 14 — Vectors

## Major Linear Algebra Foundation

## Topics

* [ ] Scalar
* [ ] Vector
* [ ] Vector components
* [ ] Vector notation
* [ ] 1D NumPy array connection
* [ ] Vector length / dimension
* [ ] Row vector
* [ ] Column vector
* [ ] Vector addition
* [ ] Vector subtraction
* [ ] Scalar multiplication

## AI Connection

A model may receive:

```text
[x1, x2, x3]
```

and contain weights:

```text
[w1, w2, w3]
```

These are vectors.

Embeddings are also vectors.

---

# Stage 15 — Vector Magnitude

## Topics

* [ ] Magnitude
* [ ] Length of a vector
* [ ] Euclidean norm intuition
* [ ] Unit vector intuition

## Why Useful

Later:

* gradient size
* cosine similarity
* embedding similarity
* normalization

---

# Stage 16 — Dot Product

## Critical Topic

The dot product is one of the most important operations in AI.

## Topics

* [ ] Multiply matching components
* [ ] Sum the results
* [ ] Input vector · weight vector
* [ ] Dot product as weighted sum
* [ ] Dot product as similarity intuition
* [ ] Positive dot product
* [ ] Negative dot product
* [ ] Near-zero dot product

## Neural Network Connection

Instead of writing:

```text
x1*w1 + x2*w2 + x3*w3
```

we can write conceptually:

```text
input · weights
```

This becomes the mathematical core of a neuron.

## Transformer Connection

Attention later uses dot products to compare vectors.

---

# Stage 17 — Angles and Vector Similarity

## Optional but Valuable

## Topics

* [ ] Angle between vectors
* [ ] Same direction
* [ ] Opposite direction
* [ ] Perpendicular vectors
* [ ] Dot product and angle
* [ ] Cosine similarity

## AI Connection

Useful for:

* embeddings
* semantic search
* vector databases
* RAG
* attention intuition

---

# Stage 18 — Matrices

## Major Foundation

## Topics

* [ ] Matrix
* [ ] Row
* [ ] Column
* [ ] Matrix element
* [ ] Matrix notation
* [ ] Matrix shape
* [ ] Rows × columns
* [ ] Matrix as collection of vectors
* [ ] 2D NumPy array connection

## AI Connection

A neural-network layer may store many weight vectors together as a matrix.

An embedding table is also a matrix.

---

# Stage 19 — Matrix Shapes

## Topics

* [ ] `(rows, columns)`
* [ ] Input dimension
* [ ] Output dimension
* [ ] Compatible dimensions
* [ ] Shape mismatch
* [ ] Why matrix dimensions matter

## Important Habit

Before performing an operation, ask:

> What are the shapes?

This becomes essential in transformer engineering.

---

# Stage 20 — Matrix-Vector Multiplication

## Topics

* [ ] Matrix × vector
* [ ] Each row performs a dot product
* [ ] Multiple outputs
* [ ] Neural layer interpretation

## Connection

One neuron:

```text
vector · weight vector
```

Many neurons:

```text
weight matrix × input vector
```

This is how a neural-network layer becomes compact matrix mathematics.

---

# Stage 21 — Matrix Multiplication

## Critical Topic

## Topics

* [ ] Matrix × matrix
* [ ] Rows vs columns
* [ ] Inner dimensions
* [ ] Output shape
* [ ] Matrix multiplication is not element-wise multiplication
* [ ] Repeated dot products

## AI Connection

Used throughout:

* neural layers
* embedding projections
* Q/K/V projections
* attention scores
* transformer blocks

---

# Stage 22 — Transpose

## Topics

* [ ] Rows become columns
* [ ] Shape reversal
* [ ] Vector transpose
* [ ] Matrix transpose

## Transformer Connection

Attention eventually performs operations conceptually related to:

```text
Q × Kᵀ
```

Understanding transpose before attention will make that expression much easier.

---

# Stage 23 — Identity Matrix

## Optional Foundation

* [ ] Identity matrix
* [ ] Matrix equivalent of multiplying by 1
* [ ] Why identity transformations matter

Useful later for understanding linear transformations and residual ideas.

---

# Stage 24 — Linear Transformations

## Topics

* [ ] Vector in
* [ ] Matrix transformation
* [ ] Vector out
* [ ] Scaling
* [ ] Rotation intuition
* [ ] Projection intuition
* [ ] Change of representation

## AI Connection

A neural linear layer transforms one vector representation into another.

Later:

```text
embedding
↓
linear transformation
↓
query vector
```

---

# Stage 25 — Bias

## Topics

* [ ] Why multiplication alone is limited
* [ ] Bias as shift
* [ ] Scalar bias
* [ ] Bias vector
* [ ] Broadcasting connection

## Neural Network Formula

Conceptually:

```text
output = input · weights + bias
```

or for a full layer:

```text
output = matrix operation + bias
```

---

# Stage 26 — Composition of Functions

## Major Calculus Prerequisite

## Topics

* [ ] Function output becomes another function's input
* [ ] Nested functions
* [ ] `f(g(x))`
* [ ] Multi-stage computation

## Neural Network Connection

A network is essentially many functions composed together.

Example:

```text
input
↓
linear function
↓
activation
↓
linear function
↓
prediction
↓
loss
```

This prepares us for the chain rule.

---

# Stage 27 — Chain Rule

## Critical Topic

## Topics

* [ ] Why chain rule exists
* [ ] Indirect influence
* [ ] Local changes
* [ ] Multiply derivatives through a path
* [ ] Two-function chain
* [ ] Three-function chain
* [ ] Chain rule notation
* [ ] Chain rule in loss calculation

## Core Mental Model

If:

```text
w affects prediction
prediction affects error
error affects loss
```

then:

```text
w affects loss through the whole chain
```

The chain rule combines those effects.

---

# Stage 28 — Computational Graph Mathematics

## Topics

* [ ] Nodes
* [ ] Operations
* [ ] Intermediate values
* [ ] Local derivatives
* [ ] Paths through graph
* [ ] Forward computation
* [ ] Backward derivative flow

## Connection

This is the mathematical foundation of backpropagation and PyTorch autograd.

---

# Stage 29 — Backpropagation Mathematics

## Topics

* [ ] Start from loss
* [ ] Derivative of loss with respect to output
* [ ] Move backward
* [ ] Chain derivatives
* [ ] Compute parameter gradients
* [ ] Shared dependencies
* [ ] Gradient accumulation

## Goal

Understand backpropagation as:

> organized repeated application of the chain rule.

---

# Stage 30 — Exponents

## Topics

* [ ] Repeated multiplication
* [ ] Positive exponents
* [ ] Negative exponents
* [ ] Fractional exponents
* [ ] Exponential growth
* [ ] `e^x`

## AI Connection

Needed for:

* softmax
* probability distributions
* exponential functions
* optimization mathematics

---

# Stage 31 — Logarithms

## Topics

* [ ] Logarithm as inverse of exponentiation
* [ ] `log`
* [ ] Natural logarithm
* [ ] Why logs compress large ranges
* [ ] Log rules intuition
* [ ] Log of probabilities

## AI Connection

Needed for:

* cross-entropy
* log likelihood
* perplexity
* numerical stability

---

# Stage 32 — Probability Fundamentals

## Topics

* [ ] Probability
* [ ] Event
* [ ] Probability range 0–1
* [ ] Mutually exclusive outcomes
* [ ] Sum of probabilities
* [ ] Conditional probability
* [ ] Independence intuition

## Language Model Connection

A language model produces something like:

```text
P(next token | previous tokens)
```

Probability is therefore central to language modeling.

---

# Stage 33 — Random Variables

## Topics

* [ ] Random variable
* [ ] Discrete random variable
* [ ] Continuous random variable
* [ ] Possible outcomes
* [ ] Probability mass intuition

## AI Connection

Token selection during generation can be viewed as sampling from a discrete probability distribution.

---

# Stage 34 — Probability Distributions

## Topics

* [ ] Distribution
* [ ] Discrete distribution
* [ ] Probability vector
* [ ] Distribution sums to 1
* [ ] Concentrated distribution
* [ ] Flat distribution

## LLM Example

A model may produce:

```text
AI      0.50
model   0.25
system  0.15
cat     0.10
```

These values form a probability distribution over possible next tokens.

---

# Stage 35 — Mean

## Already Encountered

* [x] Arithmetic mean
* [x] `np.mean`
* [x] Mean loss

## Additional Topics

* [ ] Mean as expected center
* [ ] Mean across tensor axes
* [ ] Batch mean

---

# Stage 36 — Variance

## Topics

* [ ] Spread around mean
* [ ] Squared deviations
* [ ] Large variance
* [ ] Small variance

## AI Connection

Useful later for:

* initialization
* normalization
* statistics
* activation distributions

---

# Stage 37 — Standard Deviation

## Topics

* [ ] Square root of variance
* [ ] Interpreting spread
* [ ] Same units as original data

## AI Connection

Important for normalization and understanding data distributions.

---

# Stage 38 — Expected Value

## Topics

* [ ] Weighted average of possible outcomes
* [ ] Probability-weighted value
* [ ] Connection with mean

## AI Connection

Useful in probability, reinforcement learning, and statistical reasoning.

---

# Stage 39 — Softmax

## Critical Transformer Topic

## Prerequisites

* vectors
* exponents
* probability distributions

## Topics

* [ ] Input scores
* [ ] Exponentiation
* [ ] Normalize values
* [ ] Output sums to 1
* [ ] Large score gets higher probability
* [ ] Relative differences matter
* [ ] Temperature connection

## Used In

* attention weights
* next-token probabilities
* classification

---

# Stage 40 — Numerical Stability of Softmax

## Optional but Important for Engineering

## Topics

* [ ] Large exponentials
* [ ] Overflow
* [ ] Subtract maximum value
* [ ] Stable softmax

This is one of the first places where mathematics and numerical engineering strongly meet.

---

# Stage 41 — Log Probability

## Topics

* [ ] Probability near 1
* [ ] Probability near 0
* [ ] Log probability
* [ ] Why multiplication becomes addition in log space

## AI Connection

Used heavily in:

* language-model loss
* sequence scoring
* probabilistic modeling

---

# Stage 42 — Cross-Entropy

## Critical Language-Model Topic

## Prerequisites

* probability distributions
* logarithms
* softmax
* target class/token

## Topics

* [ ] Predicted probability distribution
* [ ] Correct target
* [ ] Penalize low probability on correct answer
* [ ] Cross-entropy loss
* [ ] One-hot target intuition
* [ ] Token-level loss

## Language Model Connection

For each training position:

```text
model predicts distribution over vocabulary
↓
actual next token is known
↓
cross-entropy measures prediction quality
```

---

# Stage 43 — Entropy

## Topics

* [ ] Uncertainty
* [ ] Predictable distribution
* [ ] Uniform distribution
* [ ] High entropy
* [ ] Low entropy

## AI Connection

Useful for understanding:

* model uncertainty
* probability distributions
* information theory
* token prediction

---

# Stage 44 — Perplexity

## Topics

* [ ] Language-model uncertainty
* [ ] Relationship to cross-entropy
* [ ] Lower vs higher perplexity
* [ ] Limitations of perplexity

---

# Stage 45 — Sampling

## Topics

* [ ] Random sampling
* [ ] Sample according to probability
* [ ] Deterministic vs stochastic choice
* [ ] Repeated sampling

## Language Model Connection

Text generation frequently samples from next-token probability distributions.

---

# Stage 46 — Temperature

## Topics

* [ ] Rescale logits
* [ ] Low temperature
* [ ] High temperature
* [ ] Distribution sharpness
* [ ] Diversity vs predictability

## Generation Connection

This will later connect directly to LLM decoding.

---

# Stage 47 — Top-k and Top-p Mathematics

## Optional Until Generation Stage

### Top-k

* [ ] Keep highest `k` probabilities
* [ ] Renormalize
* [ ] Sample

### Top-p

* [ ] Sort probabilities
* [ ] Accumulate until threshold
* [ ] Dynamic candidate set
* [ ] Renormalize

---

# Stage 48 — Normalization

## Topics

* [ ] Scaling
* [ ] Centering
* [ ] Standardization
* [ ] Mean subtraction
* [ ] Divide by standard deviation

## AI Connection

Useful for:

* data preprocessing
* neural-network stability
* LayerNorm intuition

---

# Stage 49 — Norms

## Topics

* [ ] L1 norm intuition
* [ ] L2 norm intuition
* [ ] Vector size
* [ ] Distance

## AI Connection

Used in:

* regularization
* gradient clipping
* vector comparison
* optimization

---

# Stage 50 — Distance

## Topics

* [ ] Euclidean distance
* [ ] Manhattan distance intuition
* [ ] Similarity vs distance

## AI Connection

Useful for:

* embeddings
* clustering
* nearest neighbors
* retrieval systems

---

# Stage 51 — Cosine Similarity

## Topics

* [ ] Vector direction
* [ ] Dot product
* [ ] Magnitudes
* [ ] Normalized similarity
* [ ] Range interpretation

## AI Connection

Common in:

* embeddings
* semantic search
* RAG
* vector databases

---

# Stage 52 — High-Dimensional Spaces

## Conceptual Topic

Neural-network vectors often have hundreds or thousands of dimensions.

## Topics

* [ ] Dimension
* [ ] Coordinate per dimension
* [ ] High-dimensional vector
* [ ] Why visualization becomes difficult
* [ ] Similarity still works mathematically

## Transformer Connection

Embedding vectors and hidden states live in high-dimensional spaces.

---

# Stage 53 — Tensor Mathematics

## Crosses Into Tensors & Data Track

## Topics

* [ ] Scalar operation
* [ ] Vector operation
* [ ] Matrix operation
* [ ] Higher-dimensional arrays
* [ ] Element-wise operations
* [ ] Reduction operations
* [ ] Broadcasting mathematics

## Goal

Connect mathematical notation to actual NumPy/PyTorch tensor operations.

---

# Stage 54 — Batch Mathematics

## Topics

* [ ] One sample vs many samples
* [ ] Batch dimension
* [ ] Mean loss across batch
* [ ] Gradient across batch
* [ ] Vectorized computation

## Current Connection

This has already appeared in the Model Learning track when calculating mean loss and mean gradients across many observations.

---

# Stage 55 — Attention Mathematics

## Later Milestone

## Prerequisites

* vectors
* dot product
* matrices
* transpose
* matrix multiplication
* softmax
* tensor shapes

## Topics

* [ ] Query vectors
* [ ] Key vectors
* [ ] Value vectors
* [ ] Query-key similarity
* [ ] Attention scores
* [ ] Scaling
* [ ] Softmax
* [ ] Weighted sum of values

## Conceptual Flow

```text
Q and K
↓
similarity scores
↓
scale
↓
softmax
↓
attention weights
↓
weighted combination of V
```

---

# Stage 56 — Scaling in Attention

## Topics

* [ ] Dot-product magnitude
* [ ] Effect of vector dimension
* [ ] Why large scores affect softmax
* [ ] Scaling by dimension intuition

This should be learned when attention is introduced, not memorized in advance.

---

# Stage 57 — Positional Encoding Mathematics

## Later Topic

## Potential Topics

* [ ] Position vectors
* [ ] Sinusoidal functions intuition
* [ ] Frequency
* [ ] Sine
* [ ] Cosine
* [ ] Rotary transformations intuition

Only the mathematics needed for the positional method being studied should be covered.

---

# Stage 58 — Layer Normalization Mathematics

## Later Topic

## Prerequisites

* mean
* variance
* standard deviation
* scaling

## Topics

* [ ] Mean across features
* [ ] Variance
* [ ] Normalize activations
* [ ] Learnable scale
* [ ] Learnable shift

---

# Stage 59 — Optimization Mathematics

## Topics

* [ ] Gradient descent geometry
* [ ] Parameter space
* [ ] Loss surface
* [ ] Step size
* [ ] Momentum
* [ ] Moving averages
* [ ] Adaptive learning rates

These should be introduced alongside their corresponding Model Learning topics.

---

# Stage 60 — Moving Averages

## Useful for Optimizers

## Topics

* [ ] Running average
* [ ] Exponential moving average
* [ ] Weight recent values more heavily
* [ ] Momentum interpretation

## Adam Connection

Adam uses moving-average-like tracking of gradient information.

---

# Stage 61 — Weight Decay Mathematics

## Topics

* [ ] Parameter magnitude
* [ ] Penalty term
* [ ] L2 intuition
* [ ] Shrinking weights

Useful during regularization study.

---

# Stage 62 — Gradient Clipping Mathematics

## Topics

* [ ] Gradient vector magnitude
* [ ] Threshold
* [ ] Rescale gradient
* [ ] Preserve direction

Useful when studying exploding gradients.

---

# Stage 63 — Floating-Point Numbers

## Engineering Math

## Topics

* [ ] Finite numerical precision
* [ ] Rounding
* [ ] Representation limits
* [ ] FP32
* [ ] FP16
* [ ] BF16 intuition

## AI Connection

Real models do not calculate with infinitely precise mathematical numbers.

Understanding numerical approximation becomes important for large-scale training.

---

# Stage 64 — Overflow and Underflow

## Topics

* [ ] Very large values
* [ ] Very small values
* [ ] Representation limits
* [ ] Exponentials
* [ ] Probabilities

Used later when understanding stable softmax and mixed-precision training.

---

# Stage 65 — Numerical Stability

## Topics

* [ ] Stable formulas
* [ ] Algebraically equivalent but computationally different expressions
* [ ] Avoiding overflow
* [ ] Avoiding division by tiny numbers
* [ ] Small epsilon values

---

# Optional Advanced Linear Algebra

These topics are useful but **not required before building neural networks or transformers**.

## Basis

* [ ] Basis vectors
* [ ] Coordinate systems
* [ ] Change of basis intuition

## Orthogonality

* [ ] Perpendicular vectors
* [ ] Orthogonal basis

## Eigenvalues and Eigenvectors

* [ ] Intuition
* [ ] Transformation directions
* [ ] Why they matter

## Singular Value Decomposition

* [ ] Matrix factorization intuition
* [ ] Low-rank approximation
* [ ] Compression connection
* [ ] LoRA connection

These should be introduced when they become useful rather than studied upfront.

---

# Optional Advanced Calculus

## Jacobian

* [ ] Multiple outputs
* [ ] Multiple inputs
* [ ] Matrix of partial derivatives
* [ ] Neural-network intuition

## Hessian

* [ ] Second derivatives
* [ ] Curvature
* [ ] Optimization intuition

## Second Derivatives

* [ ] Rate of change of derivative
* [ ] Curvature
* [ ] Convexity intuition

These are useful for deeper optimization understanding but should not block normal progress.

---

# Optional Information Theory

Useful later for deeper language-model understanding.

* [ ] Information content
* [ ] Surprise
* [ ] Entropy
* [ ] Cross-entropy
* [ ] KL divergence
* [ ] Bits vs nats

---

# Optional Probability Topics

* [ ] Joint probability
* [ ] Marginal probability
* [ ] Conditional probability in depth
* [ ] Bayes' theorem
* [ ] Maximum likelihood
* [ ] Log likelihood
* [ ] Sampling distributions

Useful later for probabilistic modeling and deeper ML theory.

---

# Practical Exercise Path

## Exercise 001 — Functions

Build simple Python functions and connect:

```text
input
↓
function
↓
output
```

Tasks:

* [ ] linear function
* [ ] squared function
* [ ] change input and observe output
* [ ] change parameter and observe output

---

# Exercise 002 — Visualize Slope

Tasks:

* [ ] choose two points
* [ ] calculate changes
* [ ] calculate slope
* [ ] compare positive and negative slope

Optional:

* [ ] plot simple function

---

# Exercise 003 — Numerical Derivative

Tasks:

* [ ] calculate function output
* [ ] slightly change input
* [ ] calculate output again
* [ ] approximate derivative
* [ ] compare across different points

---

# Exercise 004 — Squared-Loss Derivative

Use a simple model.

Tasks:

* [ ] prediction
* [ ] target
* [ ] error
* [ ] squared loss
* [ ] manually calculate derivative
* [ ] compare with numerical derivative

---

# Exercise 005 — Vectors

Using NumPy:

* [ ] create vectors
* [ ] inspect shape
* [ ] add vectors
* [ ] multiply vector by scalar
* [ ] connect vector components to model inputs

---

# Exercise 006 — Dot Product

Tasks:

* [ ] manually multiply components
* [ ] manually sum them
* [ ] compare with NumPy dot product
* [ ] connect to neuron weighted sum

---

# Exercise 007 — Matrices

Tasks:

* [ ] create matrix
* [ ] inspect rows and columns
* [ ] inspect shape
* [ ] select rows
* [ ] select columns
* [ ] connect matrix to multiple weight vectors

---

# Exercise 008 — Matrix-Vector Multiplication

Tasks:

* [ ] perform manually
* [ ] perform with NumPy
* [ ] understand each output as one dot product
* [ ] connect to multiple neurons

---

# Exercise 009 — Partial Derivatives

Use a function containing two parameters.

Tasks:

* [ ] change first parameter
* [ ] observe output
* [ ] change second parameter
* [ ] observe output
* [ ] calculate separate derivatives

---

# Exercise 010 — Chain Rule

Build a small calculation:

```text
x
↓
operation 1
↓
operation 2
↓
output
```

Tasks:

* [ ] calculate forward values
* [ ] calculate local derivatives
* [ ] multiply derivatives backward
* [ ] verify with numerical derivative

---

# Exercise 011 — Softmax

Tasks:

* [ ] start with scores
* [ ] exponentiate
* [ ] sum
* [ ] normalize
* [ ] verify probabilities sum to 1
* [ ] observe effect of changing scores

---

# Exercise 012 — Cross-Entropy

Tasks:

* [ ] create predicted distribution
* [ ] choose correct target
* [ ] calculate target probability
* [ ] calculate loss
* [ ] compare good vs bad predictions

---

# Exercise 013 — Embedding Similarity

Later:

* [ ] create simple vectors
* [ ] calculate dot product
* [ ] calculate cosine similarity
* [ ] compare similar vs dissimilar vectors

---

# Exercise 014 — Attention Mathematics

Later:

* [ ] create tiny Q/K/V vectors
* [ ] calculate scores
* [ ] apply softmax
* [ ] combine values
* [ ] inspect output

---

# Cross-Track Connections

## Model Learning

Math provides:

```text
Functions
↓
Derivatives
↓
Partial derivatives
↓
Gradient
↓
Chain rule
↓
Backpropagation
```

---

## Tensors & Data

Math provides meaning for:

```text
Scalar
Vector
Matrix
Dot product
Matrix multiplication
```

Tensors & Data provides the computational representation.

---

## Neural Networks

Math provides:

```text
Vectors
↓
Dot product
↓
Matrices
↓
Linear transformations
↓
Activation functions
↓
Derivatives
↓
Backpropagation
```

---

## Tokenizer

The tokenizer itself requires relatively little advanced math.

But its output leads to:

```text
Token IDs
↓
Embedding vectors
```

which connects directly to linear algebra.

---

## Transformers

Math provides:

```text
Vectors
+
Matrices
+
Dot products
+
Softmax
+
Probability
+
Normalization
=
Attention foundations
```

---

# Recommended Learning Order

We should **not** complete all 65 stages sequentially before touching another track.

The practical near-term order is:

## Phase A — Needed Immediately

1. [ ] Functions
2. [ ] Graphs
3. [ ] Slope
4. [ ] Rate of change
5. [ ] Derivatives
6. [ ] Squared-loss derivative

This supports the Model Learning track.

---

## Phase B — Begin in Parallel

7. [ ] Scalars
8. [ ] Vectors
9. [ ] Vector operations
10. [ ] Dot product
11. [ ] Matrices
12. [ ] Shapes
13. [ ] Matrix-vector multiplication
14. [ ] Matrix multiplication

This supports Tensors & Data and unlocks the first neuron.

---

## Phase C — Backpropagation Mathematics

15. [ ] Multiple-variable functions
16. [ ] Partial derivatives
17. [ ] Gradient vector
18. [ ] Composition of functions
19. [ ] Chain rule
20. [ ] Computational graph mathematics
21. [ ] Backpropagation

---

## Phase D — Transformer Mathematics

22. [ ] Exponents
23. [ ] Probability distributions
24. [ ] Softmax
25. [ ] Logarithms
26. [ ] Cross-entropy
27. [ ] Mean / variance / standard deviation
28. [ ] Normalization
29. [ ] Attention mathematics

---

# Current Position

Already encountered through other tracks:

* [x] Variables
* [x] Basic equations
* [x] Arithmetic mean
* [x] Squaring
* [x] Basic derivative intuition
* [x] Basic gradient intuition
* [x] Gradient sign
* [x] Gradient magnitude

Systematic Math track begins here:

```text
Functions
↓
Graphs
↓
Slope
↓
Rate of Change
↓
Derivative
```

while linear algebra begins in parallel:

```text
Scalar
↓
Vector
↓
Dot Product
↓
Matrix
↓
Matrix Multiplication
```

These paths later merge:

```text
Calculus
+
Linear Algebra
↓
Neural Networks
↓
Transformers
```

---

# Immediate Next Topics

Priority order:

1. [ ] Function intuition
2. [ ] Function notation
3. [ ] Graph of a function
4. [ ] Slope
5. [ ] Rate of change
6. [ ] Derivative
7. [ ] Squared-error derivative
8. [ ] Scalar and vector
9. [ ] Dot product
10. [ ] Matrix
11. [ ] Partial derivatives
12. [ ] Chain rule

---

# Completion Goal

This track reaches foundation-level completion when expressions used in AI can be understood conceptually rather than memorized.

For example, eventually seeing something like:

```text
gradient
matrix multiplication
softmax
cross-entropy
```

should immediately suggest:

* what quantities are involved,
* what changes are being measured,
* what the shapes represent,
* why the operation exists,
* and how it affects model learning.

The goal is not to become a mathematician before becoming an AI engineer.

The goal is to make the mathematics inside AI systems understandable rather than mysterious.
