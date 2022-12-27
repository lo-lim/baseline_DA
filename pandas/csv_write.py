# 표 형식의 데이터를 CSV 파일로 저장하기

import pandas as pd


bmi = {'Weight' : [62, 67, 55, 74],
       'Height' : [165, 177, 160, 180],
       'index': ['ID_1','ID_2','ID_3','ID_4']
      }


df = pd.DataFrame(bmi)
print(df)

df.index.name = 'User'
print(df)
