import numpy as np


# Numpy array (list/tuple as arguments): better to visualise as blocks
my_1d_array = np.array([1, 2, 3, 4])  # 1D array: need 1 layer of []
my_2d_array = np.array([[1, 2, 3], [2, 3, 4], [7, 8, 9]])  # 2d array: need 2 layers of []
my_3d_array = np.array([[[1, 2, 3]], [[0, 9, 8]]])  # 3d array: need 3 layers of []
# print(my_1d_array)
# print(my_2d_array)
# print(my_3d_array)


# print(my_3d_array.ndim)  # '.ndim' gets the dimension of array
# print(my_3d_array.shape)  # get number of: 2d arrays in 3d arrays, 1d arrays in 2d arrays, elements in 1d arrays
# print(my_3d_array[1, 0, 0])  # indexing


# Use nested for loops to iterate over all elements
a_3d_array = np.array([[[1, 2, 3], [-1, -2, -3]], [[4, 5, 6], [-4, -5, -6]]])
for i in a_3d_array:
    for j in i:
        for k in j:
            print(k)


# Funcionalities
# Create an array of zeros/ones
zeros_array = np.zeros(10)
# print(zeros_array)  # The zeros are all floats
# print(zeros_array.astype(int))
# Create an array prefilled with specific numbers
prefilled_array = np.full(10, 5)  # An array of 10 elements, each element = 5
# print(prefilled_array)


# Scalar Operations
# Addition & subtraction (CANNOT be performed on lists)
print("Addition: {} \n Subtraction: {}".format(my_2d_array + 2, my_2d_array - 2))
# Multiplication
my_2d_list = [[1, 2, 3], [2, 3, 4], [7, 8, 9]]
print("Multiplication of np arrays:\n{}".format(my_2d_array*2))  # All values of elements *2
print("Multiplication of lists:\n{}".format(my_2d_list*2))  # Repeat all elements
# Division (CANNOT be performed on lists)
print("Float division:\n{}".format(my_2d_array/2))
print("Integer division:\n{}".format(my_2d_array//2))
# Raise to a power (CANNOT be performed on lists)
print("\nRaise to a power:\n{}".format(my_2d_array**2))


# Take transpose of matrix (2d-array) (CANNOT be performed on lists)
print("\nTranspose: {}".format(my_2d_array.T))


# Element wise operation (CANNOT be performed on lists)
# Addition & subtraction & multiplication
matrix_1 = np.array([[1, 2], [4, 6]])
matrix_2 = np.array([[7, 8], [4, 2]])
print("Addition:\n{}\nSubtraction:\n{}Multiplication:\n{}".format(matrix_1 + matrix_2, matrix_1 - matrix_2, matrix_1*matrix_2))
# Division
print("Float division:\n{}".format(matrix_1/matrix_2))
print("Integer division:\n{}".format(matrix_1//matrix_2))
# Matrix multiplication
print("Matrix multiplication:\n{}".format(np.matmul(matrix_1, matrix_2)))


# Statistics
print("Min:{}".format(np.min(matrix_1)))  # np.min()
print("Max:{}".format(np.max(matrix_1)))  # np.max()
print("Sum of elements:{}".format(np.sum(matrix_1)))  # np.sum()
print("Mean of elements:{}".format(np.mean(matrix_1)))  # np.mean()
print("Standard deviaiton of elements:{}".format(np.std(matrix_2)))  # np.std()
