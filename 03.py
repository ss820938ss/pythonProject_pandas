import pandas as pd
import matplotlib.pyplot as plt

exam = ['김지용', 20]
exam_index = ['name', 'age']
make_series = pd.Series(exam, exam_index)
print(make_series.index)
print(make_series)
print('---------------------------------------------------------')
data = {'NAME': ['TeaYeon', 'jenny', 'yuju'],
        'GROUP': ['SNSD', 'BLACKPINK', 'GFRIEND'],
        'BORN': ['1989-03-09', '1996-01-16', '1997-10-04'],
        'AGE': [33, 26, 25],
        'CAMPANY': ['SM', 'YG', 'SOURCE_MUSIC']
        }

index_DataFrame = [1, 2, 3]
make_DataFrame = pd.DataFrame(data, index_DataFrame)
print(make_DataFrame)
print()
print(make_DataFrame.info())
print()
one = make_DataFrame.iloc[0]  # 1개만 표시할때 시리즈, 2개이상은 데이터프레임
print(one)
print(type(one))
print(one.index)
print(one.values)
print()

age = make_DataFrame['AGE']
print(age)
print(type(age))
print()

print('AGE 의 평균값 : ', age.mean())
print('AGE 의 최대값 : ', age.max())
print('AGE 의 최소값 : ', age.min())
print('AGE 의 표준편차값 : ', age.std())
print()

a = make_DataFrame.describe()
print(a)  # 자동 계산 수식
print()


print('---------------------------------------------------------')
