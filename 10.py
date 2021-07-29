import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)
print(tips.dtypes)
print()

print(tips['sex'].memory_usage())
tips['sex'] = tips['sex'].astype(object)

print(tips['sex'].memory_usage())

print('---------------------------------------------------------')


def my_sq(x):
    return x ** 2


def my_exp(x, n):
    return x ** n


df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})
result1 = df['a'].apply(my_sq)
print(result1)
print()

# result2 = df['a'].apply(my_exp)
result2 = df['a'].apply(my_exp, n=5)
print(result2)

print('---------------------------------------------------------')


def my_exp(x, n):
    return x ** n


def avg_3(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x + y + z) / 3


df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})

result = df.apply(avg_3)
print(result)

print('---------------------------------------------------------')

