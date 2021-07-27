import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')  # tsv 파일이라 \t 를 써서 정렬, csv 는 자동정렬
print(df)
print('---------------------------------------------------------')
print(type(df))
print(df.dtypes)
print('---------------------------------------------------------')
print(df.columns)
print('---------------------------------------------------------')
print(df.info())
print('---------------------------------------------------------')
print(df.head())
print('---------------------------------------------------------')
print(df.tail())
print('---------------------------------------------------------')
print(df['country'])
print(df['continent'])
print(df['year'])
print(df['lifeExp'])
print(df['pop'])
print(df['gdpPercap'])
print('---------------------------------------------------------')
print(type(df['country']))
print(type(df['year']))
print(type(df))
print('---------------------------------------------------------')
choice = df[['country', 'year']]
print(choice)
print(type(choice))
print('---------------------------------------------------------')
#  연습
print('#  연습')

choice2 = df[['country', 'pop', 'year']]
print(choice2)
print(choice2.dtypes)
print(type(choice2))
print(choice2.head())
print('---------------------------------------------------------')
print(df.loc[:10])
print()
print(df.iloc[:10])
print('---------------------------------------------------------')
df.index = df.index+1
print(df)
print('---------------------------------------------------------')
print(df.iloc[4])
print()
print(df.loc[5])
print('---------------------------------------------------------')
#  연습
print('#  연습')

print(df.loc[:3])
print()
print(df.iloc[3:-1])
print()
print(df.iloc[-1])
print()
print(df.loc[3].dtype)
print('---------------------------------------------------------')
#  문제
print('#  문제')

attr = df[['country', 'year']]
print(attr.iloc[9:99])
print('---------------------------------------------------------')
print(df['lifeExp'].mean())
print(df['lifeExp'].sum())
print(df['lifeExp'].shape)
print('---------------------------------------------------------')
#  문제
print('#  문제')

print(df[['lifeExp', 'pop']].mean())
print()
print(df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean())
print()

result = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(result)
print(type(result))
print()
print(result.info())
print('---------------------------------------------------------')

