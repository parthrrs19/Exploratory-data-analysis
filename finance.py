from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import matplotlib.pyplot as plt

#reading data
df = pd.read_pickle('all_banks')
tickers = ['BAC','C','GS','JPM','MS','WFC']

#exploratory data analysis
#maximum close price
df.xs(key='Close',axis=1,level='Stock Info').max()

#returns of each bank
returns = pd.DataFrame()
for x in tickers:
    returns[x+' Return'] = df[x]['Close'].pct_change()
print(returns.head())

sns.set()
sns.pairplot(returns)
plt.show()

print(returns.idxmin())
print(returns.idxmax())
print(returns.std())
print(returns.loc['2015-01-01':'2015-12-31'].std())

#morgan stanley 2015 returns
sns.distplot(returns['MS Return'].loc['2015-01-01':'2015-12-31'],bins=100,color='green')
plt.show()

#citigroup 2008 returns
sns.distplot(returns['C Return'].loc['2008-01-01':'2008-12-31'],bins=100,color='red')
plt.show()

#visualizations
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

for x in tickers:
    df[x]['Close'].plot(figsize=(12,4),label=x)
plt.legend()
plt.show()

df.xs(key='Close',axis=1,level='Stock Info').plot()
plt.show()

#moving averages
plt.figure(figsize=(12,6))
df['BAC']['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
df['BAC']['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()
plt.show

#correlation between stocks close price
sns.heatmap(df.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True,cmap='coolwarm')
plt.show()

sns.clustermap(df.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True,cmap='viridis')
plt.show()