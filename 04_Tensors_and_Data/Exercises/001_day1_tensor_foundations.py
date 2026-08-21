"""
Tensors & Data — Day 1 Exercises
=================================

Focus:
- Python lists vs NumPy arrays
- scalar, vector, matrix, higher-dimensional array
- shape, ndim, size, dtype
- indexing and slicing
- axis-aware thinking

RULE FOR THIS FILE:
Before running an operation that changes/selects data, write your predicted
shape/result in a comment first. If your prediction is wrong, keep the old
comment and add what you misunderstood.

Do the TODOs manually. There are intentionally no finished solutions here.
"""

import numpy as np


# ================================================================
# EXERCISE 1 — PYTHON LIST VS NUMPY ARRAY
# ================================================================

# Create the same numerical values twice:
#   1. as a normal Python list
#   2. as a NumPy array
#
# Use the values: 2, 4, 6, 8
#
# Then multiply both objects by 2 and observe what happens.
#
# Questions to answer in comments:
# - What does `python_list * 2` do?
# - What does `numpy_array * 2` do?
# - Why is NumPy behavior more useful for numerical AI work?

# TODO: create the Python list

# TODO: create the NumPy array

# TODO: multiply each by 2 and print the results


# ================================================================
# EXERCISE 2 — SCALAR, VECTOR, MATRIX
# ================================================================

# Create these NumPy objects yourself:
#
# scalar:
#   one numerical value
#
# vector:
#   [10, 20, 30, 40]
#
# matrix:
#   [
#       [1, 2, 3],
#       [4, 5, 6]
#   ]
#
# For EACH object, print:
# - the object
# - .shape
# - .ndim
# - .size
# - .dtype
#
# Before running, predict all five properties in comments.

# TODO: scalar

# TODO: vector

# TODO: matrix


# ================================================================
# EXERCISE 3 — BUILD A 3D ARRAY
# ================================================================

# Create a NumPy array containing TWO matrices.
# Each matrix should contain TWO rows and THREE columns.
#
# Use any values you like.
#
# BEFORE running:
# - Predict the shape.
# - Predict ndim.
# - Predict total size.
# - Explain what each position in the shape means.

# TODO: create the 3D array

# TODO: print shape, ndim, and size


# ================================================================
# EXERCISE 4 — VECTOR INDEXING
# ================================================================

numbers = np.array([10, 20, 30, 40, 50, 60])

# Retrieve and print:
# 1. the first element
# 2. the fourth element
# 3. the last element using a negative index
# 4. the second-last element using a negative index
#
# Do not rewrite the array.

# TODO


# ================================================================
# EXERCISE 5 — MATRIX INDEXING
# ================================================================

matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
])

# Retrieve ONE value at a time using row/column indexing:
# - 10
# - 70
# - 100
# - 120
#
# For every lookup, write the row index and column index in a comment first.

# TODO


# ================================================================
# EXERCISE 6 — VECTOR SLICING
# ================================================================

values = np.array([5, 10, 15, 20, 25, 30, 35, 40])

# Use slicing to produce each result WITHOUT manually creating new arrays:
#
# A.  [10, 15, 20]
# B.  the first four values
# C.  everything from 20 onward
# D.  every second value
# E.  the vector in reverse order
#
# Before each slice, explain what start / stop / step you intend to use.

# TODO


# ================================================================
# EXERCISE 7 — MATRIX SLICING
# ================================================================

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
])

# Without manually constructing the results, slice out:
#
# A. the first row
# B. the last column
# C. the middle 2x2 block containing 6, 7, 10, 11
# D. the first two rows and last two columns
#
# Predict the SHAPE of every result before running it.

# TODO


# ================================================================
# EXERCISE 8 — AXIS INTUITION
# ================================================================

scores = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

# We have already used np.mean() in Model Learning.
# Now explore what an axis changes.
#
# Calculate and print:
# - mean of ALL values
# - mean with axis=0
# - mean with axis=1
#
# BEFORE running, answer in comments:
# - What do you think axis=0 will combine?
# - What do you think axis=1 will combine?
# - What shape do you expect from each reduction?

# TODO


# ================================================================
# FINAL REFLECTION — WRITE IN YOUR OWN WORDS
# ================================================================

# Answer these in comments:
#
# 1. What is the difference between shape, ndim, and size?
# 2. Why is a vector with four values still only 1D?
# 3. What does an axis actually represent?
# 4. Why is indexing different from slicing?
# 5. Why are NumPy arrays more suitable than normal lists for the
#    numerical operations we used in Model Learning?
