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
born = df['Born'].sort_values(ascending=False)
result1 = age.append(born)
result2 = result1.sample()
print(result1)
print()

died = df['Died']
result3 = age.append(died)
result4 = result3.sample()
print(result3)
print('---------------------------------------------------------')

data = {'NAME': ['TaeYeon', 'Jenny', 'YuJu'],
        'GROUP': ['SNSD', 'BlackPink', 'GFriend'],
        'BORN': ['1989-03-09', '1996-01-16', '1997-10-04'],
        'AGE': [33, 26, 25],
        'COMPANY': ['SM', 'YG', 'Source_Music']
        }
make_DataFrame = pd.DataFrame(data)
new_ages = make_DataFrame['AGE']

print(age + new_ages)
