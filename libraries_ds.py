import numpy as np


# Numpy array (list/tuple as arguments): better to visualise as blocks
my_1d_array = np.array([1, 2, 3, 4])  # 1D array: need 1 layer of []
my_2d_array = np.array([[1, 2, 3], [2, 3, 4], [7, 8, 9]])  # 2d array: need 2 layers of []
my_3d_array = np.array([[[1, 2, 3]], [[0, 9, 8]]])  # 3d array: need 3 layers of []
# print(my_1d_array)
# print(my_2d_array)
# print(my_3d_array)

print(my_3d_array.ndim)  # '.ndim' gets the dimension of array
print(my_3d_array.shape)  # get number of: 2d arrays in 3d arrays, 1d arrays in 2d arrays, elements in 1d arrays
print(my_3d_array[1, 0, 0])  # indexing

# Use nested for loops to iterate over all elements
a_3d_array = np.array([[[1, 2, 3], [-1, -2, -3]], [[4, 5, 6], [-4, -5, -6]]])
for i in a_3d_array:
    for j in i:
        for k in j:
            print(k)
