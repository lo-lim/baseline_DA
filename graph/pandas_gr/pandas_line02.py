# pandas의 선그래프

import pandas as pd
import matplotlib.pyplot as plt

# x축에 index값 날짜출력, y축에 Series 데이터 출력
s = pd.Series([1,2,3,4,5,6,7,8,9,10], index = pd.date_range('2019-01-01', periods=10))
print(s)

s.plot()
plt.show()

s.plot(grid=True)       # 격자모양 추가함
plt.show()