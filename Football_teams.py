import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/Football teams.csv')
# df.to_excel('./save/football_team.xlsx')

df = pd.read_excel('./save/football_team.xlsx')
print(df)
print(type(df))
print(df.columns)
print(df.dtypes)
print(df.info())
print('---------------------------------------------------------')
print(df['Team'])
print(df['Tournament'])
print(df['Pass%'])
print(df['AerialsWon'])
print(df['Rating'])
print('---------------------------------------------------------')
print(type(df['Team']))
print('---------------------------------------------------------')
choice = df[['Team', 'Pass%']]
print(choice)
print(type(choice))
print(choice.head())
print('---------------------------------------------------------')
print(df.loc[:5])
print(df.iloc[:5])
print('---------------------------------------------------------')
# pd.set_option('display.max_columns', None)  # 요약없이 표 전체보기
# pd.set_option('display.max_rows', None)
# print(df.sort_values(by='Goals', ascending=False))
print('---------------------------------------------------------')
df.index = df.index + 1
print(df)
print('---------------------------------------------------------')
print(df.iloc[4])
print(df.loc[3])
print('---------------------------------------------------------')
print(df.loc[:3])
print()
print(df.iloc[3:-1])
print()
print(df.iloc[-1])
print()
print(df.loc[3].dtype)
print('---------------------------------------------------------')
print(df['Pass%'].mean())
print(df['Pass%'].sum())
print(df['Pass%'].shape)
print('---------------------------------------------------------')
print(df[['Pass%', 'Rating']].mean())
print()

result = df.groupby(['Pass%', 'Rating']).mean()
print(result)
print('---------------------------------------------------------')
test = df.groupby('Goals')['Rating'].mean()
print(test)
test.plot()
plt.title('test')
plt.xlabel('Goal')
plt.ylabel('Rating')
plt.show()
