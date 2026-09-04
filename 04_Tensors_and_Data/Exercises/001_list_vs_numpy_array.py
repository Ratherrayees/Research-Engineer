# Exercise 1 — Python list vs NumPy array
import numpy as np

values = [10, 20, 30, 40]

# Print the results
print("Original list:", values)

# Addition
# Print the results regular python addition

print("After addition (Python list):", [x + 5 for x in values])

# multiplication
# Print the results for multiplication using Python list; here *2 doesnt mean multiplication it means repeat the list twice.
values_list_mult = values * 2
print("After multiplication (Python list):", values_list_mult)

# now print the results for multiplication for every element in the list using a loop
result = []
for x in values:
    result.append(x * 2)
print("After multiplication (Python list using loop):", result)

# division
# Print the results for division using Python list
values_list_div = [x / 2 for x in values]
print("After division (Python list):", values_list_div)

# subtraction
# Print the results for subtraction using Python list
values_list_sub = [x - 3 for x in values]
print("After subtraction (Python list):", values_list_sub)

# now convert the Python list to a NumPy array and print the results.
values_np = np.array(values)
print("Converted to NumPy array:", values_np)
print("Addition with NumPy array:", values_np + 5)
print("Multiplication with NumPy array:", values_np * 2)
print("Division with NumPy array:", values_np / 2)
print("Subtraction with NumPy array:", values_np - 3)

# Now print the type of the original list and the NumPy array, as well as the data type of the NumPy array.
print("Python type:", type(values))
print("NumPy type:", type(values_np))
print("NumPy dtype:", values_np.dtype)