import pandas as pd

df = pd.read_csv('./data/scientists.csv')
print(df)
print()

age = df['Age']
result = age > age.mean()
print(age)
print('---------------------------------------------------------')
result = age > 59.125
print(result)
print()

print(age[age > age.mean()])
print()

age = df['Age']
print(age + age)
print()

print(age * 2)
print()

age = df['Age']
born = df['Born']
result1 = age.append(born)
result2 = result1.sample()
print(result1)
print('---------------------------------------------------------')


