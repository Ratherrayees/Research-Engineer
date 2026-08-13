# Model Learning — Curriculum & Progress

## Purpose

This track explains how a model learns from data.

The goal is to understand:

* what parameters are,
* how predictions are produced,
* how error becomes loss,
* how gradients describe parameter changes,
* how gradient descent updates parameters,
* how this extends from one weight to many weights,
* how chain rule and backpropagation train neural networks,
* and how modern optimizers automate these updates at scale.

This track should be understood first manually, then connected to NumPy and later PyTorch.

---

# Stage 1 — What Is a Model?

## Concepts

* [x] What is a model?
* [x] Input
* [x] Output
* [x] Prediction
* [x] Target / actual value
* [x] Parameter
* [x] Weight

## Core Mental Model

A model is a mathematical system that receives input and produces an output.

A very simple model can be:

```text
input × weight = prediction
```

The weight controls the model's behavior.

Learning means:

> changing the weight so predictions become closer to the correct targets.

---

# Stage 2 — Error and Loss

## Concepts

* [x] Prediction error
* [x] Prediction − target
* [x] Positive error
* [x] Negative error
* [x] Squared error
* [x] Loss
* [x] Why loss is different from raw error
* [x] Mean loss across multiple examples
* [x] Mean Squared Error intuition

## Core Flow

```text
Prediction
↓
Compare with target
↓
Error
↓
Loss
```

Raw error tells us:

> how far and in which direction the prediction differs from reality.

Loss gives the training process a numerical score representing how badly the model is performing.

---

# Stage 3 — First Learning Loop

## Concepts

* [x] Initial parameter guess
* [x] Make prediction
* [x] Calculate error
* [x] Calculate loss
* [x] Change parameter
* [x] Repeat
* [x] Observe whether loss improves

## Goal

Understand that learning does not mean the model suddenly discovers an answer.

It repeatedly:

```text
predicts
↓
measures mistake
↓
changes parameters
↓
predicts again
```

---

# Stage 4 — Learning Rate

## Concepts

* [x] What is a learning rate?
* [x] Why parameter updates need a step size
* [x] Small learning rate
* [x] Large learning rate
* [x] Overshooting intuition
* [x] Slow convergence intuition

## Mental Model

The gradient determines:

> which direction and how strongly the parameter should move.

The learning rate determines:

> how much of that suggested movement we actually take.

Conceptually:

```text
gradient = direction and sensitivity

learning rate = step-size control
```

---

# Stage 5 — Derivative Intuition

## Status

Basic intuition completed.

Deeper study still required.

## Concepts

* [x] Basic derivative intuition
* [x] Derivative as rate of change
* [x] Relationship between parameter change and loss change
* [ ] Functions in depth
* [ ] Slope
* [ ] Slope of a curve
* [ ] Derivative notation
* [ ] Derivative of simple functions
* [ ] Power rule intuition
* [ ] Derivative of squared loss
* [ ] Derivative with respect to a parameter

## Goal

Understand:

> If I change this parameter slightly, how will the loss change?

This is the mathematical question that allows learning to become systematic.

---

# Stage 6 — Gradient

## Concepts

* [x] Basic gradient intuition
* [x] Gradient sign
* [x] Gradient magnitude
* [x] Gradient becoming smaller near a good parameter
* [x] Gradient calculation for one weight
* [x] Gradient calculation across multiple samples
* [ ] Gradient as derivative of loss with respect to parameter
* [ ] Gradient vector
* [ ] Gradient with many parameters
* [ ] Partial derivatives

## Gradient Sign

Positive gradient:

```text
increasing the parameter increases loss
```

So gradient descent tends to move the parameter downward.

Negative gradient:

```text
increasing the parameter decreases loss
```

So gradient descent tends to move the parameter upward.

Near a good solution:

```text
gradient → smaller
```

because small parameter changes have less effect on loss.

---

# Stage 7 — Gradient Descent

## Concepts

* [x] Gradient descent intuition
* [x] Parameter update
* [x] Learning rate × gradient
* [x] Subtracting the gradient
* [x] Repeating updates
* [x] Convergence intuition
* [x] Gradient descent from scratch
* [x] Gradient descent on multiple training samples
* [ ] Loss landscape
* [ ] Local minima intuition
* [ ] Plateaus
* [ ] Divergence
* [ ] Oscillation
* [ ] Learning-rate sensitivity

