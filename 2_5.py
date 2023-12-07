import numpy as np

data = np.array([1, 2, 2, 3, 4, 6, 8, 9, 10, 100])

mean = np.mean(data)
std_dev = np.std(data)

# Set a threshold (e.g., 2 standard deviations)
threshold = 2

# Identify outliers
outliers = (data - mean) / std_dev > threshold

print("Outliers:", data[outliers])
