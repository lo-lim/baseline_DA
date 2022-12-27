# pandas 막대그래프

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 세트 만들기 (3개의 난수로 이루어진 10개의 배열)
data_set = np.random.rand(10,3)
print(data_set)

# pandas의 데이터프레임(DataFrame) 생성
df = pd.DataFrame(data_set, columns = ['A','B','C'])
print(df)

# 수직 막대 그래프 그리기
df.plot(kind='bar')
plt.show()

# 수평 막대 그래프 그래기 (horizontal)
df.plot(kind='barh')
plt.show()

# 영역 그래프 그래기
df.plot(kind='area', stacked=False)
plt.show()