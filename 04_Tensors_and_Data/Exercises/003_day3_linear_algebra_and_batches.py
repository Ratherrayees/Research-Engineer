"""
Tensors & Data — Day 3 Exercises
=================================

Focus:
- dot product
- matrix-vector multiplication
- matrix multiplication
- shape compatibility
- sample / feature / target structure
- batches and batch dimensions
- language-model style sequence shapes

RULE FOR THIS FILE:
Always write the expected shape BEFORE running an operation.
Do the TODOs manually. No full solutions are provided.
"""

import numpy as np


# ================================================================
# EXERCISE 1 — MANUAL DOT PRODUCT
# ================================================================

x = np.array([2.0, 3.0, 4.0])
w = np.array([0.5, -1.0, 2.0])

# First calculate the dot product MANUALLY using:
#
# x1*w1 + x2*w2 + x3*w3
#
# Then calculate the same result with NumPy.
#
# Questions to answer in comments:
# - What shape does each input vector have?
# - Why is the final dot-product result a scalar?
# - Why is this operation useful for a neuron?

# TODO: manual calculation

# TODO: NumPy dot product


# ================================================================
# EXERCISE 2 — MULTIPLE INPUT FEATURES
# ================================================================

features = np.array([1.5, 2.0, -3.0])
weights = np.array([0.2, 0.7, -0.4])
bias = 0.5

# Compute a simple prediction using:
#
# input vector · weight vector + bias
#
# Do the multiplication manually first, then with NumPy.
#
# Explain why three input features require three corresponding weights.

# TODO


# ================================================================
# EXERCISE 3 — MATRIX × VECTOR
# ================================================================

samples = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
    [10.0, 11.0, 12.0],
])

weights = np.array([0.1, 0.2, 0.3])

# Treat:
# - each ROW as one sample
# - each COLUMN as one feature
#
# Predict:
# samples shape = ?
# weights shape = ?
# output shape = ?
#
# Multiply the matrix by the weight vector using @.
#
# Explain why the result contains one prediction per sample.

# TODO


# ================================================================
# EXERCISE 4 — MATRIX MULTIPLICATION SHAPE RULE
# ================================================================

A = np.arange(12).reshape(3, 4)
B = np.arange(20).reshape(4, 5)

# BEFORE running:
#
# A shape = ?
# B shape = ?
# Do the inner dimensions match?
# Expected output shape = ?
#
# Then perform A @ B.
#
# Write the general rule in comments:
#
# (m, n) @ (n, p) -> (?, ?)

# TODO


# ================================================================
# EXERCISE 5 — INVALID MATRIX MULTIPLICATION
# ================================================================

C = np.arange(15).reshape(3, 5)
D = np.arange(8).reshape(4, 2)

# Predict whether C @ D is valid.
#
# If not, explain EXACTLY which dimensions fail to match.
# Test it using try/except so the rest of the file still runs.

# TODO


# ================================================================
# EXERCISE 6 — ELEMENT-WISE VS MATRIX MULTIPLICATION
# ================================================================

A = np.array([
    [1, 2],
    [3, 4],
])

B = np.array([
    [5, 6],
    [7, 8],
])

# Compute BOTH:
#
# A * B
# A @ B
#
# Print the results side by side.
#
# Explain in comments why they produce different values even though the
# input shapes are identical.

# TODO


# ================================================================
# EXERCISE 7 — SAMPLE, FEATURE, TARGET
# ================================================================

# Imagine a tiny house-price dataset.
# Each sample has three features:
#
# [area, bedrooms, age]
#
# Create a feature matrix X containing FIVE samples.
# Choose your own realistic numerical values.
#
# Create a target vector y containing FIVE corresponding prices.
#
# Print:
# X.shape
# y.shape
#
# Explain:
# - What does one row of X represent?
# - What does one column represent?
# - Why does y have one value per sample?

# TODO


# ================================================================
# EXERCISE 8 — MANUAL BATCHING
# ================================================================

# Using your X dataset from Exercise 7:
#
# Select the first TWO samples as batch_1.
# Select the next TWO samples as batch_2.
# Select the final sample as batch_3.
#
# Do this with slicing.
#
# Predict and print the shape of every batch.
#
# Explain why the final batch can be smaller than the requested batch size.

# TODO


# ================================================================
# EXERCISE 9 — SINGLE SAMPLE VS BATCH
# ================================================================

sample = np.array([1200.0, 3.0, 10.0])

# Starting shape should be:
# (3,)
#
# Convert it into a batch containing ONE sample so that the shape becomes:
# (1, 3)
#
# Use np.expand_dims() rather than manually rebuilding the data.
#
# Explain what the new axis represents.

# TODO


# ================================================================
# EXERCISE 10 — TOKEN-ID BATCH SHAPE
# ================================================================

# Imagine a tokenizer produced these padded token-ID sequences:
#
# sentence 1: [5, 9, 2, 0, 0]
# sentence 2: [7, 4, 8, 3, 0]
# sentence 3: [1, 6, 2, 9, 4]
#
# Create one NumPy array containing all three sequences.
#
# Predict the shape BEFORE running.
#
# Interpret each axis:
# axis 0 = ?
# axis 1 = ?

# TODO


# ================================================================
# EXERCISE 11 — EMBEDDING-SHAPE SIMULATION
# ================================================================

# Suppose the token-ID batch from Exercise 10 has shape:
#
# (batch, sequence)
#
# and every token will eventually be represented by an embedding with
# FOUR numerical features.
#
# Without using a real embedding layer yet, create a dummy NumPy array of
# zeros with the shape you expect AFTER embeddings are looked up.
#
# Explain what EACH axis represents.
#
# Hint: think [batch, sequence, embedding_features].

# TODO


# ================================================================
# EXERCISE 12 — SHAPE REASONING CHALLENGE
# ================================================================

# Do NOT run code for this section until you have written every answer.
#
# For each operation, decide whether it is valid and give the output shape:
#
# A. (8, 64) @ (64, 20)
# B. (10, 32) @ (31, 5)
# C. (128, 768) @ (768, 3072)
# D. (32, 10) @ (10, 1)
# E. (20, 64) @ (64, 8)
#
# Then create dummy NumPy arrays with these shapes and verify your answers.

# TODO


# ================================================================
# FINAL REFLECTION — WRITE IN YOUR OWN WORDS
# ================================================================

# 1. What does a dot product actually compute?
# 2. Why can one matrix-vector multiplication produce predictions for many
#    samples at once?
# 3. What do the inner dimensions mean in matrix multiplication?
# 4. What is the difference between a single sample and a batch?
# 5. In a feature matrix shaped (100, 8), what do 100 and 8 represent?
# 6. In token data shaped (32, 128), what might each axis represent?
# 7. After embedding lookup gives shape (32, 128, 768), what does the new
#    768 axis represent?
# 8. Explain why shape reasoning will matter when we move to multiple
#    weights, neural networks, embeddings, and Transformers.
