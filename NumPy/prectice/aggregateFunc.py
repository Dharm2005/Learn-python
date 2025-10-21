import numpy as np

a = np.array([[56,65,74,75], [76,77,90,95]])

print(np.sum(a))

print(np.sum(a, axis = 1))

print(np.mean(a))
# print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.min(a))
print(np.max(a))
print(np.argmin(a))
print(np.argmax(a))
