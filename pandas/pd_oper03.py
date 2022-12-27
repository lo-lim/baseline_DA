# pandas의 통계분석 함수

import pandas as pd

# 2012년 부터 2016년까지 우리나라 계절별 강수량 데이터 ( 단위 : mm )
table_data = {'봄' : [256.5, 264.3, 215.9, 223.2, 312.8],
              '여름' : [770.6, 567.5, 599.8, 387.1, 446.2],
              '가을' : [363.5, 231.2, 293.1, 247.7, 381.6],
              '겨울' : [139.3, 59.9, 76.9, 109.1, 108.1]}
columns_list = ['봄','여름','가을','겨울']
index_list = ['2012','2013','2014','2015','2016']

# index : 연도,  columns : 계절
df = pd.DataFrame(table_data, index=index_list, columns=columns_list)
print(df)

# axis 인자를 설정하지 않으면 기본값이 0이 설정됨
# axis = 0 이면 열(column)별로 합을 구함 : 각 계절별 강수량 합을 구함
# axis = 1 이면 행(row)별로 합을 구함 :  각 연도별 강수량 합을 구함

# 2012년 ~ 2016년 계절별 강수량의 합
print('계절별 강수량 합')
sum0 = df.sum(axis=0)
print(sum0)

# 2012년 ~ 2016년 연도별 강수량의 합
print('연도별 강수량 합')
sum1 = df.sum(axis=1)
print(sum1)

# 2012년 ~ 2016년 계절별 강수량 평균
print('계절별 강수량 평균')
mean0 = df.mean(axis=0)
print(mean0)

# 2012년 ~ 2016년 연도별 강수량 평균
print('연도별 강수량 평균')
mean1 = df.mean(axis=1)
print(mean1)

# describe() 함수를 이용하면, 평균, 표준편차, 최소값, 최대값 등을 한번에 구할수 있다.
describe = df.describe()
print(describe)