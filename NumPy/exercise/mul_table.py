import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
user_inp = int(input("Enter Number: "))

inp_array = np.array([user_inp])

print(arr1 * inp_array)