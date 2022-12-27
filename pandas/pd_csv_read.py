# CSV 파일 읽어오기

import pandas as pd

# sea_rain1.csv 파일을 DataFrame 데이터로 읽어온다.
df = pd.read_csv('sea_rain1.csv', encoding='utf-8')
print(df)

