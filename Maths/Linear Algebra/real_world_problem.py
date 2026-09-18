import numpy as np

# A is the "recipe" matrix
A = np.array([
  [300, 100],
  [100, 200]
])

# b is stock matrix
b = np.array([11000, 8000])

# solving Ax = B for x
x = np.linalg.solve(A, b)

print(f"Units of Blend A (x) : {x[0]}")
print(f"Units of Blend B (y) : {x[1]}")