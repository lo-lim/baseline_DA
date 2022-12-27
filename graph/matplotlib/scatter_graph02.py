# 산포도

# plot()함수 대신에 scatter()함수 사용함
# marker 의 모양 변경 : scatter()함수에 marker = '>' 추가
# marker의 크기 변경 :  s = 50
# x의 값에 따라 y축 값의 색상을 바꾸는 colormap 추가
# :scatter()함수에 c=colormap
# plt.colorbar()

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,9,8,3,2,4,3,4])

colormap = x

plt.figure(figsize=(10,6))
plt.scatter(x,y, s=50, c=colormap, marker='>')

plt.colorbar()
plt.show()