## Core Update

Conceptually:

```text
new parameter
=
old parameter
-
learning rate × gradient
```

Why subtract?

Because the gradient points toward increasing loss.

Gradient descent moves in the opposite direction.

---

# Stage 8 — Multiple Training Samples

## Completed

* [x] NumPy arrays
* [x] Multiple input values
* [x] Multiple targets
* [x] Vectorized predictions
* [x] Multiple errors
* [x] Multiple squared losses
* [x] Mean loss
* [x] Mean gradient
* [x] Batch parameter update

## Current Model Behavior

The model can learn a relationship such as:

```text
y = 2x
```

from multiple training examples.

It begins from an incorrect weight and repeatedly reduces mean loss until the learned weight approaches the correct value.

## Important Insight

The model is no longer learning from one observation at a time.

It can evaluate:

```text
many observations
↓
many errors
↓
mean loss
↓
mean gradient
↓
one parameter update
```

---

# Stage 9 — Batch Gradient Descent

## Concepts

* [x] Whole dataset used for one gradient calculation
* [x] Mean gradient across observations
* [ ] Formal definition of batch gradient descent
* [ ] Batch size
* [ ] Full-batch training
* [ ] Benefits
* [ ] Limitations

## Goal

Understand why using the whole dataset produces one overall update direction.

Later compare this with:

* Stochastic Gradient Descent
* Mini-batch Gradient Descent

---

# Stage 10 — Multiple Parameters

## Status

Next major milestone.

## Concepts

* [ ] One input with multiple parameters
* [ ] Multiple inputs
* [ ] Multiple weights
* [ ] Bias
* [ ] Weight vector
* [ ] Input vector
* [ ] Prediction from multiple weighted inputs
* [ ] Separate gradient for each parameter
* [ ] Gradient vector

## Transition

Current simple model:

```text
x × w
```

Next:

```text
x1w1 + x2w2 + x3w3 + bias
```

This is the bridge from:

simple learner

to:

neuron

---

# Stage 11 — Partial Derivatives

## Concepts

* [ ] Function with multiple variables
* [ ] Hold other variables constant
* [ ] Derivative with respect to one parameter
* [ ] One gradient per parameter
* [ ] Partial derivative notation
* [ ] Gradient vector from partial derivatives

## Why This Matters

If a model has:

```text
w1
w2
w3
bias
```

we need to answer separately:

```text
How does loss change if w1 changes?
How does loss change if w2 changes?
How does loss change if w3 changes?
How does loss change if bias changes?
```

Those answers form the gradient vector.

---

# Stage 12 — Gradient Vector

## Concepts

* [ ] Scalar gradient vs gradient vector
* [ ] Parameter vector
* [ ] One derivative per parameter
* [ ] Direction in parameter space
* [ ] Updating multiple parameters simultaneously

## Mental Model

Single parameter:

```text
one parameter
→
one gradient
```

Many parameters:

```text
many parameters
→
many partial derivatives
→
gradient vector
```

---

# Stage 13 — Loss Surface

## Concepts

* [ ] Loss as a function of parameters
* [ ] One-dimensional loss curve
* [ ] Two-dimensional parameter surface
* [ ] High-dimensional loss landscape
* [ ] Valley
* [ ] Minimum
* [ ] Saddle point intuition
* [ ] Plateau intuition

## Goal

Understand gradient descent geometrically.

A real neural network does not have one visible curve.

It has a loss function over potentially millions or billions of parameter dimensions.

---

# Stage 14 — Chain Rule

## Major Prerequisite

Requires deeper derivative understanding.

## Concepts

* [ ] Function inside another function
* [ ] Composition of functions
* [ ] Local derivative
* [ ] Multiplying effects through a chain
* [ ] Chain rule intuition
* [ ] Chain rule notation
* [ ] Chain rule in a learning model

## Example Structure

A model may have:

```text
input
↓
weighted calculation
↓
activation
↓
prediction
↓
loss
```

A weight affects loss indirectly through every intermediate operation.

The chain rule allows us to calculate that total influence.

---

# Stage 15 — Computational Graphs

## Concepts

* [ ] Operation nodes
* [ ] Values flowing forward
* [ ] Dependencies
* [ ] Forward computation
* [ ] Reverse traversal
* [ ] Local derivatives
* [ ] Gradient flow

