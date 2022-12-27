# 데이터 연산
# pandas의 Series()로 생성한 데이터끼리 산술 연산을 할 수 있다.

import pandas as pd

#1. 원소의 갯수가 같은 경우
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])

print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)

#2. 원소의 갯수가 다른 경우
# 1)numpy의 배열은 원소의 갯수가 서로 다르면 산술연산을 할수 없지만,
#   pandas는 원소의 갯수가 달라도 산술연산할 수 있다. 
# 2)연산을 할 수 없는 경우는 NaN 으로 출력됨
s3 = pd.Series([1,2,3,4])
s4 = pd.Series([10,20,30,40,50])
print(s3+s4)
print(s3-s4)
print(s3*s4)
print(s3/s4)

