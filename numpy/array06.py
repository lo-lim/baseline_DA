import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

a1 = arr1 + arr2                # 배열 더하기 : 각 원소끼리 더하기
print(a1)                       # [11 22 33 44]

a2 = arr1 - arr2                # 배열 빼기: 각 원소끼리 빼기
print(a2)                       # [ 9 18 27 36]

a3 = arr2 * 2                   # 배열에 상수 곱하기
print(a3)                       # [2 4 6 8]

a4 = arr2 ** 2                  # 배열에 거듭제곱
print(a4)                       # [ 1  4  9 16]

a5 = arr1 * arr2                # 배열 곱하기 : 각 원소끼리 곱함
print(a5)                       # [ 10  40  90 160]

a6 = arr1 / arr2                # 배열 나누기 : 각 원소끼리 나눔
print(a6)                       # [10. 10. 10. 10.]

a7 = arr1 / (arr2 ** 2)         # 복합 연산
print(a7)                       # [ 10. 5. 3.33333333  2.5 ]

# 비교연산 : 각 원소와 비교해서 참이면 True, 거짓이면 False 리턴
a8 = arr1 > 20                  
print(a8)                       # [False  False  True  True]