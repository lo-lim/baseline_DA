# x축, y축에 한글 라벨 설정

import matplotlib.pyplot as plt
import matplotlib

x = [1,2,3,4,5]
y = [1,2,3,4,5]

# 한글 라벨 설정 :  '맑은 고딕'으로 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

plt.xlabel('x축')        # x축 라벨
plt.ylabel('y축')        # y축 라벨
plt.plot(x,y)
plt.show()