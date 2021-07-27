import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import missingno as msno
import seaborn as sns
from collections import Counter

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.svm import LinearSVC, SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import SMOTE
from xgboost.sklearn import XGBClassifier

import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

import os
for dirname, _, filenames in os.walk('./data/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('./data/water_potability.csv')
print(df.head(10))
print(df.shape)
print(df.info())
unique_count = []

for col in df.columns:
    unique_count.append(len(df[col].unique()))

print(pd.Series(unique_count, index = df.columns))

print(df.describe(include='all'))

x = df.Potability.value_counts()
labels = [0, 1]
print(x)

fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(16,6))

ax[0].pie(x,
        labels = labels,
        autopct = '%1.1f%%',
        colors=['orange', 'steelblue'],
        explode = [0.005]*len(labels),
        textprops={'size': 'x-large'},
        wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'})

ax[1].bar(labels,height=x,color=['orange', 'steelblue'])
ax[1].set_xlabel('Potability')
ax[1].set_ylabel('Count')
ax[1].set_xticks([0, 1])

plt.show()

cor_mat = df.corr()
mask = np.array(cor_mat)
mask[np.tril_indices_from(mask)] = False
fig = plt.gcf()
fig.set_size_inches(30, 12)
sns.heatmap(data=cor_mat, mask=mask, square=True, annot=True, cbar=True)

fig, ax = plt.subplots(ncols=2, nrows=9, figsize=(14, 42))

features = list(df.columns.drop('Potability'))
target = 'Potability'
idx = 0

for col in features:
    sns.violinplot(data=df, y=col, x=target, ax=ax[idx, 0],
                   inner='quartile', color='pink')

    sns.boxplot(data=df, y=col, x=target, ax=ax[idx, 1],
                palette=('orange', 'steelblue'))

    idx += 1
plt.show()

df.drop('Potability', axis=1).hist(bins=10, figsize=(20, 20))
plt.show()

