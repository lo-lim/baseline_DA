import numpy as np

# 1.문자를 원소로 갖는 numpy 배열 생성
str_a1 = np.array(['1.567','0.123','5.123','9','8'])
print(str_a1)                           # ['1.567' '0.123' '5.123' '9' '8']
print(str_a1.dtype)                     # <U5     유니코드 5자리(문자 5자리)

# astype()함수로 문자를 실수형으로 형변환
num_a1 = str_a1.astype(float)
print(num_a1)                           # [1.567 0.123 5.123 9.    8.   ]
print(num_a1.dtype)                     # float64

# 2.문자를 원소로 갖는 numpy 배열 생성
str_a2 = np.array(['1','3','5','7','9'])
print(str_a2)                           # ['1' '3' '5' '7' '9']
print(str_a2.dtype)                     # <U1     유니코드 1자리(문자 1자리)

# astype()함수로 문자를 정수형으로 형변환
num_a2 = str_a2.astype(int)
print(num_a2)                           # [1 3 5 7 9]
print(num_a2.dtype)                     # int32

# 3.실수를 원소로 갖는 numpy 배열 생성
num_f1 = np.array([10, 21, 0.549, 4.75, 5.98])
print(num_f1)                           # [10.    21.     0.549  4.75   5.98 ]
print(num_f1.dtype)                     # float64

# astype()함수로 실수를 정수형으로 형변환
num_i1 = num_f1.astype(int)
print(num_i1)                           # [10 21  0  4  5]
print(num_i1.dtype)                     # int32
