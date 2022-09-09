# Categorical Variable Transformation
# Machines can only process numerical values. Sometimes need to transform categorical values into numerical values
import pandas as pd


df = pd.read_csv('titanic.csv')
df = df[0:5][['Name', 'Sex']]
print(df)

# 1.Label encoding
print(df['Sex'].replace({'male': 0, 'female': 1}, inplace=False))  # inplace=True: cahnge dataframe; only display 'Sex' column

# 2.Frequency encoding
# replace categorical variables with their frequency
freq = df['Sex'].value_counts()/len(df['Sex'])
print(freq)
df['Sex'].replace({'male': freq['male'], 'female': freq['female']}, inplace=True)  # inplace=True: cahnge dataframe
print(df)
