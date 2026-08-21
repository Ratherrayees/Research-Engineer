"""
Tensors & Data — Day 2 Exercises
=================================

Focus:
- element-wise operations
- reductions
- broadcasting
- reshape and flatten
- squeeze / expand_dims
- transpose
- axis reordering with NumPy

RULE FOR THIS FILE:
Predict the output shape before running each operation.
Do the TODOs manually. No finished solutions are included.
"""

import numpy as np


# ================================================================
# EXERCISE 1 — ELEMENT-WISE OPERATIONS
# ================================================================

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

# Perform and print:
# - x + y
# - y - x
# - x * y
# - y / x
# - x ** 2
#
# In comments, explain why these are called element-wise operations.

# TODO


# ================================================================
# EXERCISE 2 — REDUCTIONS
# ================================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

# Calculate:
# - total sum
# - mean of all values
# - minimum
# - maximum
# - sum along axis=0
# - sum along axis=1
# - mean along axis=0
# - mean along axis=1
#
# Predict the output shape of every axis-based reduction.

# TODO


# ================================================================
# EXERCISE 3 — SCALAR BROADCASTING
# ================================================================

vector = np.array([2, 4, 6, 8])

# Add 5 to the vector.
# Multiply the vector by 3.
#
# Explain in comments:
# - Why can a scalar interact with every element of the vector?
# - Did NumPy literally create a second [5, 5, 5, 5] array first?

# TODO


# ================================================================
# EXERCISE 4 — VECTOR + MATRIX BROADCASTING
# ================================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

bias = np.array([1, 2, 3])

# Add the bias vector to the matrix.
#
# BEFORE running:
# - matrix shape = ?
# - bias shape = ?
# - output shape = ?
#
# Then explain why this is similar to how a neural-network bias can be
# added across many samples.

# TODO


# ================================================================
# EXERCISE 5 — BROADCASTING ERROR
# ================================================================

bad_bias = np.array([1, 2])

# Predict whether this will work:
#
# matrix + bad_bias
#
# Do NOT remove the prediction comment after testing.
# If it fails, explain which dimensions are incompatible.

# TODO: test it intentionally


# ================================================================
# EXERCISE 6 — RESHAPE
# ================================================================

x = np.arange(24)

# Starting shape should be (24,).
# Reshape the same data into each VALID shape below:
#
# (2, 12)
# (3, 8)
# (4, 6)
# (2, 3, 4)
#
# For each one:
# - predict ndim
# - predict shape
# - confirm size stays 24

# TODO


# ================================================================
# EXERCISE 7 — INVALID RESHAPE
# ================================================================

# Predict whether these shapes are possible for 24 values:
#
# (5, 5)
# (2, 2, 5)
# (6, 4)
#
# Test the invalid ones inside try/except blocks so the rest of the file
# can continue running.
#
# Explain the rule that determines reshape validity.

# TODO


# ================================================================
# EXERCISE 8 — FLATTEN
# ================================================================

matrix = np.arange(12).reshape(3, 4)

# Flatten this matrix back into one dimension.
#
# Predict:
# - output shape
# - ndim
# - size
#
# Then explain what structural information was lost.

# TODO


# ================================================================
# EXERCISE 9 — ADDING SIZE-1 AXES
# ================================================================

vector = np.array([10, 20, 30, 40, 50])

# Use np.expand_dims() to create:
#
# (1, 5)
#
# and:
#
# (5, 1)
#
# Explain what axis=0 and axis=1 mean in each case.

# TODO


# ================================================================
# EXERCISE 10 — SQUEEZE
# ================================================================

x = np.arange(5).reshape(1, 5, 1)

# Starting shape:
# (1, 5, 1)
#
# Use np.squeeze() and predict the output shape first.
#
# Then try squeezing only axis 0.
# Then try squeezing only axis 2.
#
# Explain why an axis with size greater than 1 cannot be squeezed away.

# TODO


# ================================================================
# EXERCISE 11 — TRANSPOSE A MATRIX
# ================================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

# Transpose this matrix.
#
# Predict:
# original shape = ?
# transposed shape = ?
#
# Print both the original and transposed matrices and explain what
# happened to rows and columns.

# TODO


# ================================================================
# EXERCISE 12 — REORDER AXES IN 3D
# ================================================================

x = np.arange(24).reshape(2, 3, 4)

# Treat the axes as:
#
# axis 0 = batch
# axis 1 = sequence
# axis 2 = features
#
# Rearrange the axes to get these shapes:
#
# (3, 2, 4)  -> sequence, batch, features
# (2, 4, 3)  -> batch, features, sequence
#
# Use np.transpose() with an explicit axis order.
#
# BEFORE running, write the required axis order for each transformation.

# TODO


# ================================================================
# FINAL REFLECTION — WRITE IN YOUR OWN WORDS
# ================================================================

# 1. Element-wise multiplication and matrix multiplication are not the
#    same operation. What does element-wise multiplication do?
#
# 2. What is broadcasting trying to save us from doing manually?
#
# 3. What must remain unchanged during reshape?
#
# 4. What is the difference between adding/removing a size-1 axis and
#    reshaping data arbitrarily?
#
# 5. What is the difference between transposing a 2D matrix and
#    explicitly reordering the axes of a 3D array?
