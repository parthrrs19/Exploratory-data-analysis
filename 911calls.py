import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')
print(df.info())
print(df.head())

print('Top 5 zipcodes for 911 calls:\n',df['zip'].value_counts().head(5))

print('Top 5 townships for 911 calls:\n',df['twp'].value_counts().head(5))

print('Number of unique title codes: ',df['title'].nunique())

#creating new column 'Reason'
df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])

print('Most common reasons for 911 calls are:\n',df['Reason'].value_counts().head(5))
sns.countplot(df['Reason'])
plt.show()

#converting strings to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

#creating columns 'Hours', 'Month', 'Day of Week'
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

df['Day of Week'] = df['Day of Week'].map(dmap)
print(df.head())

sns.set()
sns.countplot(x='Day of Week',hue='Reason',data=df)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

sns.countplot(x='Month',hue='Reason',data=df)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

byMonth = df.groupby('Month').count()
sns.lmplot(x='Month',y='lat',data=byMonth.reset_index())
plt.show()

#creating column 'Date'
df['Date'] = df['timeStamp'].apply(lambda x: x.date())
print(df.head())

df.groupby('Date').count()['twp'].plot()
plt.tight_layout()
plt.show()

df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()
plt.show()

df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()
plt.show()

df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
plt.show()

heatmapdf = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
fig = plt.figure(figsize=(12,7))
sns.heatmap(heatmapdf,cmap='coolwarm')
plt.show()
sns.clustermap(heatmapdf,cmap='coolwarm')
plt.show

monthday = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
fig = plt.figure(figsize=(12,7))
sns.heatmap(monthday,cmap='coolwarm')
plt.show()
sns.clustermap(monthday,cmap='coolwarm')
plt.show()
