import numpy as np

array = np.array([
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
])

# slicing -> array[start:end:step]  |  [] -> subscript operator

# ROW selection
print(array[-1:-5:-2])

# COLUMN selection
print(array[:, 2])
print(array[:, 1::2])

# BOTH
print(array[2:4,1:3])