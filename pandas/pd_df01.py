# 데이터 프레임(DataFrame)

import numpy as np
import pandas as pd

#1.numpy로 1차원 배열 데이터로 DataFrame 생성
#  index와 columns 이  0,1,2 로 출력됨
data_list = np.array([[10,20,30],[40,50,60],[70,80,90]])
df1 = pd.DataFrame(data_list)
print(df1)

#2.index와 columns 를 지정된 날짜와 문자로 출력
data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index_date = pd.date_range('2019-09-01', periods=4)
columns_list = ['A','B','C']
df2 = pd.DataFrame(data, index=index_date, columns=columns_list)
print(df2)

#3.어느 회사의 연도 및 지사별 고객수 데이터
# 이 데이터를 딕셔너리 타입의 데이터로 만들어 보자
table_data = {'연도':[2015, 2016, 2016, 2017, 2017],
              '지사':['한국','한국','미국','한국','미국'],
              '고객수':[200, 250, 450, 300, 500]}
print(table_data)


# 딕셔너리 데이터를 이용해서 DataFrame 으로 만들어 보자
df3 = pd.DataFrame(table_data)
print(df3)
print(df3.index)        # RangeIndex(start=0, stop=5, step=1)
print(df3.columns)      # Index(['연도', '지사', '고객수'], dtype='object')
print(df3.values)