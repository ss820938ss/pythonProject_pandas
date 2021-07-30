import pandas as pd
import seaborn as sns
import os

ebola = pd.read_csv('./data/country_timeseries.csv')
# print(ebola.info())

ebola['new_Date'] = pd.to_datetime(ebola['Date'])
print(ebola)
print(ebola.info())
print('---------------------------------------------------------')
ebola['date_Year'] = ebola['new_Date'].dt.year
print(ebola.date_Year)
print()

print(ebola[['Date', 'new_Date', 'date_Year']])
print('---------------------------------------------------------')
ebola['new_Date'] = pd.to_datetime(ebola['Date'])
ebola['date_Year'] = ebola['new_Date'].dt.year
ebola['date_Month'] = ebola['new_Date'].dt.month
ebola['date_Day'] = ebola['new_Date'].dt.day

print(ebola[['new_Date', 'date_Year', 'date_Month', 'date_Day']])
print('---------------------------------------------------------')
df = sns.load_dataset('titanic')
print(df.describe(include='all'))