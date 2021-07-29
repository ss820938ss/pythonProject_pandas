import pandas as pd

pew = pd.read_csv('./data/pew.csv')

# pd.set_option('max_columns', None)  # 모든 열들이 보이게 하기
print(pew)

print('---------------------------------------------------------')

test = pd.melt(pew, id_vars='religion',
               var_name='income',
               value_name='count')
# pd.set_option('max_rows', None)  # 모든 헹들이 보이게 하기
print(test)

print('---------------------------------------------------------')

print('#  billboard')
billboard = pd.read_csv('./data/billboard.csv')
# print(billboard)

pd.set_option('max_columns', None)
billboard_song = pd.melt(billboard,
                         id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week',
                         value_name='rating')
billboard_song = billboard_song[['year', 'artist', 'track', 'time', 'date.entered']]
billboard_song = billboard_song.drop_duplicates()
print(billboard_song)
print()

print(billboard_song[billboard_song.track == 'Loser'])

print('---------------------------------------------------------')

weather = pd.read_csv('./data/weather.csv')
print(weather)
print()

weather_test = pd.melt(weather,
                       id_vars=['id', 'year', 'month', 'element'],
                       var_name='day',
                       value_name='temperature')
print(weather_test)
print()

new_weather = weather_test.pivot_table(index=['id', 'year', 'month', 'day'],
                                       columns='element',
                                       values='temperature',
                                       dropna=False)
print(new_weather.info())
print()

re_new_weather = new_weather.reset_index()
# pd.set_option('display.max_rows',None)
print(re_new_weather)

print('---------------------------------------------------------')

football = pd.read_csv('./data/Football teams.csv')
print(football)
print()

football_long = pd.melt(football,
                        id_vars=['Team', 'Tournament', 'Rating'],
                        var_name='Pass%',
                        value_name='Goal')

football_new = football_long[['Team', 'Tournament', 'Rating']]
football_new = football_new.drop_duplicates()

print(football_new)
print()
# print(football_long)
print(football_new[football_new.Tournament == 'Serie A'])
