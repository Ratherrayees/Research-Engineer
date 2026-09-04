# Exercise 2 — Multi-axis slicing

import numpy as np
x = np.zeros((32, 100, 256))

# 1. First 8 samples. x[0:8] or x[:8] are equivalent.
x[:8]
# Output shape: (8, 100, 256)

# 2. Samples 8–15.
x[8:16]
# Output shape: (8, 100, 256)

# 3. First 20 time steps from every sample.
x[:, :20]
# Output shape: (32, 20, 256)

# 4. Features 50–99 from every time step.
x[:, :, 50:100]
# Output shape: (32, 100, 50)

# 5. Samples 5–9, time steps 20–39, features 100–149.
x[5:10, 20:40, 100:150]
# Output shape: (5, 20, 50)

# Print the output shapes to verify
print("Output shape for first 8 samples:", x[:8].shape)
print("Output shape for samples 8–15:", x[8:16].shape)
print("Output shape for first 20 time steps:", x[:, :20].shape)
print("Output shape for features 50–99:", x[:, :, 50:100].shape)
print("Output shape for samples 5–9, time steps 20–39, features 100–149:", x[5:10, 20:40, 100:150].shape)