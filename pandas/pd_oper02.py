# 데이터 연산

# pandas의 DataFrame()으로 생성한 데이터끼리 산술 연산을 할 수 있다.

import pandas as pd

table_data1 = {'A' : [1, 2, 3, 4, 5],
               'B' : [10, 20, 30, 40, 50],
               'C' : [100, 200, 300, 400, 500]}

table_data2 = {'A' : [6, 7, 8],
               'B' : [60, 70, 80],
               'C' : [600, 700, 800]}

df1 = pd.DataFrame(table_data1)
print(df1)

df2 = pd.DataFrame(table_data2)
print(df2)

# 데이터프레임 데이터 df1과 df2의 길이지 같지 않아도 산술연산을 할 수 있다.
print(df1 + df2)
print(df1 - df2)
print(df1 * df2)
print(df1 / df2)