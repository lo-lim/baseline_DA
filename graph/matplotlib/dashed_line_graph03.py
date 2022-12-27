# 점선 그래프 그리기

# 점선 : plot()함수에 linestyle='dashed' 추가
# 마커 표시 : plot()함수에 marker = 'o' 추가
# 마커 색깔 : plot()함수에 markerfacecolor = 'red'
# 마커 크기 : plot()함수에 markersize = 12

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]

plt.figure(figsize=(10,6))
plt.plot(x,y,color='green', linestyle='dashed', marker='o',
             markerfacecolor='red', markersize=12)
plt.show()