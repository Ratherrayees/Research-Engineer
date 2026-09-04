import numpy as np

# Create a dummy 3D tensor.
# We don't care about the actual values yet,
# only the structure/shape. np.zeros is a inbuilt numpy function that creates an array of zeros with the specified shape.
# by default, np.zeros creates an array of floats, but you can specify a different data type using the dtype parameter.
# also it creats it in a row-major order also called C-order.
x = np.zeros((24, 60, 128))

print(x.shape)

# Select one recording.
print(x[3].shape)
# This the selected recording [3] has 60 time steps and 128 features, so the shape of the selected recording is (60, 128).

# Select one time step from one recording.
print(x[3, 10].shape)
# This the selected time step [10] from the selected recording [3] has 128 features, so the shape of the selected time step is (128,).

# Select one specific feature value.
print(x[3, 10, 50].shape)
# This the selected feature value [50] from the selected time step [10] from the selected recording [3] is a scalar, so the shape of the selected feature value is ().

print(type(x))
print(type(x[3]))
print(type(x[3, 10]))
print(type(x[3, 10, 50]))