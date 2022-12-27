# 데이터프레임 데이터 추출하기
# 2011년 부터 2017년까지 노선별 KTX이용자 수(단위: 천명) 데이터

import numpy as np
import pandas as pd

KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX','호남선 KTX','경전선 KTX','전라선 KTX','동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, columns = col_list, index = index_list)
print(df_KTX)                                   # DataFrame 데이터 출력
print(df_KTX.index)                             # index 정보 출력
print(df_KTX.columns)                           # columns 정보 출력
print(df_KTX.values)                            # values 정보 출력

print(df_KTX.head())                            # DataFrame 데이터의 첫 5개 행 데이터 출력
print(df_KTX.head(3))                           # DataFrame 데이터의 첫 3개 행 데이터 출력

print(df_KTX.tail())                            # DataFrame 데이터의 마지막 5개 행 데이터 출력
print(df_KTX.tail(3))                           # DataFrame 데이터의 마지막 3개 행 데이터 출력

# 행의 index 번호로 데이터 추출
# DataFrame_data[행 시작위치 : 행 끝위치] : 행 시작위치 ~ 행 끝위치-1  까지의 행데이터 반환
# 행의 위치는 0부터 시작
print(df_KTX[1:2])                              # 1의 행 데이터 출력
print(df_KTX[2:5])                              # 2에서 4의 행 데이터 출력

# 행의 index 항목 이름으로 데이터 추출
# DataFrame_data.loc[index_name]
print(df_KTX.loc['2011'])                       # 2011년 행 데이터 추출

# 행의 index 항목 이름으로 구간을 지정해서 연속된 구간의 행 데이터 추출
# DataFrame_data.loc[start_index_name : end_index_name]
print(df_KTX.loc['2013' : '2016'])              # 2013년부터 2016년까지 행 데이터 추출

# 열(column) 항목 이름으로 데이터 추출
# DataFrame_data[column_name]
print(df_KTX['경부선 KTX'])                     # columns 항목중 '경부선 KTX'의 열 데이터 추출

# 하나의 열을 선택 후 index 범위의 데이터 추출
# DataFrame_data[column_name][index_name]
# DataFrame_data[column_name][index_pos]
print(df_KTX['경부선 KTX']['2012':'2014'])     # '경부선 KTX' 열을 선택한 후 2012년에서 2014년까지 데이터 추출
print(df_KTX['경부선 KTX'][2:5])                # '경부선 KTX' 열을 선택한 후 2행에서 4행 데이터 추출

# DataFrame 데이터 중에서 하나의 원소 선택하는 방법들
# 1. DataFrame_data.loc[index_name] [column_name]
print(df_KTX.loc['2016']['호남선 KTX'])                # 10622.0
# 2. DataFrame_data.loc[index_name : column_name]
print(df_KTX.loc['2016','호남선 KTX'])                # 10622.0
# 3. DataFrame_data[column_name][index_name]
print(df_KTX['호남선 KTX']['2016'])                    # 10622
# 4. DataFrame_data[column_name][index_pos]
print(df_KTX['호남선 KTX'][5])                          # 10622
# 5. DataFrame_data[column_name].loc[index_name]
print(df_KTX['호남선 KTX'].loc['2016'])                # 10622

# DataFrame 의 행과 열을 바꾸는 전치 행렬을 만들어 준다.
print(df_KTX.T)
