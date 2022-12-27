# pandas 막대그래프

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# '맑은 고딕'으로 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['axes.unicode_minus'] = False

grade_num = [5, 14, 12, 3]
students = ['A', 'B', 'C', 'D']

# columns 값 Student 가 범례로 출력
df_grade = pd.DataFrame(grade_num, index=students, columns = ['Student'])
print(df_grade)

grade_bar = df_grade.plot.bar(grid = True)
grade_bar.set_xlabel("학점")
grade_bar.set_ylabel("학생수")
grade_bar.set_title("학점별 학생 수 막대 그래프")
plt.show()