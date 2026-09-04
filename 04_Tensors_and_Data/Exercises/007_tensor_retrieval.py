# Exercise 3 — Orchard tensor
# 10 trees, 20 branches per tree, 30 apples per branch

import numpy as np

# Create 6000 sequential values and reshape them into:
# axis 0 = trees
# axis 1 = branches
# axis 2 = apples
orchard_tensor = np.arange(6000).reshape(10, 20, 30)
# np.arange() is a NumPy function that creates an array of sequential values. in our case from 0 to 5999.

print("Orchard shape:", orchard_tensor.shape)


# 1. One entire tree
# Tree 1 = index 0
# Predicted shape: (20, 30)
tree = orchard_tensor[0]
print("\nTree 1 shape:", tree.shape)
print(tree)


# 2. One branch from one tree
# Branch 5 of Tree 3
# Human Tree 3   -> index 2
# Human Branch 5 -> index 4
# Predicted shape: (30,)
branch = orchard_tensor[2, 4]
print("\nBranch 5 of Tree 3 shape:", branch.shape)
print(branch)


# 3. One apple
# Pick Tree 1, Branch 2, Apple 3
# Human numbering -> indexes [0, 1, 2]
# Predicted shape: () because this is one scalar value
apple = orchard_tensor[0, 1, 2]
print("\nOne apple:")
print(apple)
print("Apple shape:", apple.shape)


# 4. Trees 2:6
# IMPORTANT:
# 2:6 is already Python slice notation.
# It selects indexes 2, 3, 4, 5.
# Predicted shape: (4, 20, 30)
trees = orchard_tensor[2:6]
print("\nTrees 2:6 shape:", trees.shape)
print(trees)


# 5. Trees 2:6, branches 5:10, apples 10:20
#
# trees    -> 2:6   -> 4 trees
# branches -> 5:10  -> 5 branches
# apples   -> 10:20 -> 10 apples
#
# Predicted shape: (4, 5, 10)
selection = orchard_tensor[2:6, 5:10, 10:20]

print("\nSelected section shape:", selection.shape)
print(selection)