import numpy as np

rng = np.random.default_rng(seed=1) # using seed we will get same result every time

print(rng.integers(1,7))

# keyword argujments
print(rng.integers(low=1,high=7))

# setting size
print(rng.integers(low=1, high=11, size=4))

# changing dimension
print(rng.integers(low=1, high=15, size=(3,2)))




# Floating number
print(np.random.uniform(-1,1,size=(3,1)))


# Suffle array
arr = np.array([1,2,3,4,5])

rng.shuffle(arr)
print(arr)

# Choice

array = np.array(['a','b','c','d','e'])
choice = rng.choice(array)

print(choice)

choices = rng.choice(array, size=(3,1))
print(choices)