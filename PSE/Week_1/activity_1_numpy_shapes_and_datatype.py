# 1- Activity : Create a NumPy array of the first 10 positive integers. Then:
# Print the array.
# Print the shape and data type of the array.
# Multiply each element by 2 and print the result.

import numpy as np

positive_integers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"First ten positive integers: {positive_integers}")

print(f"Shape of the array: {positive_integers.shape}")

print(f"Data type of the array: {positive_integers.dtype}")

print(f"Array multiplied by 2: {positive_integers * 2}")