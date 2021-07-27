import pandas as pd

scientist = pd.read_csv('./data/scientists.csv')
print(scientist['Born'])
print(scientist['Died'])

born_change = pd.to_datetime(scientist['Born'], format='%Y/%m/%d')
print(born_change)
print('---------------------------------------------------------')
print(scientist)
print()

scientist["born_change"] = pd.to_datetime(scientist['Born'], format='%Y/%m/%d')
print(scientist["born_change"].dtype)
print()

scientist["died_change"] = pd.to_datetime(scientist['Died'], format='%Y/%m/%d')
print(scientist)
print(scientist["died_change"].dtype)
print()

drop_test = scientist.drop(['Born', 'Died'], axis=1)
print(drop_test)
print('---------------------------------------------------------')
#  연습
print('#  연습')

scientist2 = pd.read_csv('./data/scientists.csv')
scientist2_drop = scientist2.drop(['Died'], axis=1)
print(scientist2_drop)
print('---------------------------------------------------------')
a = scientist.sort_values(by='Age', ascending=False)
print(a)
print('---------------------------------------------------------')
name_test = scientist['Name']
name_test.to_pickle('./save/namep.pickle')

reading = pd.read_pickle('./save/namep.pickle')
print(reading)
print()

scientist_save = scientist
scientist_save.to_pickle('./save/savetest.pickle')

scientist_reading = pd.read_pickle('./save/savetest.pickle')
print(scientist_reading)
print()

scientist_save2 = scientist
scientist_save2.to_csv('./save/savetest.csv')

scientist_reading2 = pd.read_csv('./save/savetest.csv')
print(scientist_reading2)
print()

scientist_save3 = scientist
scientist_save3.to_csv('./save/savetest.tsv', sep='\t')

scientist_reading3 = pd.read_csv('./save/savetest.tsv', sep='\t')
print(scientist_reading3)
print()

scientist.to_excel('./save/savatest1.xls')
scientist.to_excel('./save/savatest2.xlsx')
print('---------------------------------------------------------')


