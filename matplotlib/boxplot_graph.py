# boxplot 그래프

import numpy as np
import matplotlib.pyplot as plt

# 3개의 난수 발생(s1, s2, s3)
# 평균값:loc옵션,  표준편차:scale 옵션, x축: 0 ~ 1000
s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)


# plt.figure(figsize=(10,6))
# plt.plot(s1, label='s1')
# plt.plot(s2, label='s2')
# plt.plot(s3, label='s3')
# plt.legend()
# plt.show()


# boxplot() 으로 출력
plt.figure(figsize=(10,6))
plt.boxplot((s1,s2,s3))
plt.grid()
plt.show()