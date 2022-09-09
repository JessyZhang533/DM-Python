import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# Univariate analusis: continuous data
df = pd.read_csv('iris.csv')
print(df)

# 1.sns.scatterplot(): scatter plot
x_axis = df.index  # x axis: extract the row labels
y_axis = df['petal.length']
sns.scatterplot(x_axis, y_axis, hue=df['variety'])  # 'hue' assigns different colors to the data points based on the categgory they belong to
plt.show()

# 2.sns.stripplot(): strip plot
sns.stripplot(x=df['variety'], y=df['petal.length'])  # x axis is the categories
plt.show()

# 3.sns.histplot(): show distribution od data
plt.title('seaborn distribution')
sns.histplot(df['petal.length'])  # x axis is the petal length; height indicates how many data points have the same given petal length
plt.show()
# same as hist()
plt.title('histogram')
plt.hist(df['petal.length'])
plt.show()

# 4.sns.boxplot(): 5 number summary: min, Q1, Q2(median), Q3, max
sns.boxplot(df['petal.length'])
plt.title('box plot')
plt.show()


# Univariate analysis: categorical data
# 1.sns.countplot(): give the total count of each value
sns.countplot(df['variety'])
plt.show()
# collaborate with plt.pie()
_labels = ['Setosa', 'Versicolor', 'Virginica']
plt.pie(df['variety'].value_counts(), labels=_labels)
plt.show()
