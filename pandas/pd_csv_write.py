# 데이터프레임 데이터를 CSV 파일로 저장하기

import pandas as pd

df_WH = pd.DataFrame({'Weight':[62, 67, 55, 74],
                      'Height':[165, 177, 160, 180]},
                       index=['ID_1', 'ID_2', 'ID_3', 'ID_4'])
df_WH.index.name = 'User'           # index 이름을 User 로 변경
print(df_WH)

# 체질량 지수(BMI) = W / H * H
# 키의 경우 입력된 데이터가 cm 단위여서, m 단위로 변경하기 위해서 100으로 나눈다.
bmi = df_WH['Weight']/(df_WH['Height']/100)**2
print(bmi)                          # bmi 정보 출력

# bmi 정보를 df_WH 데이터 프레임에 추가한다.
df_WH['BMI'] = bmi      

print(df_WH)                        # df_WH 데이터프레임에 BMI 열이 추가됨

# bmi.csv 파일로 저장
df_WH.to_csv('bmi.csv', encoding='utf8')