# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd
import folium
import webbrowser

# 대학교 리스트를 데이터프레임 변환 (에러 발생시  xlrd  모듈 설치)
# df = pd.read_excel('서울지역 대학교 위치.xlsx', sheet_name='Sheet1')
df = pd.read_excel('서울지역 대학교 위치.xlsx')
print(df.head())                                # 앞에서 5개의 데이터를 불러옴

# 대학교명이 저장된 컬럼명이 없으므로 collage로 추가
df.columns = ['collage', '위도', '경도']
# print(df)

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain',
                        zoom_start=12)

# 대학교 위치정보를 Marker로 표시
for name, lat, lng in zip(df.collage, df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)
# for index, row in df.iterrows():
#     folium.Marker([row['위도'], row['경도']], popup=row['collage']).add_to(seoul_map)

# 지도를 HTML 파일로 저장하기
seoul_collage = 'seoul_colleges.html'
seoul_map.save(seoul_collage)

# 웹브라우저로 지도 출력
webbrowser.open(seoul_collage)