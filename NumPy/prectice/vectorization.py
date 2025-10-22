import numpy as np

# without using vectorization

data = [1,2,3,4,5]
result = []

for i in data:
  result.append(i * 2)
  
print(result)


# using vectorization

data = np.array([1,2,3,4,5])
print(data * 2)