import numpy as np

# np.arange(start, stop, step)
a1 = np.arange(0, 10, 2)
print(a1)                           # [0 2 4 6 8]

# np.arange(start, stop)
a2 = np.arange(1, 10)
print(a2)                           # [1 2 3 4 5 6 7 8 9]

# np.arange(stop)
a3 = np.arange(5)
print(a3)                           # [0 1 2 3 4]

# arange(12)로 12개의 숫자 생성후 reshape(4,3)으로 4x3 행렬을 만든다.
a4 = np.arange(12).reshape(4, 3)
print(a4)                           # [[ 0  1  2]
                                    #  [ 3  4  5]
                                    #  [ 6  7  8]
                                    #  [ 9 10 11]]
print(a4.shape)                     # (4, 3)       4행 3열 행렬

# linspace(start, stop, num)
# 1부터 10까지 10개의 데이터 생성
a5 = np.linspace(1, 10, 10)
print(a5)                           # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

# 1부터 10까지 3개의 데이터 생성
a6 = np.linspace(1, 10, 3)
print(a6)                           # [ 1. 5.5  10. ]

# 0부터 pie 까지 동일한 간격으로 나눈 20개의 데이터를 생성
a7 = np.linspace(0, np.pi, 20)
print(a7)

# [0.         0.16534698 0.33069396 0.49604095 0.66138793 0.82673491
#  0.99208189 1.15742887 1.32277585 1.48812284 1.65346982 1.8188168
#  1.98416378 2.14951076 2.31485774 2.48020473 2.64555171 2.81089869
#  2.97624567 3.14159265]