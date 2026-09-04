# Exercise 5 — Sensor indexing
import numpy as np

# Create a 2D NumPy array representing sensor readings
sensor_readings = np.array([[18, 19, 21, 22],
                            [20, 22, 25, 27],
                            [26, 28, 32, 29]])
print("Sensor readings:")
print(sensor_readings)

# Accessing specific sensor readings using indexing
print("\nAccessing specific sensor readings:")
# Access the reading of second sensor.
print("Reading of second sensor (row 1):", sensor_readings[1])
# Access the third reading of the first sensor.
print("Third reading of first sensor (row 0, column 2):", sensor_readings[0, 2])
# Access the last reading of the last sensor.
print("Last reading of last sensor (row 2, column 3):", sensor_readings[2, 3])
# Access all readings sensor index 1.
print("All readings of sensor index 1:", sensor_readings[1])