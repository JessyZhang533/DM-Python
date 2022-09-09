import yfinance as yf  # a python library that allows down loading stocka data from yahoo finance
import pandas as pd
import matplotlib.pyplot as plt


# 1.Getting stock data using yfinace
# yf.downlaod('label_name', start='date1', end='date2'): download data
df = yf.download('AAPL', start='2022-01-03', end='2022-01-31')  # 'AAPL' is an abbreviation for Apple
print(df.head(10))
print(type(df.index[0]))  # DAta type is Timestamp, indicsting it is a time series


# 2.Convert a dataset into a time series
# (1) pd.to_datetime(): convert the values of the date column from string to Timestamp
df_1 = pd.read_csv('data_df.csv')
df_1.set_index('Date', inplace=True)  # Change the index
print(df_1)
print(type(df_1.index[0]))
df_1.index = pd.to_datetime(df_1.index)
print(type(df_1.index[0]))
# (2) cases where direct conversion as shown above is not possible
df_2 = pd.read_csv('ETH_1h.csv')
df_2.set_index('Date', inplace=True)
print(df_2)
print(type(df_2.index[0]))
df_2.index = pd.to_datetime(df_2.index, format='%Y-%m-%d %I-%p')
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print(type(df_2.index[0]))


# 3.Working with time series
# (1) day_name(): check if 2002-1-1 is a business day
Jan_1 = pd.to_datetime('2022, 1, 1')
print(Jan_1.day_name())
# (2) .min()/.max(): find the minimum/maximum date among timestamp/datetime (sometimes time series dataset might not be in order)
print(df.index.max())
print(df.index.min())
# (3) .loc[]: indexing using timestamp, time-based indexing
print(df.loc['2022-01-07'])
print(df.loc['2022-01'])
print(df.loc['2022-01-05':'2022-01-10'])


# 4.Time Series data visualization
plt.figure(figsize=(15, 5))
plt.title('Apple stock prices for 5 years')
plt.xlabel('Year')
plt.ylabel('Price')
plt.plot(df['Adj Close'])
plt.show()
# index to get data for a desired period
plt.plot(df.loc['2022-01-05':'2022-01-10']['Adj Close'])
plt.show()
