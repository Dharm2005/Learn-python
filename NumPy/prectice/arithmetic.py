import numpy as np

# scalar arithmetic

a1 = np.array([1,3,5])

print(a1 + 1)
print(a1 - 1)
print(a1 * 2)
print(a1 / 2)
print(a1 % 2)
print(a1 ** 3)



# vectorized math functions

a2 = np.array([2.4, 5.6, 7.01])

print(np.sqrt(a2))
print(np.round(a2))
print(np.pi)



# Element-wise arithmetic 

a3 = np.array([1,2,3])
a4 = np.array([5,7,9])

print(a3 + a4)
print(a3 - a4)
print(a3 * a4)
print(a3 / a4)


# comparison operator

runs = np.array([11,59,17,0,59,100,36])

print(runs == 100)

runs[runs < 50] = 0
print(runs)