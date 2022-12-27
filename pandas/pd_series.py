import numpy as np
import pandas as pd

# 1.스칼라(Scalar) 데이터
s1 = pd.Series(7, index=['a','b','c'])
print(s1)

# 2. 일차원 배열 데이터
s2 = pd.Series(np.random.randn(5))   # 난수 5개 발생
print(s2)

s3 = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
print(s3)

# 3. 리스트 데이터
s4 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s4)

# 딕셔너리 데이터
s5 = pd.Series({'국어':100, '영어':95, '수학':90})
print(s5)

