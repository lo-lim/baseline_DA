import numpy as np

# 2 x 2 행렬 A와 B 생성
A = np.array([0,1,2,3]).reshape(2,2)
B = np.array([3,2,0,1]).reshape(2,2)

# 행렬 곱
print(A.dot(B))
print(np.dot(A,B))
# [[0 1]
#  [6 7]]

# 행렬 A의 전치 행렬
print(A.transpose())
print(np.transpose(A))
# [[0 2]
#  [1 3]]

# 행렬 A의 역행렬
print(np.linalg.inv(A))
# [[-1.5  0.5]
#  [ 1.   0. ]]

# 행렬 A의 행렬식
print(np.linalg.det(A))             # -2.0