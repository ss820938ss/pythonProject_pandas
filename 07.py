import folium
import folium as fol
import pandas as pd

# deagu_map = folium.Map(location=[35.87, 128.60], zoom_start=12)
# deagu_map.save('./save/deagu_map.html')
#
# deagu_map1 = folium.Map(location=[35.87, 128.60], zoom_start=12, tiles='Stamen Terrain')
# deagu_map1.save('./save/deagu_map1.html')
#
# deagu_map2 = folium.Map(location=[35.87, 128.60], zoom_start=15, tiles='Stamen Toner')
# deagu_map2.save('./save/deagu_map2.html')

print('---------------------------------------------------------')

df = pd.read_excel('./data/영남인재교육원위치.xlsx')
print(df)

youngnam_map = folium.Map(location=[35.87, 128.60], zoom_start=13)

for name, lat, lng in zip(df['Unnamed: 0'], df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(youngnam_map)

youngnam_map.save('./save/youngman.html')

print('---------------------------------------------------------')

# 35.85716373645387, 128.55588171467303

# df = pd.DataFrame({'': ['두류역'],
#                    '위도': [35.85716373645387],
#                    '경도': [128.55588171467303]})
#
# writer = pd.ExcelWriter('./data/두류역좌표.xlsx', engine='xlsxwriter')
# df.to_excel(writer, sheet_name='Sheet1', index=False)
#
# writer.save()

df = pd.read_excel('./data/두류역좌표.xlsx')
print(df)

duryu_map = folium.Map(location=[35.87, 128.60], zoom_start=13)

for name, lat, lng in zip(df['Unnamed: 0'], df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(duryu_map)

duryu_map.save('./save/duryu.html')
