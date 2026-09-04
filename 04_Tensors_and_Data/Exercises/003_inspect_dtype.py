# Exercise 3 — Inspect dtype
import numpy as np

array1 = [1, 2, 3, 4, 5]
array2 = [1.0, 2.0, 3.0, 4.0, 5.0]
array3 = [True, False, True, False, True]
array4 = [1, 2, 3, 4.5, 5]
#print the original lists and their types
print("Original array1:", array1, "Type:", type(array1))
print("Original array2:", array2, "Type:", type(array2))
print("Original array3:", array3, "Type:", type(array3))
print("Original array4:", array4, "Type:", type(array4))

# Convert the lists to NumPy arrays
np_array1 = np.array(array1)
np_array2 = np.array(array2)
np_array3 = np.array(array3)
np_array4 = np.array(array4)

# Print the NumPy array's, data types of the NumPy arrays
print(np_array1)
print(type(np_array1))
print("Data type of np_array1:", np_array1.dtype)
print()  # Print a blank line for better readability

print(np_array2)
print(type(np_array2))
print("Data type of np_array2:", np_array2.dtype)
print()  # Print a blank line for better readability

print(np_array3)
print(type(np_array3))
print("Data type of np_array3:", np_array3.dtype)
print()  # Print a blank line for better readability

print(np_array4)
print(type(np_array4))
print("Data type of np_array4:", np_array4.dtype)

# Now create a NumPy array with a custom data type (dtype) of float32 and print its type and data type.
custom = np.array([1, 2, 3], dtype=np.float32)

print(custom)
print(type(custom))
print(custom.dtype)
# the dtype of the custom array is float32, because we explicitly specified it when creating the array. This allows us to control the precision and memory usage of the array elements.