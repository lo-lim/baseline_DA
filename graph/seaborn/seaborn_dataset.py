# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# titanic 데이터셋 살펴보기
print(titanic.head(891))
print('\n')
print(titanic.info())

import pandas as pd
titanic.to_csv('titanic.csv', encoding='utf-8')
df = pd.read_csv('titanic.csv', encoding='utf-8')
print(df)
print(df.columns)
print(df['fare'].mean())
print(df['fare'])
