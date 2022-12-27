# pandas 파이그래프

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 5개의 난수로 이루어진 데이터 생성
data = np.random.rand(5)
print(data)

# pandas 시리즈형 데이터로 변환
s = pd.Series(data, index=['a','b','c','d','e'], name='series')
print(s)

# pie 그래프 출력
s.plot(kind='pie', autopct='%.2f', figsize=(7,7))
plt.show()


