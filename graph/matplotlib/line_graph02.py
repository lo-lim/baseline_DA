# 선 그래프 그리기

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]

plt.figure(figsize=(10,6))          # 크기 설정
plt.plot(x,y,color='green')        # 선색깔: green
plt.show()