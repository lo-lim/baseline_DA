import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 50개의 난수로 이루어진 데이터 생성
data = np.random.rand(50)
print(data)

# pandas 시리즈형 데이터로 변환
s = pd.Series(data)
print(s)

# 선형 그래프 그리기
s.plot()
plt.show()