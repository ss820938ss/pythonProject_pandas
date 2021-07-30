import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('./data/gapminder.tsv', sep='\t')
print(df.describe())
print('---------------------------------------------------------')
print(df.mean())
print('---------------------------------------------------------')
print(df['lifeExp'].median())
print('---------------------------------------------------------')
print(df['lifeExp'].std())
print('---------------------------------------------------------')
print(df.corr())
print('---------------------------------------------------------')
test = df[['year', 'lifeExp', 'pop']].corr()
print(test)
print('---------------------------------------------------------')
print('#  한국 자료')
df = pd.read_excel('./data/한국표준과학연구원_수질참조표준데이터_20201201.xlsx')
pd.set_option('display.max_columns',None)
print(df)
print('---------------------------------------------------------')
print(df.info())
print('---------------------------------------------------------')
print(df.describe())
print('---------------------------------------------------------')
print(df.mean())
print(df.median())
print(df.std())
print(df.corr())
print('---------------------------------------------------------')



