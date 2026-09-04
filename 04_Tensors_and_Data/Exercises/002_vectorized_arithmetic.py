# Exercise 2 — Vectorized price adjustment
# Using NumPy: Increase every price by 10%. Subtract a flat discount of 20. Print the final prices. Do not use a Python for loop.

import numpy as np

#Product prices:
prices = [120, 250, 80, 450, 300]

# Convert the list to a NumPy array
prices_np = np.array(prices)

# For 10% increase, multiply the prices by 1.10
increased_prices = prices_np * 1.10

# Now subtract a flat discount of 20 from each price not the increased prices.
discounted_prices = prices_np - 20

#now for the final prices after both operations, first increase by 10% and then subtract 20.
final_prices = prices_np * 1.10 - 20

# Print the prices
print("Original prices:", prices_np)
print("Prices after 10% increase:", increased_prices)
print("Prices after flat discount of 20:", discounted_prices)
print("Final prices after 10% increase and flat discount of 20:", final_prices)