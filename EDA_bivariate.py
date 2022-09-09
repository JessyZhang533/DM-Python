import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('titanic.csv')
print(df)

# Continuous & Continuous:
# 1.scatter plot
sns.scatterplot(x=df['Fare'], y=df['Age'])
plt.title('Bivariate-continuous & continuous-1')
plt.show()
# 2..corr(): find correlation; correlation high, the two variables are more related
correlation_dataframe = df[['Fare', 'Age']].corr()  # a small dataframe; correlation very low
print(correlation_dataframe)
# 3.sns.heatmap(): create a heatmap to graphically visualise the two variables
sns.heatmap(correlation_dataframe)
plt.show()


# Categorical & Categorical
# 1.sns.barplot(): bar plot
survived_ratio = df[['Pclass', 'Survived']].groupby('Pclass').sum()
print(survived_ratio)
sns.barplot(x=survived_ratio.index, y=survived_ratio['Survived'])
plt.show()


# Continuous & Categorical
# 1.sns.boxplot()
# Survived-->categorical, Age-->continuous
sns.boxplot(x=df['Survived'], y=df['Age'])  # plot two box plots, one for survived=0, one for survived=1, both based on the data of Age
plt.show()  # Younger people have a greateer chace of survival
# 2.sns.barplot()
# Sex-->categorical, Age-->continuous
sns.barplot(x=df['Sex'], y=df['Age'])  # plot two bars, one for sex=0, one for sex=1, both based on the data of age
plt.show()  # Elderly are mostly male
