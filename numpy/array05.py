import numpy as np

# 0.0 <= r1 < 1.0 사이의 실수형태의 난수 발생
r1 = np.random.rand()
print(r1)

# 0.0 <= r2 < 1.0 사이의 실수형태의 2행 3열 난수 발생
r2 = np.random.rand(2,3)
print(r2)

# 1 <= r3 < 30 사이의 정수형태의 난수 발생
r3 = np.random.randint(1,30)
print(r3)

# 0 <= r4 < 10 사이의 정수형태의 3행 4열 난수 발생
r4 = np.random.randint(10, size=(3, 4))
print(r4)