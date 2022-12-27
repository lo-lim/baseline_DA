import numpy as np

arr3 = np.arange(5)
print(arr3)                         # [0 1 2 3 4]

sum = arr3.sum()                    # 배열 각 원소의 합
print(sum)                          # 10

mean = arr3.mean()                  # 배열 원소의 평균
print(mean)                         # 2.0

var = arr3.var()                    # 분산
print(var)                          # 2.0

std = arr3.std()                    # 표준편차
print(std)                          # 1.4142135623730951

max = arr3.max()                    # 최대값
print(max)                          # 4

min = arr3.min()                    # 최소값
print(min)                          # 0

arr4 = np.arange(1, 5)
print(arr4)                         # [1 2 3 4]

cumsum = arr4.cumsum()              # 각 원소들의 누적합
print(cumsum)                       # [ 1  3  6 10]

cumprod = arr4.cumprod()            # 각 원소들의 누적곱
print(cumprod)                      # [ 1  2  6  24]