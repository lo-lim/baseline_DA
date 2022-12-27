# pandas 기초

import numpy as np
import pandas as pd

# pandas 사용법

# 1. pd.Series()
# pandas 의 데이터 유형 중 기초가 되는 것이 Series 입니다.
# Series()는 대괄호로 만드는 파이썬의 list 데이터로 만들어 진다.
s = pd.Series([1,3,5,7,9])
print(s)


# 2. pd.date_range()
# pandas의 날짜형의 데이터인 date_range()
# date_range() 에 기본 날짜를 지정하고 periods 옵션으로 6일간을 지정함
dates = pd.date_range('20130101', periods=6)
print(dates)


# 3. pd.DataFrame()
# DataFrame 유형의 데이터를 생성함
# 6행 4열의 random변수를 만들고, 컬럼에는  columns=['A','B','C','D']
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
print(df)

# head() 함수는 기본적으로 5행을 출력하지만, head(3)은 3개의 데이터만 출력함
print(df.head(3))

# index 명령으로 pandas의 DataFrame 인덱스를 확인
print(df.index)

# columns 명령으로 pandas의 DataFrame 컬럼을 확인
print(df.columns)

# values 명령으로 pandas의 내용을 확인 (6행 4열의 난수)
print(df.values)

# info() 명령으로 DataFrame() 의 개요를 출력
df.info()

# describe() 명령으로 DataFrame() 의 통계적 개요를 확인
print(df.describe())

# sort_values() 명령으로 by로 지정된 컬럼을 기준으로 정렬합니다.
# ascending 옵션은 오름차순, 내림차순으로 정렬할 수 있습니다.
#( B컬럼을 기준으로 내림차순 정렬함 )
print(df.sort_values(by='B', ascending=False))


# DataFrame 의 전체내용 출력
print(df)

# DataFrame 의 'A' 컬럼 내용 출력
print(df['A'])

# DataFrame 의 0 ~ 3번째행 내용 출력
print(df[0:3])

# 2013.01.02부터 2013.01.04까지의 행을 출력
print(df['20130102':'20130104'])


# df.loc()명령으로 특정날짜(2013.01.01)의 데이터만 출력
# loc()는 location 옵션으로 원하는 날짜를 슬라이싱 한다.
print(df.loc[dates[0]])


# A, B열의 모든 행을 출력
print(df.loc[:,['A','B']])

# 2013년 1월 2일부터 2013년 1월 4일까지 데이터중 A와 B컬럼 데이터만 출력
print(df.loc['20130102':'20130104',['A','B']])


# 2013년 1월 2일의 A, B 컬럼 내용을 출력
print(df.loc['20130102',['A','B']])


# dates[0]에 맞는 날짜인 2013년 1월 1일 A컬럼 데이터 출력
print(df.loc[dates[0],'A'])


# iloc[] 명령을 사용하면 행이나 열의 범위를 지정할 수 있다.
# iloc[3] 은  4번째 행 데이터를 출력함 (행번호는 0번부터 시작)
print(df.iloc[3])


# 3번째 부터 4번째 행과 0번 부터 1번열 까지의 데이터를 구해옴
print(df.iloc[3:5,0:2])


# 0행,1행,3행과 0열,1열의 데이터를 구해옴
print(df.iloc[[1,2,4],[0,2]])


# 행(1행, 2행) 과 열(모든 열) 데이터 출력
# 콜론(:)은 전체를 의미함
print(df.iloc[1:3, :])


# 행(모든 행) 과 열(1열, 2열) 데이터 출력
print(df.iloc[:, 1:3])


# DataFrame의 전체 데이터 출력
print(df)

# DataFrame의 A컬럼 값이 0 보다 큰 데이터 출력
print(df[ df.A > 0 ])

# DataFrame의 값이 0 보다 큰 데이터 출력
# 조건을 만족하지 않은 곳은 NaN 으로 출력
print(df[df > 0])



# DataFrame 을 복사할 때는 copy() 함수를 사용한다.
df2 = df.copy()

# DataFrame에 새로운 컬럼을 추가
df2['E'] = ['one','one','two','three','four','three']
print(df2)

# isin() 함수는 df2 DataFrame의 E컬럼에서 two와 four가 있는지 판별한다.
# 있으면 True, 없으면 False를 출력함
print(df2['E'].isin(['two','four']))


# lambda 를 이용해서 최대값과 최소값의 차이를 출력
print(df.apply(lambda  x: x.max() - x.min()))
