import numpy as np

# shape (1, 4) (4, 1)

a1 = np.array([[1,2,3,4]])
a2 = np.array([[1],[2],[3],[4]])

print(a1.shape)
print(a2.shape)

print(a1 * a2)



# shape (2, 2) (2, 2)

a1 = np.array([[1,2],[3,4]])
a2 = np.array([[5,6],[7,8]])

print(a1.shape)
print(a2.shape)

print(a1 + a2)


# shape (2, 2) (2, 1)

a1 = np.array([[1,2],[3,4]])
a2 = np.array([[2],[4]])

print(a1.shape)
print(a2.shape)

print(a1 + a2)