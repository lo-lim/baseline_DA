# 파이 그래프

import matplotlib.pyplot as plt
import matplotlib

# '맑은 고딕'으로 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]

# 1.파이 그래프가 타원모양으로 출력
plt.pie(result)
plt.show()

# 2.파이 그래프의 너비와 높이를 1대 1로 출력(원모양) : figsize=(5,5)
plt.figure(figsize=(5,5))
plt.pie(result)
plt.show()

# 3.라벨과 비율 추가
plt.figure(figsize=(5,5))
plt.pie(result, labels= fruit, autopct='%.1f%%')
plt.show()

# 4.각도 90도에서 시작해서 시계방향으로 설정
plt.figure(figsize=(5,5))
plt.pie(result, labels= fruit, autopct='%.1f%%', startangle=90, counterclock = False)
plt.show()

# 5.그림자 효과 추가하고 사과 부채꼴만 강조
explode_value = (0.1, 0, 0, 0, 0)
plt.figure(figsize=(5,5))
plt.pie(result, labels= fruit, autopct='%.1f%%', startangle=90, counterclock = False, explode=explode_value, shadow=True)
plt.show()