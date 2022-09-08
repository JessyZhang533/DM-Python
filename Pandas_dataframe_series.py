import pandas as pd
import numpy as np


# Creating a dataframe using lists/np arrays
my_list = [['Apple', 'red'], ['Banana', 'yellow'], ['Plum', 'black']]
my_dataframe_1 = pd.DataFrame(my_list, columns=['Fruit', 'Color'])  # Default indices of rows & columns are integers starting from zero
print(my_dataframe_1)

my_array = np.array([[1, 2], [3, 4], [5, 6]])
my_dataframe_2 = pd.DataFrame(my_array, index=['row1', 'row2', 'row3'], columns=['odd', 'even'])  # Default indices of rows & columns are integers starting from zero
print(my_dataframe_2)

# Creating a dataframe using dictionaries: keys-->column labels; values(encapsulated in lists)-->content os dataframe, same key same column
my_dic = {'Fruit': ['Apple', 'Banana', 'Plum'], 'Color': ['red', 'yellow', 'black']}
my_dataframe_3 = pd.DataFrame(my_dic)
print(my_dataframe_3)


# Loading csv file as dataframe
# First row of csv file-->column labels
# numerical values automatically assigned as row labels
df = pd.read_csv('cereals.csv')
print(df)

# Changing the index column
# 1.Set one of the existing index column as the new index column: .set_index()
print(df.set_index('name'))  # Doesn't actually change df
df.set_index('name', inplace=True)  # Does actually change df: inplace=True
print(df)
# 2.Change indices directly: see line 11 of code


# .head(n): gives us the first n rows of our data frame or series by default.
# .tail(n): gives us the last n rows of our data frame or series by default.
print(df.head(3))
print(df.tail(3))
# [n:m]: row slicing, n inclusive, m exclusive; Doesn't actually change df
print(df[1:4])
# If we pass a list of boo lines to the brackets operator, we get another dataframe containing only
# the rows for which the corresponding element in the list were true.
second_row = [False, True, False, False, False, False, False, False, False, False]
print(df[second_row])

# INDEXING (Doesn't actually change df) https://www.geeksforgeeks.org/select-rows-columns-by-name-or-index-in-pandas-dataframe-using-loc-iloc/#:~:text=Indexing%20in%20Pandas%20means%20selecting,also%20known%20as%20Subset%20selection.
# 1.column indexing: single column: []; multiple columns: [[]]
# 2.row indexing: single row: .loc[]; multiple rows: .loc[[]]
# print(df[['protein', 'rating']])
print(df.loc[['Apple Jacks', 'All-Bran']])

# .describe(): Get statistical summary of the dataframe https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
# print(df.describe())
