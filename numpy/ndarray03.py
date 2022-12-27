import numpy as np

arr1=np.array([1,2,3], dtype=np.float64)
arr2=np.array([1,2,3], dtype=np.float32)
print(arr1.dtype)                   # float64
print(arr2.dtype)                   # float32

arr3=np.array([1,2,3,4,5])
print(arr3.dtype)                   # int32
float_arr3=arr3.astype(np.float64)  # int32  -> float64 자료형 변경
print(float_arr3)                   # [1. 2. 3. 4. 5.]         
print(float_arr3.dtype)             # float64

arr4=np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr4.dtype)                   # float64
int_arr4=arr4.astype(np.int32)      # float64 -> int32 자료형 변경
print(int_arr4)                     # [ 3 -1 -2  0 12 10]