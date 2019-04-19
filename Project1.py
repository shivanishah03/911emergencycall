# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:13:27 2018

@author: HP
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('911.csv')
print(df.head())
print(df['zip'].value_counts().head(5))
print(df['twp'].value_counts().head(5))
print(df['title'].nunique())
x=df['title'].iloc[0]
print(x.split(':')[0])
df['Reason']=df['title'].apply(lambda title:title.split(':')[0])
print(df['Reason'])
print(df['Reason'].value_counts())
print(sns.countplot(x='Reason',data=df))
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
type(df['timeStamp'].iloc[0])
time=(df['timeStamp'].iloc[0])
print(time.hour)
print(time.year)
print(time.dayofweek)
df['Hour']=df['timeStamp'].apply(lambda time: time.hour)
df['Month']=df['timeStamp'].apply(lambda time: time.month)
df['Day of week']=df['timeStamp'].apply(lambda time: time.dayofweek)
dmap={0:'Mon',1:'Tue',3:'Wed',4:'Thu',5:'Fri',5:'Sat',6:'Sun'}
df['Day of week'] = df['Day of week'].map(dmap)
print(sns.countplot(x='Day of week', data=df, hue='Reason',palette='viridis'))
print(sns.countplot(x='Month', data=df, hue='Reason',palette='viridis'))
byMonth=df.groupby('Month').count()
print(byMonth.head())
print(byMonth['lat'].plot())
print(sns.countplot(x='Day of week', data=df,palette='viridis'))
print(byMonth['lat'].plot())
dayHour=df.groupby(by=['Day of week','Hour']).count()['Reason'].unstack()
plt.figure(figsize=(12,6))
print(sns.heatmap(dayHour,cmap='viridis'))