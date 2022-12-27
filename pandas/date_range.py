# 날짜 자동 생성 :  date_range()

import pandas as pd

# 시작 날짜(start)와 끝 날짜(end)를 지정해서 날짜 데이터 생성
date1 = pd.date_range(start='2019-01-01', end='2019-01-07')
print(date1)

# 시작 날짜(start)와 날짜 생성 기간(periods)을 7로 지정해서 날짜 데이터 생성
date2 = pd.date_range(start='2019-01-01', periods=7)
print(date2)

# 2일씩 증가하는 날짜 생성
date3 = pd.date_range(start='2019-01-01', periods=4, freq='2D')
print(date3)

# 1시간 주기로 10개의 시간을 생성
date4 = pd.date_range(start='2019-01-01 08:00', periods=10, freq='H')
print(date4)

# 30분 단위로 4개의 시간을 생성
date5 = pd.date_range(start='2019-01-01 10:00', periods=4, freq='30min')
print(date5)

# 10초 단위로 4개의 시간을 생성
date6 = pd.date_range(start='2019-01-01 10:00:00', periods=4, freq='10S')
print(date6)