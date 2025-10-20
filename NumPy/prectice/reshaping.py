import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newArray = array.reshape(2,2,3)
print(newArray)

a1 = newArray.reshape(-1)
print(a1)

# converting from 2-rows , 3-cols to 3-rows , 3-cols

np1 = np.array([[1,2,3],[4,5,6]])
print(np1)

np2 = np1.reshape(3,2)
print(np2)