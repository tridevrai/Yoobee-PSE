# Activity Week1 - using NumPy
# Tasks:
# Print the average temperature for a week.
# Find the highest and lowest temperature recorded.
# Convert all temperatures to Fahrenheit and print the result.
# (Formula: F = C * 9/5 + 32)
# Identify the days (by index) where the temperature was above 20°C.

import numpy as np

temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

#printing all the temperatures as is.
print(temperatures)

#printing the average temperature
print(np.mean(temperatures))

#printing the maximum temperature
print(np.max(temperatures))

#printing the minimum temperature
print(np.min(temperatures))

#converting to fahrenheit
temperatures_in_fahrenheit = ((temperatures * 9)/5) + 32

#printing the temperatures in fahrenheit
print(temperatures_in_fahrenheit)

#print the indexes of the temperatures that are greater than 20
print(np.nonzero(temperatures > 20))