## Conceptual Example

```text
x ──┐
    × ── prediction ── error ── square ── loss
w ──┘
```

The graph records how the final loss depends on earlier values.

This becomes the foundation of backpropagation and autograd.

---

# Stage 16 — Backpropagation

## Major Milestone

## Concepts

* [ ] What backpropagation actually means
* [ ] Forward pass
* [ ] Loss calculation
* [ ] Backward pass
* [ ] Chain rule through graph
* [ ] Gradient with respect to each parameter
* [ ] Reusing intermediate derivatives
* [ ] Backprop through one neuron
* [ ] Backprop through one layer
* [ ] Backprop through multiple layers

## Mental Model

Forward:

```text
inputs
↓
predictions
↓
loss
```

Backward:

```text
loss
↓
how much each operation contributed
↓
how much each parameter contributed
↓
gradients
```

Then:

```text
gradients
↓
optimizer
↓
updated parameters
```

---

# Stage 17 — Automatic Differentiation

## Concepts

* [ ] Why manual derivatives do not scale
* [ ] Computational graph recording
* [ ] Reverse-mode automatic differentiation
* [ ] Autograd intuition
* [ ] Difference between symbolic differentiation and autodiff
* [ ] Why backpropagation is efficient for neural networks

## Unlock

PyTorch:

```text
requires_grad
.backward()
.grad
```

should only become convenient automation after the manual process is understood.

---

# Stage 18 — Gradient Descent Variants

## Full-Batch Gradient Descent

* [x] Basic implementation
* [ ] Formal understanding

Uses:

```text
entire dataset
→
one gradient
→
one update
```

---

## Stochastic Gradient Descent

* [ ] One training example per update
* [ ] Noisy gradients
* [ ] Faster updates
* [ ] Advantages
* [ ] Disadvantages

---

## Mini-Batch Gradient Descent

* [ ] Small subset of dataset per update
* [ ] Batch size
* [ ] Why modern neural networks commonly use mini-batches
* [ ] GPU efficiency
* [ ] Gradient noise

Conceptually:

```text
dataset
↓
small batches
↓
gradient for each batch
↓
parameter update
```

---

# Stage 19 — Epochs, Steps, and Iterations

## Concepts

* [ ] Epoch
* [ ] Batch
* [ ] Training step
* [ ] Iteration
* [ ] Relationship between dataset size and batch size
* [ ] Multiple epochs

## Goal

Replace arbitrary `while` loops with structured training loops.

Conceptually:

```text
Epoch 1
    Batch 1
    Batch 2
    Batch 3

Epoch 2
    Batch 1
    Batch 2
    Batch 3
```

---

# Stage 20 — Optimizers

## Gradient Descent

* [x] Basic parameter update

## SGD

* [ ] SGD optimizer

## Momentum

* [ ] Why gradients can oscillate
* [ ] Velocity intuition
* [ ] Accumulating direction
* [ ] Momentum update

## RMSProp

* [ ] Gradient magnitude tracking
* [ ] Adaptive step sizes

## Adam

* [ ] Momentum component
* [ ] Adaptive learning rates
* [ ] First moment
* [ ] Second moment
* [ ] Why Adam is widely used
* [ ] Adam trade-offs

---

# Stage 21 — Training Stability

## Learning Rate

* [ ] Too small
* [ ] Too large
* [ ] Stable range
* [ ] Learning-rate schedules
* [ ] Warmup

## Gradients

* [ ] Vanishing gradients
* [ ] Exploding gradients
* [ ] Gradient clipping

## Parameters

* [ ] Initialization
* [ ] Poor initialization
* [ ] Xavier initialization intuition
* [ ] He initialization intuition

---

# Stage 22 — Generalization

## Concepts

* [ ] Training loss
* [ ] Validation loss
* [ ] Training accuracy
* [ ] Generalization
* [ ] Underfitting
* [ ] Overfitting
* [ ] Memorization
* [ ] Model capacity

## Goal

Understand:

> Low training loss does not automatically mean the model learned something useful.

A model must also perform well on data it did not train on.

---

# Stage 23 — Regularization

## Topics

* [ ] Weight decay
* [ ] L1 intuition
* [ ] L2 intuition
* [ ] Dropout
* [ ] Early stopping
* [ ] Data augmentation concept
* [ ] Regularization vs optimization

