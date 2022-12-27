import numpy as np

data1=[6, 7.5, 8, 0, 1]
arr1=np.array(data1)           # 배열생성
print(arr1)
# [6.  7.5 8.  0.  1. ]
print(arr1.ndim)                # 1
print(arr1.dtype)               # float64
print(arr1.shape)               # (5,)

data2=[[1,2,3,4],[5,6,7,8]]     
arr2=np.array(data2)            # 배열생성
print(arr2)
# [[1 2 3 4]
#  [5 6 7 8]]
print(arr2.ndim)                # 2
print(arr2.dtype)               # int32
print(arr2.shape)               # (2, 4)

