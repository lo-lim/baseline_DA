# 데이터프레임 데이터 통합하기

import numpy as np
import pandas as pd

# 두 학급의 시험 점수가 담긴 DataFrame 생성
df1 = pd.DataFrame({'Class1': [95, 92, 98, 100],
                    'Class2': [91, 93, 97, 99]})
print(df1)

# 두 학급에 전학온 학생들의 점수 DataFrame 생성
df2 = pd.DataFrame({'Class1': [87, 89],
                    'Class2': [85, 90]})
print(df2)

# 1. 세로 방향으로 통합하기 : append() 함수 이용
# ignore_index=True 로 설정하지 않으면 기존 index 번호가 그대로 유지된다.
print(df1.append(df2))                          # 기존 index번호가 유지됨

# ignore_index=True 로 설정하면 새로운 index 번호가 할당된다.
print(df1.append(df2, ignore_index=True))       # 새로운 index번호가 할당됨

# 만약 columns 가 같지 않은 DataFrame 데이터를 append() 함수로 추가하면
# 데이터가 없는 부분은 NaN 으로 채워진다.
# 이를 확인하기 위해서 열(column)이 하나만 있는 DataFrame df3를 생성
df3 = pd.DataFrame({'Class1': [96, 83]})
print(df3)

# 열(column)이 두 개인 DataFrame df2에 열(column)이 하나인 DataFrame df3를 추가
print(df2.append(df3, ignore_index=True))       # 데이터가 없는 부분은 NaN 으로 채워짐


# 2. 가로 방향으로 통합하기 : join() 함수 이용
# df1과 index방향으로 크기가 같은 DataFrame 생성
df4 = pd.DataFrame({'Class3': [93, 91, 95, 98]})
print(df4)

# df1에 join()함수를 이용해서 df4를 가로방향으로 추가
print(df1.join(df4))

# index라벨을 지정한 DataFrame 데이터의 경우에도 index 가 같으면 join() 함수를
# 이용해서 가로방향으로 데이터를 추가할 수 있다.
index_label = ['a','b','c','d']
df1a = pd.DataFrame({'Class1' : [95, 92, 98, 100],
                     'Class2' : [91, 93, 97, 99]}, index=index_label)
df4a = pd.DataFrame({'Class3' : [93, 91, 95, 98]}, index=index_label)
print(df1a.join(df4a))

# index의 크기가 다은 DataFrame 데이터를 join() 함수를 이용해서 추가하면,
# 데이터가 없는 부분은 NaN으로 채워진다.
df5 = pd.DataFrame({'Class4': [82, 92]})
print(df5)

# index의 크기가 2인 DataFrame df5 를 join()함수를 이용해 index 크기가 4인 DataFrame df1에 추가
print(df1.join(df5))


# 3. 특정 열을 기준으로 통합하기
# 1월부터 4월까지 제품 A와 B의 판매량 데이터를 변수 df_A_B 에 할당하고, 같은 기간 동안
# 제품 C와 D의 판매량 데이터를 변수 df_C_D 에 할당
df_A_B = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                       '제품A': [100, 150, 200, 130],
                       '제품B': [90, 110, 140, 170]})
print(df_A_B)

df_C_D = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                       '제품C': [112, 141, 203, 134],
                       '제품D': [90, 110, 140, 170]})
print(df_C_D)

# 두 DataFrame 의 공통 컬럼인 '판매월'을 중심으로 DataFrame 데이터를 통합
print(df_A_B.merge(df_C_D))

# 특정 열을 기준으로 일부만 공통 데이터를 가진 DataFrame 데이터를 통합한 예
df_left = pd.DataFrame({'key':['A','B','C'], 'left': [1, 2, 3]})
print(df_left)
df_right = pd.DataFrame({'key':['A','B','D'], 'right': [4, 5, 6]})
print(df_right)

print(df_left.merge(df_right, how='left', on = 'key'))      # 왼쪽을 먼저 선택
print(df_left.merge(df_right, how='right', on = 'key'))     # 오른쪽을 먼저 선택
print(df_left.merge(df_right, how='outer', on = 'key'))     # 양쪽을 모두 선택
print(df_left.merge(df_right, how='inner', on = 'key'))     # 공통 항목만 선택
