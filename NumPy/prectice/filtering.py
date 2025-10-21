import numpy as np

ages = np.array([[21,17,20,50],
                 [37,65,27,10]])

# Boolean indexing
teenagers = ages[ages <= 18]
adult = ages[(ages >= 18) & (ages <= 50)]
print(teenagers)
print(adult)


# using where function
adult = np.where(ages > 18, ages, 0) # slower than boolean indexing
print(adult)