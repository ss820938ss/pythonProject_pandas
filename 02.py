import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

test = df.groupby('year')['lifeExp'].mean()
print(test)
# test.plot()
# plt.show()
print('---------------------------------------------------------')
#  연습
print('#  연습')

test2 = df.groupby('year')['gdpPercap'].mean()
#  groupby()[].수식 << 규칙 지키지 않으면 오류 뜸
print(test2)
plt.title('gdpPercap test')
plt.xlabel('year')
plt.ylabel('gdpPercap')
# plt.plot(test2, '--', markersize=5)
# plt.show()

print()

test3 = df['lifeExp']
print(test3)
# plt.hist(test3, bins=100, histtype='step')
# plt.show()
print('---------------------------------------------------------')
#  표 모양 조절
print('#  표 모양 조절')

plt.title('test title')
plt.xlabel('year')
plt.ylabel('lifeExp')
# plt.plot(test, 'o', markersize=2)
# plt.show()
print('---------------------------------------------------------')
