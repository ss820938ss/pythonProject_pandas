import pandas as pd


data1 = {'NAME': ['TeaYeon', 'Jenny', 'YuJu'],
         'GROUP': ['SNSD', 'BlackPink', 'GFriend'],
         'BORN': ['1989-03-09', '1996-01-16', '1997-10-04'],
         'AGE': [33, 26, 25],
         'COMPANY': ['SM', 'YG', 'Source_Music'],
         'TEST1': ['t1', 't2', 't3']}

df1 = pd.DataFrame(data1)

data2 = {'NAME': ['태연', 'Jenny', 'YuJu'],
         'GROUP': ['SNSD', 'BlackPink', 'GFriend'],
         'BORN': ['1989-03-09', '1996-01-16', '1997-10-04'],
         'AGE': [33, 26, 25],
         'COMPANY': ['SM', 'YG', 'Source_Music'],
         'TEST2': ['t1', 't2', 't3']}

df2 = pd.DataFrame(data2)

# print(df1['AGE'])
# print(df2['AGE'])

total = pd.merge(df1['GROUP'], df2['GROUP'])
print(total)
print()

total2 = pd.merge(df1['NAME'], df2['NAME'])
print(total2)  # 같지 않은 태연 부분은 표시되지 않고 합쳐짐
print()

# total3 = pd.merge(df1['TEST1'], df2['TEST2'])  # 머지할 항목의 열 이름이 같지 않으면 오류남
# print(total3)

total3 = pd.merge(df1, df2)
print(total3)  # 중복된 열이 있으면 하나로 합하고 다르면 나열해 붙임, 내용이 다른 행값은 생략함
# t1 과 같은 라인이 생략되는 이유는 태연과 같은 행값이라 그 줄이 전부 생략됨
print()

total4 = df1.merge(df2,
                   left_on='NAME',
                   right_on='GROUP')
print(total4)

print('---------------------------------------------------------')

person = pd.read_csv('./data/survey_person.csv')
site = pd.read_csv('./data/survey_site.csv')
visited = pd.read_csv('./data/survey_visited.csv')
servey = pd.read_csv('./data/survey_survey.csv')

# print(person)
# print(site)
# print(visited)
# print(servey)

merge_example1 = person.merge(servey,
                              left_on='ident',
                              right_on='person')
print(merge_example1)
# dyer, William, Dyer 와 같은 값은 이름은 같지만 데이터 기준으로는 다른 값이라 중복 출력
print()

merge_example2 = person.merge(visited,
                              left_on='ident',
                              right_on='site')
print(merge_example2)
print()

merge_example3 = person.merge(site,
                              left_on='ident',
                              right_on='name')
print(merge_example3)
print()

print('---------------------------------------------------------')

evola = pd.read_csv('./data/country_timeseries.csv')
# print(evola)

# print(evola.isnull())
# print(evola.isnull().sum())

evola_parts = evola.iloc[:10, :5]  # 앞에건 행, 뒤에건 열
print(evola_parts)
print()

print(evola_parts.fillna(0))  # NaN 값을 0으로 채우겠다는 의미
print()

print(evola_parts.fillna(method='ffill'))
# front fill 앞의 값으로 NaN을 채우겠다는 의미, 맨 앞이 NaN일 경우 NaN 값이 남는 경우가 있음
print()

print(evola_parts.fillna(method='bfill'))
# back fill 뒤의 값으로 NaN을 채우겠다는 의미, 맨 뒤가 NaN일 경우 채워지지 않음
print()

print(evola_parts.interpolate())
# interpolate() 메서드는 NaN값의 앞과 뒤의 평균값을 NaN 값으로 치환시킴
# 앞이나 뒤의 값 중 하나가 NaN일 경우 평균값을 내는게 불가능, 그대로 NaN으로 남음
print()

print(evola_parts.dropna())  # NaN 값을 포함한 행을 지워냄
print()

print('---------------------------------------------------------')

evola = pd.read_csv('./data/country_timeseries.csv')
three_country = evola.loc[:10, ['Cases_Guinea',
                                'Cases_Liberia',
                                'Cases_SierraLeone']]
print(three_country)
print()

evola['country_sum'] = evola['Cases_Guinea'] + evola['Cases_Liberia'] + evola['Cases_SierraLeone']
c_sum = evola.loc[:10, ['Cases_Guinea',
                        'Cases_Liberia',
                        'Cases_SierraLeone',
                        'country_sum']]
print(c_sum)
