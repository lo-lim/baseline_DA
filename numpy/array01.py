import numpy as np

data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
print(a1)                                   # [0 1 2 3 4 5]
print(a1.dtype)                             # int32

data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
print(a2)                                   # [ 0.1  5.  4. 12. 0.5]
print(a2.dtype)                             # float64

a3 = np.array([0.5, 2, 0.01, 8])
print(a3)                                   # [0.5  2. 0.01 8. ]
print(a3.dtype)                             # float64

# 2차원 배열
a4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a4)
print(a4.dtype)
