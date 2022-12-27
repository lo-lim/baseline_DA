# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))               # 그래프 크기 설정
ax1 = fig.add_subplot(1, 3, 1)                  # 1행 3열 - 1번째 그래프
ax2 = fig.add_subplot(1, 3, 2)                  # 1행 3열 - 2번째 그래프
ax3 = fig.add_subplot(1, 3, 3)                  # 1행 3열 - 3번째 그래프
 
# 기본값 : 히스토그램 + 커널밀도함수
sns.distplot(titanic['fare'], ax=ax1) 

# hist=False : 커널밀도함수
sns.distplot(titanic['fare'], hist=False, ax=ax2) 

# kde=False : 히스토그램
sns.distplot(titanic['fare'], kde=False, ax=ax3)        

# 차트 제목 표시
ax1.set_title('titanic fare - hist/ked')     # 히스토그램 / 커널밀도함수
ax2.set_title('titanic fare - ked')          # 커널밀도함수
ax3.set_title('titanic fare - hist')         # 히스토그램

plt.show()