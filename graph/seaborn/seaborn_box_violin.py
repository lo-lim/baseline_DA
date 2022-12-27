# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 그래프 객체 생성 (figure에 4개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 10))           # 그래프 크기 설정
ax1 = fig.add_subplot(2, 2, 1)               # 2행 2열 - 1번째 그래프
ax2 = fig.add_subplot(2, 2, 2)               # 2행 2열 - 2번째 그래프
ax3 = fig.add_subplot(2, 2, 3)               # 2행 2열 - 3번째 그래프
ax4 = fig.add_subplot(2, 2, 4)               # 2행 2열 - 4번째 그래프
 
# 박스 그래프 - 기본값
sns.boxplot(x='alive', y='age', data=titanic, ax=ax1) 

# 박스 그래프 - hue = 'sex' 변수를 추가하여 남녀 데이터를 구분하여 출력
sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2) 

# 바이올린 그래프 - 기본값
sns.violinplot(x='alive', y='age', data=titanic, ax=ax3) 

# 바이올린 그래프 - hue = 'sex' 변수를 추가하여 남녀 데이터를 구분하여 출력
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4) 

plt.show()