import pandas as pd
import seaborn as sns
import numpy as np

titanic = sns.load_dataset('titanic')
print(titanic)

print('---------------------------------------------------------')

def count_missing(vec):
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count

cmis_col = titanic.apply(count_missing)
print(cmis_col)

print('---------------------------------------------------------')

def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return (num/dem) * 100

pmis_col = titanic.apply(prop_missing)
print(pmis_col)

print('---------------------------------------------------------')

titanic['num_missing'] = titanic.apply(count_missing, axis=1)
print(titanic)

print('---------------------------------------------------------')

print(titanic.loc[titanic.num_missing > 1, :])

print('---------------------------------------------------------')

tips = sns.load_dataset('tips')
# pd.set_option('display.max_rows',None)
print(tips)
print()

pmis_col = tips.apply(prop_missing)
print(pmis_col)
print()

tips['num_missing'] = tips.apply(count_missing, axis=1)
print(tips)
print()

print(tips.loc[tips.num_missing > 1, :])
