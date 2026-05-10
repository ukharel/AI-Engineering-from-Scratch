import numpy as np

# A matrix representing 3 sensors
# Sensor 3 is just (Sensor 1 + Sensor 2). It's a 'Fake' feature.
sensor_data = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 9.0],
    [7.0, 8.0, 15.0]
])

# Calculate Rank
rank = np.linalg.matrix_rank(sensor_data)

print(f"Matrix Shape: {sensor_data.shape}")
print(f"Mathematical Rank: {rank}")

if rank < sensor_data.shape[1]:
    print("This matrix is 'Rank Deficient'. One of your features is a ghost.")