---

# Stage 24 — From Learning Model to First Neuron

## Prerequisites

Before entering the Neural Network track:

* [ ] Multiple weights
* [ ] Vectors
* [ ] Dot product
* [ ] Bias
* [ ] Partial derivatives
* [ ] Gradient vector
* [ ] Chain rule basics

## Transition

Current:

```text
prediction = input × weight
```

Next:

```text
prediction =
input vector · weight vector
+
bias
```

Then:

```text
weighted sum
↓
activation
↓
neuron output
```

---

# Stage 25 — Connection to PyTorch

After backpropagation is understood manually:

Manual:

```text
prediction
↓
loss
↓
gradient calculation
↓
parameter update
```

PyTorch:

```text
forward
↓
loss
↓
backward
↓
optimizer step
```

Topics to unlock:

* [ ] `requires_grad`
* [ ] computational graph
* [ ] `.backward()`
* [ ] `.grad`
* [ ] `zero_grad()`
* [ ] optimizer
* [ ] `optimizer.step()`

---

# Optional Deep-Dive Topics

These are useful but should not block progress.

## Calculus

* [ ] Numerical derivative approximation
* [ ] Finite differences
* [ ] Jacobian intuition
* [ ] Hessian intuition

## Optimization

* [ ] Convex vs non-convex optimization
* [ ] Saddle points
* [ ] Momentum geometry
* [ ] Adaptive optimizers
* [ ] Second-order methods overview

## Numerical Stability

* [ ] Floating-point precision
* [ ] Gradient precision
* [ ] Overflow
* [ ] Underflow
* [ ] Mixed precision intuition

---

# Practical Exercises

## Completed

### Exercise 001 — Basic Model

* [x] Input
* [x] Weight
* [x] Prediction

### Exercise 002 — First Learner

* [x] Error
* [x] Loss
* [x] Repeated parameter update

### Exercise 003 — Gradient Descent Learner

* [x] NumPy dataset
* [x] Multiple samples
* [x] Mean Squared Error
* [x] Gradient
* [x] Learning rate
* [x] Gradient descent
* [x] Weight convergence

---

# Planned Exercises

## Exercise 004 — Multiple Weights

Build a learner with:

* [ ] multiple inputs
* [ ] multiple weights
* [ ] one prediction
* [ ] separate gradients

---

## Exercise 005 — First Neuron

Build:

* [ ] weighted sum
* [ ] bias
* [ ] activation
* [ ] prediction

---

## Exercise 006 — Manual Backpropagation

Build:

* [ ] forward pass
* [ ] loss
* [ ] computational graph
* [ ] chain rule
* [ ] gradients
* [ ] parameter update

---

## Exercise 007 — Mini-Batch Training

Build:

* [ ] dataset
* [ ] batch size
* [ ] epoch loop
* [ ] mini-batch gradient descent

---

## Exercise 008 — Optimizer Comparison

Compare:

* [ ] Gradient Descent
* [ ] SGD
* [ ] Momentum
* [ ] Adam

Track:

* [ ] convergence speed
* [ ] loss behavior
* [ ] stability

---

# Current Position

Completed path:

```text
Model
↓
Parameter
↓
Prediction
↓
Error
↓
Loss
↓
Learning Rate
↓
Gradient
↓
Gradient Descent
↓
Multiple Training Samples
↓
Mean Loss
↓
Batch Gradient
```

Current transition:

```text
Single Weight
↓
Multiple Weights
↓
Gradient Vector
↓
Chain Rule
↓
Backpropagation
↓
First Neuron
```

---

# Immediate Next Topics

Priority order:

1. [ ] Multiple parameters / weights
2. [ ] Vector representation of parameters
3. [ ] Derivatives in deeper detail
4. [ ] Partial derivatives
5. [ ] Gradient vector
6. [ ] Chain rule
7. [ ] Computational graphs
8. [ ] Backpropagation
9. [ ] First neuron

---

# Completion Goal

This track is complete at the foundation level when the following statement is fully understandable:

> A model makes predictions using parameters. A loss function measures prediction quality. Backpropagation uses the chain rule to efficiently calculate how every trainable parameter contributed to that loss. An optimizer then uses those gradients to update the parameters so future predictions improve.

At that point, neural-network training should no longer feel like a hidden process.
