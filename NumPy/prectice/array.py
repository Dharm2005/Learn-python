import numpy as np

# zero dimensional array

z_array = np.array('a')
# print(z_array.ndim)

# one dimensional array

o_array = np.array([1, 2])
# print(o_array.ndim)

# two dimensional array

t_array = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
# print(t_array.ndim)


# three dimensional array

th_array = np.array([[[1,2,3], [4,5,6], [7,8,9]],
                     [[9,8,7], [6,5,4], [3,2,1]],
                     [[6,5,4], [9,8,7], [3,2,1]]])

# print(th_array.ndim)

# chain indexing
print(th_array[0][0][0]) # output :- 1

# multidimensional indexing
print(th_array[0, 0, 0]) # output :- 1

# array = np.array([1,2,3,4])

# array *= 2

# print(array)
# print(type(array))