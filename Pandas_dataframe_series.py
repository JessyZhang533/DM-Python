import pandas as pd
import numpy as np


# Creating a dataframe using lists/np arrays
my_list = [['Apple', 'red'], ['Banana', 'yellow'], ['Plum', 'black']]
my_dataframe_1 = pd.DataFrame(my_list, columns=['Fruit', 'Color'])  # Default indices of rows & columns are integers starting from zero
print(my_dataframe_1)

my_array = np.array([[1, 2], [3, 4], [5, 6]])
my_dataframe_2 = pd.DataFrame(my_array, columns=['odd', 'even'])  # Default indices of rows & columns are integers starting from zero
print(my_dataframe_2)

# Creating a dataframe using dictionaries: keys-->column labels; values(encapsulated in lists)-->content os dataframe, same key same column
my_dic = {'Fruit': ['Apple', 'Banana', 'Plum'], 'Color': ['red', 'yellow', 'black']}
my_dataframe_3 = pd.DataFrame(my_dic)
print(my_dataframe_3)
