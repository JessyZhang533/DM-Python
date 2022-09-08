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

# INDEXING (Doesn't actually change df)
# https://www.geeksforgeeks.org/select-rows-columns-by-name-or-index-in-pandas-dataframe-using-loc-iloc/#:~:text=Indexing%20in%20Pandas%20means%20selecting,also%20known%20as%20Subset%20selection.
# 1.column indexing: single column: []; multiple columns: [[]]
# 2.row indexing: single row: .loc[]; multiple rows: .loc[[]]
print(df[['protein', 'rating']])
print(df.loc[['Apple Jacks', 'All-Bran']])

# FILTERING (Doesn't actually change df)
# If we pass a list of boo lines to the brackets operator, we get another dataframe containing only
# the rows for which the corresponding element in the list were true.
second_row = [False, True, False, False, False, False, False, False, False, False]
print(df[second_row])
# Filtering rows: apply condiitons (essentially boolean lists)
print(df[df['calories'] > 70])  # one condition
print(df[(df['calories'] > 70) & (df['protein'] < 4)])  # group conditions: and, &
print(df[(df['calories'] > 70) | (df['protein'] > 3)])  # group conditions: or, |
# .loc[..., ...]: 1st argument-->row label, 2nd argument-->column label
print(df.loc['All-Bran', 'protein'])
# .loc[[...], [...]]: same as above but get a dataframe
print(df.loc[['All-Bran'], ['protein']])
# .loc[...:..., ...:...]: slice rows & columns
print(df.loc['100% Bran':'All-Bran', 'calories':'protein'])
# .loc[[..., ...], ...:...]: index rows, slice columns; vice versa
print(df.loc[['100% Bran', 'All-Bran'], 'calories':'protein'])

# .iloc: essentially same as .loc, but takes position rather than names as arguments
print(df.iloc[2, 1])
print(df.iloc[[2], [1]])
print(df.iloc[0:3, 0:2])
print(df.iloc[[0, 3], 0:2])

# Adding and deleting rows and columns
# 1.Adding rows: .loc[...] = [.., ..., ......]
df.loc['new'] = [0, 0, 0, 0]  # Note: should match the number of columns
print(df)
# 2.Deleting rows: .drop(..., axis=0, inplace=True)-->dataframe wouldn't change if inplace=False
df.drop('new', axis=0, inplace=True)
print(df)
# 3.Adding columns: [...] = [..., ..., ......]
df['new'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Note: should match th enumber of columns
print(df)
# 4.Deleting columns: .drop(..., axis=1, inplace=True)-->dataframe wouldn't change if inplace=False
df.drop('new', axis=1, inplace=True)
print(df)


# .describe(): Get statistical summary of the dataframe https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
print(df.describe())


# SORTING
# 1.Sort w.r.t. a column (ascending by default; alphabetically/numerically)
print(df.sort_values('calories'))  # ascending
print(df.sort_values('calories', ascending=False))  # descending


# Exporting & saving a dataframe: .to_csv('filename.csv', index_label=...)-->depends on whether one wants to store row labels
df_new = df[2:5]
df_new.to_csv('my_file.csv', index_label=True)  # Store row labels (default)
df_new_show = pd.read_csv('my_file.csv')
print(df_new_show)
