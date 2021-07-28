import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

anscombe = sns.load_dataset('anscombe')
# print(anscombe)

# dataset1 = anscombe[anscombe['dataset'] == 'I']
# plt.plot(dataset1['x'], dataset1['y'], 'o')
# plt.show()

print('---------------------------------------------------------')

# dataset1 = anscombe[anscombe['dataset'] == 'I']
# dataset2 = anscombe[anscombe['dataset'] == 'II']
# dataset3 = anscombe[anscombe['dataset'] == 'III']
# dataset4 = anscombe[anscombe['dataset'] == 'IV']

# fig = plt.figure()
# fig.suptitle('Anscombe Data')
# fig.tight_layout()

# axe1 = fig.add_subplot(2, 2, 1)
# axe2 = fig.add_subplot(2, 2, 2)
# axe3 = fig.add_subplot(2, 2, 3)
# axe4 = fig.add_subplot(2, 2, 4)

# axe1.plot(dataset1['x'], dataset1['y'], 'o')
# axe2.plot(dataset2['x'], dataset2['y'], 'o')
# axe3.plot(dataset3['x'], dataset3['y'], 'o')
# axe4.plot(dataset4['x'], dataset4['y'], 'o')

# axe1.set_title('DataSet I')
# axe2.set_title('DataSet II')
# axe3.set_title('DataSet III')
# axe4.set_title('DataSet IV')

# plt.show()

print('---------------------------------------------------------')

tips = sns.load_dataset('tips')
print(tips)

# fig = plt.figure()
# axes1 = fig.add_subplot(1, 1, 1)
# axes1.hist(tips['total_bill'], bins=10)

# axes1.set_title('Histogram of Total Bill')
# axes1.set_xlabel('Frequency')
# axes1.set_ylabel('Total Bill')

# plt.show()

print('---------------------------------------------------------')

# fig = plt.figure()
#
# axes1 = fig.add_subplot(1, 1, 1)
# axes1.scatter(tips['total_bill'], tips['tip'])
#
# axes1.set_title('Scatter Graph')
# axes1.set_xlabel('Total Bill')
# axes1.set_ylabel('Tip')
#
# plt.show()

print('---------------------------------------------------------')

# tips = sns.load_dataset('tips')
# print(tips.sort_values(by=['tip']))
#
#
# def recode_sex(sex):
#     if sex == 'Female':
#         return 'red'
#     else:
#         return 'blue'
#
# tips['sex_color'] = tips['sex'].apply(recode_sex)
#
# fig = plt.figure()
# axes1 = fig.add_subplot(1, 1, 1)
# axes1.scatter(x=tips['total_bill'],
#               y=tips['tip'],
#               s=tips['size'] * 10,
#               c=tips['sex_color'],
#               alpha=0.5)
#
# axes1.set_title('Scatter Graph')
# axes1.set_xlabel('Total Bill')
# axes1.set_ylabel('Tip')
#
# plt.show()

print('---------------------------------------------------------')

# tips = sns.load_dataset('tips')
# ax = plt.subplots()
# ax = sns.kdeplot(data=tips['total_bill'],
#                  data2=tips['tip'],
#                  shade=True)
#
# ax.set_title('Kernel Density Plot')
# ax.set_xlabel('Total Bill')
# ax.set_ylabel('Tip')
#
# plt.show()

print('---------------------------------------------------------')

# tips = sns.load_dataset('tips')
# ax = plt.subplots()
#
# colors = ["yellow", "purple"]
# sns.set_palette(sns.color_palette(colors))
#
# ax = sns.violinplot(x='time', y='total_bill',
#                     hue='sex', data=tips, split=True)
#
# ax.set_title('Violinplot Plot')
#
# plt.show()

print('---------------------------------------------------------')

# tips = sns.load_dataset('tips')
#
# facet = sns.FacetGrid(tips, col='time')
# facet.map(sns.displot, 'total_bill', rug=True)
#
# plt.show()

print('---------------------------------------------------------')

df1 = pd.read_csv('./data/concat_1.csv')
df2 = pd.read_csv('./data/concat_2.csv')
df3 = pd.read_csv('./data/concat_3.csv')

# print(df1)
# print(df2)
# print(df3)

total = pd.concat([df1, df2, df3])
print(total)
print()

new_Series = pd.Series(['new1', 'new2', 'new3', 'new4'])
print(type(new_Series))
print(pd.concat([total, new_Series]))
print()

# result = pd.concat([total, new_Series])
# print(result)

new_DataFrame = {'A': 'new1',
                 'B': 'new2',
                 'C': 'new3',
                 'D': 'new4'}

link_data = total.append(new_DataFrame,
                         ignore_index=True)
print(link_data)
print()

total_row = pd.concat([df1, df2, df3], axis=0)
total_attr = pd.concat([df1, df2, df3], axis=1,
                       ignore_index=True)
print(total_row)
print(total_attr)
print()

df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

total_df = pd.concat([df1, df2, df3], axis=0)
print(total_df)
print()

total_df2 = pd.concat([df1, df2, df3], join='inner')
print(total_df2)
print()

total_row = pd.concat([df1, df2, df3])
df1_df3 = pd.concat([df1, df3], join='inner')

print(total_row)
print(df1_df3)

print('---------------------------------------------------------')

