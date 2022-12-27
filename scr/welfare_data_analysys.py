# SPSS 파일을 읽어오기 위해서  pyreadstat 모듈 설치
# pip  install  pyreadstat


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
raw_welfare = pd.read_spss('Data/Koweps_hpwc14_2019_beta2.sav')

# 복사본 만들기
welfare = raw_welfare.copy()

# 데이터 검토하기
print(welfare)                          # 데이터 앞부분, 뒷부분 출력
print(welfare.shape)                    # 행, 열 갯수 출력   [14418 rows x 830 columns]
                                        #                 (14418, 830)
print(welfare.info())                   # 변수 속성 출력
print(welfare.describe())               # 요약 통계량 출력

# 변수명 변경하기
welfare = welfare.rename(
    columns={'h14_g3'     : 'sex',              # 성별
             'h14_g4'     : 'birth',            # 태어난 연도
             'h14_g10'    : 'marriage_type',    # 혼인 상태
             'h14_g11'    : 'religion',         # 종교 유무
             'p1402_8aq1' : 'income',           # 월급
             'h14_eco9'   : 'code_job',         # 직업 코드
             'h14_reg7'   : 'code_region'})     # 지역 코드

# -----------------------------------------------------------------------------
# 맑은 고딕 폰트 설정 : 한글 제목 출력 하기 위해서 설정한다.
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family' : 'Malgun Gothic'})

#Q1. 성별에 따른 월급 차이
#    성별에 따라 월급이 얼마나 다를까?

# 1) 변수 검토 하기
# sex 변수의 데이터 타입
print(welfare['sex'].dtype)                     # 변수의 데이터 타입 출력 : float64

# 2) 전처리
# sex 변수의 빈도 구하기
print(welfare['sex'].value_counts())
# 2.0    7913                                   # 2 : 여자
# 1.0    6505                                   # 1 : 남자
# Name: sex, dtype: int64                       # 9 : 모름 / 무응답

# sex 변수는 1과 2만 있고 9나 다른 값은 없다.
# sex 변수에 이상치가 없으므로, 이상치를 결측 처리하지 않아도 된다.
# 만약 이상치가 있다면, 이상치를 결측 처리하는 작업을 해야한다.

# 이상치를 결측처리 : 이상치가 없으므로 생략
welfare['sex'] = np.where(welfare['sex'] == 9, np.nan, welfare['sex'])

# 결측치 확인
print(welfare['sex'].isna().sum())             # 0 : 결측치 없음

# 성별 변수의 값 수정 :  1 -> male,  2 -> female
welfare['sex'] = np.where(welfare['sex'] == 1, 'male', 'female')

# 성별 빈도 구하기
print(welfare['sex'].value_counts())
# female    7913                            여자
# male      6505                            남자
# Name: sex, dtype: int64
                                                
# 3) 변수 검토 하기
# income 변수의 데이터 타입
print(welfare['income'].dtype)                  # float64

# income 변수의 요약 통계량 확인
print(welfare['income'].describe())
# count    4534.000000
# mean      268.455007
# std       198.021206
# min         0.000000
# 25%       150.000000
# 50%       220.000000
# 75%       345.750000
# max      1892.000000
# Name: income, dtype: float64

# income 의 분포를 히스토그램으로 분포 확인
sns.histplot(data=welfare, x='income')
plt.title('income 분포')
plt.show()
# 0 ~ 250만원에 가장 많은 사람들이 분포하고, 그 뒤로는 점점 빈도가 감소한다.

# 4) 전처리 하기
# 월급의  단위는 '만원' 이고, 모름/무응답은 9999 로 되어 있다.

# income 의 이상치 확인
print(welfare['income'].describe())
# count    4534.000000
# mean      268.455007
# std       198.021206
# min         0.000000
# 25%       150.000000
# 50%       220.000000
# 75%       345.750000
# max      1892.000000
# Name: income, dtype: float64

# income의 최소값이 0이고, 최대값이 1892 이다.
# income의 이상치는 없다.
# income의 이상치가 없으므로, 이상치를 결측으로 처리하지 않아도 된다.

# income 의 결측치 확인
print(welfare['income'].isna().sum())         # 결측치 : 9884
# 직업이 없어서 월급을 받지 않는 응답자가 있으므로 결측치 9884개 있다.

# 이상치가 있는 경우, 이상치를 결측치로 처리하기 : 생략 가능
welfare['income'] = np.where(welfare['income'] == 9999, np.nan, welfare['income'])

# 5) 분석하기
# 성별 월급 평균표를 만들어 성별에 따른 평균 월급의 차이를 비교해 보자

# 성별 월급 평균표 만들기 : # income 결측치 제거  # sex 별로 분리해서 처리
sex_income = welfare.dropna(subset = ['income'])\
    .groupby('sex', as_index=False)\
    .agg(mean_income = ('income', 'mean'))              # income 평균 구하기
print(sex_income)
#       sex      mean_income
# 0     female   186.293096
# 1     male     349.037571

# 남자 평균 월급은 349만원, 여자 평균 월급은 186만원으로 남자가 여자보다 약 163만원 더 많다.

# 6) 그래프 그리기
# 성별 평균 월급을 막대 그래프로 출력해보자.

# 막대 그래프 그리기
sns.barplot(data = sex_income, x = 'sex', y = 'mean_income')
plt.title('성별 평균 월급')
plt.show()

# -----------------------------------------------------------------------------
#Q2. 나이와 월급과의 관계
#    몇살때 월급을 가장 많이 받을까?

# 1) 변수 검토하기

# birth(태어난 연도) 변수 데이터 타입
print(welfare['birth'].dtype)                   # float64

# birth 변수의 요약 통계 구하기
print(welfare['birth'].describe())
# count    14418.000000
# mean      1969.280205
# std         24.402250
# min       1907.000000
# 25%       1948.000000
# 50%       1968.000000
# 75%       1990.000000
# max       2018.000000
# Name: birth, dtype: float64

# 히스토그램 만들기
sns.histplot(data=welfare, x = 'birth')
plt.title('birth 분포')
plt.show()

# 2) 전처리
# 태어난 연도는 '모름/무응답' 일 경우 9999로 처리되어 있다.

# 이상치 확인
print(welfare['birth'].describe())                      # 이상치 없음

# 결측치 확인
print(welfare['birth'].isna().sum())                    # 0 : 결측치 없음

# 만약 이상치가 있으면, 이상치를 결측으로 처리해야 한다.(생략)
welfare['birth'] = np.where(welfare['birth'] == 9999, np.nan, welfare['birth'])

# 3) 파생변수 만들기 - 나이
# 태어난 연도를 이용해서 파생변수 나이를 구해보자.
# 2019년 데이터이므로 2019년에서 태어난 연도를 뺀 다음 1을 더해서 나이를 구하면 된다.

# 파생변수 만들기 : 나이(age)
welfare = welfare.assign(age = 2019 - welfare['birth'] + 1)     # 나이(age) 변수 만들기
print(welfare['age'].describe())

# 나이(age) 히스토그램 만들기
sns.histplot(data = welfare, x = 'age')
plt.title('age 분포')
plt.show()

# 4) 나이별 평균 월급표 만들기 : # income 결측치 제거, # age별 분리, # income 평균 구하기
age_income = welfare.dropna(subset=['income']).groupby('age').agg(mean_income = ('income', 'mean'))
print(age_income.head())                                    # 앞에서 부터 5개만 출력
#        mean_income
# age
# 19.0   162.000000
# 20.0   121.333333
# 21.0   136.400000
# 22.0   123.666667
# 23.0   179.676471

# 5) 그래프 만들기
# x축은 나이, y축을 월급으로 지정하고 나이에 따른 월급의 변화를 선그래프로 그려보자.

# 선그래프 만들기
sns.lineplot(data = age_income, x = 'age', y = 'mean_income')
plt.title('나이별 평균 월급')
plt.show()

# 20대 초반에 월급을 150만원 가량 받고 이후 점점 지속해서 증가하는 추세를 보입니다.
# 40대에 350만원 가량으로 가장 많이 받고 지속적으로 감소하다가 60대 후반부터는 20대보다 낮은 월급을 받는다.

# -----------------------------------------------------------------------------
#Q3. 연령대에 따른 월급 차이
#    어떤 연령대의 월급이 가장 많을까?

# 1) 파생변수 만들기 - 연령대
#  초년층 : 30세 미만
#  중년층 : 30 ~ 59세
#  노년층 : 60세 미만

# 나이 변수 살펴보기
print(welfare['age'].head())                    # 앞에서 부터 5개만 출력
# 0    75.0
# 1    72.0
# 2    78.0
# 3    58.0
# 4    57.0
# Name: age, dtype: float64

# 연령대 변수 만들기
welfare = welfare.assign(ageg = np.where(welfare['age'] < 30, 'young',
                                         np.where(welfare['age'] <= 59, 'middle', 'old')) )

# 연령대별 빈도 구하기
print("연령대별 빈도 구하기")
print(welfare['ageg'].value_counts())
# old       5955
# middle    4963
# young     3500
# Name: ageg, dtype: int64

# 연령대별 빈도 막대 그래프 그리기
sns.countplot(data = welfare, x = 'ageg')
plt.title('연령대별 빈도')
plt.show()

# 2) 연령대별 평균 월급표 만들기
# 연령대별 평균 월급표 만들기 : # income 결측치 제거, # ageg별로 분리해서 구하기, # income 평균 구하기
print("연령대별 평균 월급표 만들기")
ageg_income = welfare.dropna(subset=['income']).groupby('ageg', as_index=False).agg(mean_income = ('income', 'mean'))
print(ageg_income)
#      ageg   mean_income
# 0  middle   329.157157
# 1     old   140.129003
# 2   young   195.663424

# 3) 그래프 만들기
# 막대 그래프 만들기 : middle, old, young 순으로 출력됨
sns.barplot(data = ageg_income, x = 'ageg', y = 'mean_income')
plt.title('연령대별 평균 월급')
plt.show()

# 막대 그래프 만들기 : young, middle, old 순으로 출력 되도록 순서를 지정하자
sns.barplot(data = ageg_income, x = 'ageg', y = 'mean_income',
            order = ['young', 'middle', 'old'])
plt.title('연령대별 평균 월급')
plt.show()

# 중년층이 330만원 정도로 가장 많은 월급을 받고 있다.
# 노년층의 월급은 140만원, 초년생이 받는 월급은 195만원 이다.

# -----------------------------------------------------------------------------
#Q4. 연령대 및 성별 월급 차이
#    성별 월급 차이는 연령대별로 다를까?

# 1) 연령대 및 성별 평균 월급표 만들기
# 연령대 및 성별 평균 월급표 만들기 : # income 결측치 제거, # ageg 및 sex별로 분리해서 구함, # income 의 평균 구하기
print("연령대 및 성별 평균 월급표 만들기")
sex_income = welfare.dropna(subset=['income'])\
    .groupby(['ageg', 'sex'], as_index=False)\
    .agg(mean_income = ('income', 'mean'))
print(sex_income)
#      ageg     sex   mean_income
# 0  middle  female   230.481735
# 1  middle    male   409.541228
# 2     old  female    90.228896
# 3     old    male   204.570231
# 4   young  female   189.822222
# 5   young    male   204.909548

# 2) 그래프 만들기
# 막대 그래프 만들기
# x축에 ageg, 막대 색깔이 성별에 따라 다르도록 hue 속성에 sex를 지정한다.
# x축 순서는 order를 이용해서 연령대 순으로 설정한다.

sns.barplot(data = sex_income, x = 'ageg', y = 'mean_income', hue = 'sex',
            order = ['young', 'middle', 'old'])
plt.title('연령대별 성별 평균 월급')
plt.show()

# 성별 월급 차이의 양상이 연령대별로 다르다.
# 초년에는 월급의 차이가 크지 않다가 중년에 크게 벌어져 남성이 여성보다 179만원 가량 더 많다.
# 노년에는 월급의 차이가 줄어들지만, 여전히 남성이 여성보다 114만원 가량 더 많다.

# 나이 및 성별 평균 월급표 만들기 : # income 결측치 제거, # age 및 sex 별로 분리해서 구하기, # income 평균 구하기
print("나이 및 성별 평균 월급표 만들기")
sex_age = welfare.dropna(subset=['income']).groupby(['age', 'sex'], as_index=False).agg(mean_income = ('income', 'mean'))
print(sex_age.head())
#    age     sex    mean_income
# 0  19.0    male   162.000000
# 1  20.0  female    87.666667
# 2  20.0    male   155.000000
# 3  21.0  female   124.000000
# 4  21.0    male   186.000000

# 선그래프 만들기
sns.lineplot(data = sex_age, x = 'age', y = 'mean_income', hue = 'sex')
plt.title('나이 및 성별 평균 월급')
plt.show()

# 남성의 월급은 50세 전후까지 급격하게 증가하다가 급격하게 감소하는 반면에 여성은 30세 초반까지 약간 증가하다가 이후에는 완만하게 감소한다.
# 성별 월급 격차는 30대 중반부터 벌어지다가 50대에 가장 크게 벌어지고, 이후로 점점 줄어들어 80대가 되면 비슷한 수준이 된다.

# -----------------------------------------------------------------------------
#Q5. 직업별 월급 차이
#    어떤 직업이 월급을 가장 많이 받을까?

# 1) 변수 검토 하기
# 직업코드가 저장된 code_job 변수 타입 출력
print(welfare['code_job'].dtype)                        # float64

# code_job 변수의 빈도 구하기
print(welfare['code_job'].value_counts())
# 611.0    962
# 941.0    391
# 521.0    354
# 312.0    275
# 873.0    236
#         ...
# 112.0      2
# 784.0      2
# 423.0      1
# 861.0      1
# 872.0      1
# Name: code_job, Length: 150, dtype: int64

# 2) 전처리하기
# code_job은 직업 코드이기 때문에, '직업분류코드 목록' 파일을 읽어 와서 code_job 대신에 직업명으로 처리해보자.

# 엑셀 파일을 읽어오기 위한 openpyxl 모듈 설치
# pip  install openpyxl

# 직업붙류코드 목록 파일 불러오기
list_job = pd.read_excel('Data/Koweps_Codebook_2019.xlsx', sheet_name='직종코드')
print(list_job.head())
#      code_job               job
# 0       111      의회 의원∙고위 공무원 및 공공단체 임원
# 1       112      기업 고위 임원
# 2       121      행정 및 경영 지원 관리자
# 3       122      마케팅 및 광고∙홍보 관리자
# 4       131      연구∙교육 및 법률 관련 관리자

print(list_job.shape)                   # 156행  2열
# (156, 2)

# welfare 데이터프레임에 list_job 데이터프레임을 merge() 함수로 합쳐보자.
# welfare와 list_job의 공통적으로 들어있는 code_job 변수를 기준으로 결합하면 된다.

# welfare에 list_job 결합하기
welfare = welfare.merge(list_job, how = 'left', on = 'code_job')

# welfare에  code_job, job 변수가 잘 결합되었는지 확인

# code_job 결측치 제거하고, code_job, job 출력
print(welfare.dropna(subset=['code_job'])[['code_job', 'job']].head())
#       code_job       job
# 2      762.0        전기공
# 3      855.0        금속기계 부품 조립원
# 7      941.0        청소원 및 환경미화원
# 8      999.0        기타 서비스 관련 단순 종사자
# 14     312.0        경영 관련 사무원

# welfare에 직업 이름으로된 job변수가 결합된 것을 확인할 수 있다.

# 3) 직업별 월급차이 분석하기
# 직업별 월급 평균표 만들기 : # job, income 결측치 제거, # job별 분리해서 처리, # income 평균 구하기
job_income = welfare.dropna(subset=['job', 'income'])\
    .groupby('job', as_index=False)\
    .agg(mean_income=('income','mean'))
print(job_income.head())
#         job                        mean_income
# 0      가사 및 육아 도우미             92.455882
# 1      간호사                        265.219178
# 2      감정∙기술영업및중개관련종사자      391.000000
# 3      건물 관리원 및 검표원            168.375000
# 4      건설 및 광업 단순 종사자         261.975000

# 4) 그래프 만들기
# 월급이 가장 많은 직업 상위 10개 추출
# 월급을 기준으로 내림차순 정렬하고, 상위 10개 직업을 추출하자

# 상위 10개 추출
print('--월급이 많은 직업 top10--')
top10 = job_income.sort_values('mean_income', ascending=False).head()
print(top10)
#        job                        mean_income
# 98    의료 진료 전문가               781.000000
# 60    법률 전문가                   776.333333
# 140   행정 및 경영 지원 관리자        771.833333
# 63    보험 및 금융 관리자            734.750000
# 110    재활용 처리 및 소각로 조작원    688.000000

# 그래프에 한글 직업에 잘 출력되도록 폰트 설정을 하자

# 맑은 고딕 폰트 설정
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family' : 'Malgun Gothic'})

# macOS 사용자는 'Malgun Gothic' 대신에 'AppleGothic'을 입력한다.

# 직업 이름이 길기 때문에 x축에 직업 이름을 설정하면 서로 겹쳐져서 알아볼 수 없다.
# 직업 이름을 y축, 평균 월급을 x축에 지정해서 그래프를 만들어서 출력하자.

# 막대 그래프 만들기
sns.barplot(data = top10, y = 'job', x = 'mean_income')
plt.title('월급이 많은 직업 top10')
plt.show()

# 출력된 표와 그래프를 보면 '의료 진료 전문가'의 평균 월급이 781만원으로 가장 많았고,
# 그 뒤로 '법률 전문가', '행정 및 경영 지원 관리자', '보험 및 금융 관리자' 순으로 월급이 많다.

# 월급이 가장 적은 직업 상위 10개 추출
# 월급을 기준으로 오름차순 정렬하고, 하위 10개 직업을 추출하자

# 하위 10개 추출
print('--월급이 적은 직업 top10--')
bottom10 = job_income.sort_values('mean_income').head()
print(bottom10)
#                                             job  mean_income
# 33   기타 돌봄∙보건 및 개인 생활 서비스 종사자      73.964286
# 34   기타 서비스 관련 단순 종사자                 77.789474
# 128  청소원 및 환경미화원                       88.461756
# 0    가사 및 육아 도우미                        92.455882
# 43   돌봄 및 보건 서비스 종사자                  117.162338

# 막대 그래프 만들기
# x축(평균 급여)의 범위를 0 ~ 800 으로 제한하자.
# sns.barplot(data = bottom10, y = 'job', x = 'mean_income')      # 급여 범위(0 ~ 120) 출력
sns.barplot(data = bottom10, y = 'job', x = 'mean_income').set(xlim = (0, 800))  # 0 ~ 800범위 출력
plt.title('월급이 적은 직업 top10')
plt.show()

# 그래프 출력 결과  '기타 돌봄∙보건 및 개인 생활 서비스 종사자' 의 평균 월급이 73만원으로 가장 적고,
# 그 뒤로 '기타 서비스 관련 단순 종사자', '청소원 및 환경미화원', '가사 및 육아 도우미' 순으로 적었다.

# -----------------------------------------------------------------------------
#Q6. 성별 직업 빈도
#    성별로 어떤 직업이 가장 많을까?

# 1) 성별 직업 빈도표 만들기
# 성별 직업별 빈도를 구해서 상위 10개를 추출해보자

# 남성 직업 빈도 상위 10개 추출 : #1.job 결측치 제거, #2.male 추출, #3.job별 분리해서 처리, #4.job의 빈도 구하기, #5.내림차순 정렬, #6.상위 10개 추출
print('남성 직업 빈도 상위 10개')
job_male = welfare.dropna(subset = ['job']) \
    .query('sex == "male"') \
    .groupby('job', as_index = False) \
    .agg(n =('job', 'count')) \
    .sort_values('n', ascending = False) \
    .head(10)
print(job_male)
#                 job           n
# 107  작물 재배 종사자           486
# 104  자동차 운전원              230
# 11   경영 관련 사무원           216
# 46   매장 판매 종사자           142
# 89   영업 종사자               113
# 127  청소원 및 환경미화원        109
# 4    건설 및 광업 단순 종사자     96
# 120  제조 관련 단순 종사자       80
# 3    건물 관리원 및 검표원       79
# 141          행정 사무원       74

# 여성 직업 빈도 상위 10개 추출 : #1.job 결측치 제거, #2.female 추출, #3.job별 분리해서 처리, #4.job의 빈도 구하기, #5.내림차순 정렬, #6.상위 10개 추출
print('여성 직업 빈도 상위 10개')
job_female = welfare.dropna(subset = ['job'])\
    .query('sex == "female"')\
    .groupby('job', as_index = False)\
    .agg(n =('job', 'count'))\
    .sort_values('n', ascending = False)\
    .head(10)
print(job_female)
#              job                 n
# 83     작물 재배 종사자            476
# 91     청소원 및 환경미화원         282
# 33     매장 판매 종사자            212
# 106    회계 및 경리 사무원          163
# 31     돌봄 및 보건 서비스 종사자    155
# 87     제조 관련 단순 종사자        148
# 73     음식 관련 단순 종사자        126
# 58     식음료 서비스 종사자         117
# 88     조리사                    114
# 24     기타 서비스 관련 단순 종사자   97

# 2) 그래프 만들기
# 앞에서 만들 직업 빈도표를 이용해서 남성 및 여성 직업 빈도를 막대 그래프로 만들어 보자.
# 두 그래프를 비교하기 위해서 x축 범위를 0 ~ 500으로 설정한다.

# 남성 직업 빈도 막대 그래프 만들기
sns.barplot(data = job_male, y = 'job', x = 'n').set(xlim = (0, 500))
plt.title('남성 직업 빈도 상위 10개')
plt.show()

# 여성 직업 빈도 막대 그래프 만들기
sns.barplot(data = job_female, y = 'job', x = 'n').set(xlim = (0, 500))
plt.title('여성 직업 빈도 상위 10개')
plt.show()

# 남녀 모두 '작물 재배 종사자'가 가장 많지만, 그 뒤로는 순위가 다르게 나타난다.
# 남성은 '자동차 운전원', '경영 관련 사무원', '매장 판매 종사자' 순으로 많은 반면에
# 여성은 '청소원 및 환경 미화원', '매장 판매 종사자', '회계 및 경리 사무원' 순으로 많습니다.

# -----------------------------------------------------------------------------
#Q7. 종교 유무에 따른 이혼율
#    종교가 있으면 이혼을 덜 할까?
# 종교가 있는 사람이 종교가 없는 사람보다 이혼을 덜 하는지 분석해보자.

# 1) 변수 검토하기 : religion(종교)
# religion(종교) 변수의 타입 확인
print(welfare['religion'].dtype)                    # float64

# religion(종교) 변수의 빈도 구하기
print(welfare['religion'].value_counts())
# 2.0    7815                                       # 종교 없음
# 1.0    6603                                       # 종교 있음
# Name: religion, dtype: int64

# 2) 전처리
# 1    종교 있음
# 2    종교 없음
# 9    모름/무응답

# 종교가 있으면 1, 종교가 없으면 2를 각각 yes와 no로 수정하자
welfare['religion'] = np.where(welfare['religion'] == 1, 'yes', 'no')

# 종교 유무의 빈도 구하기
print(welfare['religion'].value_counts())
# no     7815                                   # 종교 없음 ( 2 -> no )
# yes    6603                                   # 종교 있음 ( 1 -> yes )
# Name: religion, dtype: int64

# 종교 유무를 빈도 막대 그래프로 출력
sns.countplot(data = welfare, x = 'religion')
plt.title('종교 유무의 빈도')
plt.show()

# 3) 변수 검토하기 : marriage_type(혼인 상태)
# marriage_type(혼인 상태) 변수의 타입 확인
print(welfare['marriage_type'].dtype)                           # float64

# marriage_type(혼인 상태) 변수의 빈도 구하기
print(welfare['marriage_type'].value_counts())
# 1.0    7190                                  # 배우자 있음
# 5.0    2357
# 0.0    2121
# 2.0    1954
# 3.0     689                                  # 이혼
# 4.0      78
# 6.0      29
# Name: marriage_type, dtype: int64

# 4) 파생 변수 만들기
# 0  -  비해당(18세 미만)
# 1  -  유배우
# 2  -  사별
# 3  -  이혼
# 4  -  별거
# 5  -  미혼(18세 이상, 미혼모 포함)
# 6  -  기타(사망 등)

# 배우자가 있으면 1, 이혼했으면 3으로 되어있다.
# 이 관계를 이용해서 파생 변수를 만들어 보자 :  1 -> marriage,  3 -> divorce , 나머지 -> etc 변수로 생성
# 이혼 여부 파생변수 만들기
welfare['marriage'] = np.where(welfare['marriage_type'] == 1, 'marriage',
                      np.where(welfare['marriage_type'] == 3, 'divorce', 'etc') )

# 이혼 여부별 빈도 : #1.marriage별 구분해서 구하기, #2.marriage별 빈도 구하기
print('이혼 여부별 빈도')
n_divorce = welfare.groupby('marriage', as_index=False).agg(n = ('marriage', 'count'))
print(n_divorce)
#    marriage      n
# 0   divorce     689
# 1       etc     6539
# 2   marriage    7190

# 결혼 상태인 사람은 7190명, 이혼한 사람은 698명이다.
# 둘중 어디에도 속하지 않아 'etc'로 분류된 사람은 6539명이다. 이들은 분석 대상이 아니므로 이후 작업에서 제외하겠다.

# 이혼 여부별 빈도 막대 그래프
sns.barplot(data = n_divorce, x = 'marriage', y = 'n')
plt.title('이혼 여부별 빈도')
plt.show()

# 5) 종교 유무에 따른 이혼율 분석하기
# 종교 유무에 따른 이혼율표를 만들어보자.
# marriage가 'etc'인 경우를 제외하고, '종교 유무 및 이혼 여부별 비율'을 구해보자
# value_counts()에 normalize = True 를 입력하면 비율이 구해진다.

# 종교 유무에 따른 이혼율표 : #1.etc제외, #2.religion별로 구분해서 구하기, #3.marriage 추출, #4.비율 구하기
print('종교 유무에 따른 이혼율')
rel_div = welfare.query('marriage != "etc" ').groupby('religion', as_index = False)['marriage'].value_counts(normalize = True)
print(rel_div)
#   religion  marriage    proportion
# 0       no  marriage    0.905045
# 1       no  divorce     0.094955
# 2      yes  marriage    0.920469
# 3      yes  divorce     0.079531

# 6) 그래프 만들기
# round() 함수를 이용해서  proportion을 백분율로 바꾸고, 소숫점 첫째자리까지 반올림하자.
# 1.divorce 추출, #2.백분율로 바꾸기, #3.소수 첫째자리까지 구하기
print('종교 유무에 따른 이혼율')
rel_div = rel_div.query('marriage == "divorce" ').assign(proportion = rel_div['proportion']*100).round(1)
print(rel_div)
#   religion  marriage    proportion
# 1       no  divorce         9.5
# 3      yes  divorce         8.0

# 종교 유무에 따른 이혼율을 막대 그래프로 출력
sns.barplot(data = rel_div, x = 'religion', y = 'proportion')
plt.title('종교 유무에 따른 이혼율')
plt.show()

# 출력한 표와 그래프를 보면 이혼율은 종교가 있으면 8.0%, 종교가 없으면 9.5% 이다.
# 따라서 종교가 있는 사람이 이혼을 덜 한다고 볼 수 있다.

# 7) 연령대 및 종교 유무에 따른 이혼율 분석하기
# 이번에는 연령대별로 나누어 종교 유무에 따른 이혼율이 연령대별로 어떻게 다른지 알아보자.

# 연령대별 이혼율표 만들기 : #1.etc제외, #2.ageg별로 구분해서 구하기, #3.marriage 추출, #4.비율 구하기
print('연령대별 이혼율')
age_div = welfare.query('marriage != "etc" ').groupby('ageg', as_index = False)['marriage'].value_counts(normalize = True)
print(age_div)
#      ageg   marriage    proportion
# 0  middle   marriage    0.910302
# 1  middle   divorce     0.089698
# 2     old   marriage    0.914220
# 3     old   divorce     0.085780
# 4   young   marriage    0.950000
# 5   young   divorce     0.050000

# 연령대별 이혼율은 중년이 8.9%로 가장 높고 그 뒤로는 노년층 8.5%, 초년층이 5% 순으로 높다.
# 그런데 빈도를 구해보면 초년층은 결혼, 이혼 모두 다른 연령대에 비해서 사례가 적어서 이후 분석에서는 제외 하겠다.

# 연령대 및 이혼 여부별 빈도 : #1.etc제외, #2.ageg별 구분해서 구하기, #3.mariage 추출, #4.빈도 구하기
print('연령대 및 이혼 여부별 빈도')
ageg_count = welfare.query('marriage != "etc" ').groupby('ageg', as_index = False)['marriage'].value_counts()
print(ageg_count)
#      ageg  marriage   count
# 0  middle  marriage   3552
# 1  middle   divorce    350
# 2     old  marriage   3581
# 3     old   divorce    336
# 4   young  marriage     57
# 5   young   divorce      3

# 8) 연령대별 이혼율 그래프 만들기
# 앞에서 만든 age_div에서 초년층은 제외하고 처리하겠다.
# proportion을 백분율로 바꾸고 소숫점 첫째자리까지 반올림 처리한다.

# 연령대별 이혼율표 만들기 : #1.초년제외, 이혼제외, #2.백분율로 바꾸기, #3.반올림
print('연령대별 이혼율')
age_div = age_div.query('ageg != "young" & marriage == "divorce" ').assign(proportion = age_div['proportion']*100).round(1)
print(age_div)
#      ageg  marriage        proportion
# 1  middle  divorce         9.0
# 3     old  divorce         8.6

# 연령대별 이혼율 막대 그래프 출력
sns.barplot(data = age_div, x = 'ageg', y = 'proportion')
plt.title('연령대별 이혼율')
plt.show()

# 9) 연령대 및 종교 유무에 따른 이혼율표 만들기
# 연령대별 종교 유무에 따른 이혼율의 차이가 있는지 알아보자.
# 먼저 연령대, 종교 유무, 이혼 여부별 비율을 구해보자. 초년층은 제외하고 구한다.

# 연령대 및 종교 유무에 따른 이혼율표 만들기 : #1.etc제외, 초년제외, #2.ageg, religion별로 구분해서 구하기, #3.marriage 추출, #4.비율 구하기
print('연령대 및 종교 유무에 따른 이혼율표')
age_rel_div = welfare.query('marriage != "etc" & ageg != "young" ').groupby(['ageg','religion'], as_index=False)['marriage'].value_counts(normalize=True)
print(age_rel_div)
#      ageg religion  marriage    proportion
# 0  middle       no  marriage    0.904953
# 1  middle       no   divorce    0.095047
# 2  middle      yes  marriage    0.917520
# 3  middle      yes   divorce    0.082480
# 4     old       no  marriage    0.904382
# 5     old       no   divorce    0.095618
# 6     old      yes  marriage    0.922222
# 7     old      yes   divorce    0.077778

# 10) 연령대 및 종교 유무에 따른 이혼율 그래프 만들기
# 이혼에 해당하는 값만 추출한 다음 proportion을 백분율로 바꾸고, 소수 첫째자리까지 반올림하자.

# 연령대 및 종교 유무에 따른 이혼율표 : #1.divorce 추출, #2.백분율로 바꾸기, #3.반올림
print('연령대 및 종교 유무에 따른 이혼율표')
age_rel_div = age_rel_div.query('marriage == "divorce" ').assign(proportion = age_rel_div['proportion']*100).round(1)
print(age_rel_div)
#     ageg religion   marriage    proportion
# 1  middle       no  divorce         9.5
# 3  middle      yes  divorce         8.2
# 5     old       no  divorce         9.6
# 7     old      yes  divorce         7.8

# 연령대 및 종교 유무에 따른 이혼율을 막대 그래프로 출력
# age_rel_div를 이용해서 막대 그래프로 출력해보자.
# 종교 유무에 따라 막대 색깔을 다르게 표현하기 위해서 hue에 religion을 지정하자.
sns.barplot(data = age_rel_div, x = 'ageg', y = 'proportion', hue = 'religion')
plt.title('연령대 및 종교 유무에 따른 이혼율')
plt.show()

# 출력된 표와 그래프를 보면 중년과 노년 모두 종교가 없는 사람의 이혼율이 더 높은 것을 볼 수 있다.
# 중년은 1.3%, 노년은 1.8% 정도로 종교가 없는 사람의 이혼율이 더 높은 것을 볼 수 있다.

# -----------------------------------------------------------------------------
#Q8. 직업별 연령대 비율
#    어느 지역에 노인층이 많을까?

# 지역별 연령대 비율을 분석해서 어느 지역에 노년층이 많이 사는지 분석해보자.

# 1) 변수 검토 하기 : code_region(지역)
# code_region 변수의 타입 구하기
print(welfare['code_region'].dtype)                         # float64

# code_region 변수의 빈도 구하기
print(welfare['code_region'].value_counts())
# 2.0    3246
# 7.0    2466
# 3.0    2448
# 1.0    2002
# 4.0    1728
# 5.0    1391
# 6.0    1137
# Name: code_region, dtype: int64

# 2) 전처리 하기
# code_region 변수의 값은 7개 권역의 지역을 의미한다.
# 1 - 서울
# 2 - 수도권(인천/경기)
# 3 - 부산/경남/울산
# 4 - 대구/경북
# 5 - 대전/충남
# 6 - 강원/충북
# 7 - 광주/전남/전북/제주도

# code_region와 region을 가진 데이터프레임 생성하자.
# 지역 코드 목록을 가진 데이터 프레임
print('code_region과 region')
list_region = pd.DataFrame({'code_region' : [1,2,3,4,5,6,7],
                            'region' : ['서울','수도권(인천/경기)','부산/경남/울산','대구/경북','대전/충남','강원/충북','광주/전남/전북/제주도'] })
print(list_region)
#     code_region        region
# 0            1            서울
# 1            2    수도권(인천/경기)
# 2            3      부산/경남/울산
# 3            4         대구/경북
# 4            5         대전/충남
# 5            6         강원/충북
# 6            7  광주/전남/전북/제주도

# list_region과 welfare 데이터프레임에 동시에 들어있는 code_region 변수를 이용해서 welfare에 지역명(region) 변수 추가하기
# 지역명(region) 변수 추가하기
welfare = welfare.merge(list_region, how = 'left', on = 'code_region')
print(welfare[['code_region','region']].head())
#        code_region  region
# 0          1.0     서울
# 1          1.0     서울
# 2          1.0     서울
# 3          1.0     서울
# 4          1.0     서울

# 3) 지역별 연령대 비율 분석하기
# 지역별 연령대의 관계를 알아보자.

# 지역별 연령대 비율표 만들기 : #1.region별 구분해서 구하기, #2.ageg 추출, #3.비율 구하기
print('지역별 연령대 비율')
region_ageg = welfare.groupby('region', as_index=False)['ageg'].value_counts(normalize=True)
print(region_ageg)
#             region       ageg       proportion
# 0          강원/충북        old       0.459103
# 1          강원/충북     middle       0.308707
# 2          강원/충북      young       0.232190
# 3   광주/전남/전북/제주도     old       0.449311
# 4   광주/전남/전북/제주도  middle       0.317924
# 5   광주/전남/전북/제주도   young       0.232766
# ...생략...

# region_ageg의 proportion을 백분율로 바꾸고 소숫점 첫째자리까지 반올림하자.
print('지역별 연령대 비율')
region_ageg = region_ageg.assign(proportion = region_ageg['proportion']*100).round(1)
print(region_ageg)
#            region         ageg     proportion
# 0          강원/충북        old        45.9
# 1          강원/충북     middle        30.9
# 2          강원/충북      young        23.2
# 3   광주/전남/전북/제주도     old        44.9
# 4   광주/전남/전북/제주도  middle        31.8
# 5   광주/전남/전북/제주도   young        23.3
# ...생략...


# 4) 지역별 연령대 비율로 막대 그래프 만들기

# 4.1) 지역별 연령대 비율로 '수평 막대 그래프' 만들기
# region_ageg를 이용해 지역별 연령대 비율을 그래프로 출력 해보자.
# 지역명이 겹치지 않도록 y축에 region, x축에 proportion을 지정해 가로 막대 그래프를 만들어 보자.
# 연령대별로 막대의 색깔을 다르게 표현하도록 hue에 ageg를 지정한다.
sns.barplot(data = region_ageg, y = 'region', x = 'proportion', hue = 'ageg')
plt.title('지역별 연령대 비율')
plt.show()

# 4.2) 지역별 연령대 비율로 '누적 비율 막대 그래프' 만들기
# 지역끼리 비교하기 쉽도록 연령대별 막대를 누적한 '누적 비율 막대 그래프'를 만들어보자.

# 피벗(pivot) 만들기
# 행과 열을 회전해 표의 구성을 바꾸는 작업을 피벗(pivot)이라고 한다.
# 누적 막대 그래프를 만드는데 적합 하도록 프레임의 행과 열을 회전해 구성을 바꾼다.
# - 지역을 기준으로 회전하도록 index = 'region'을 입력
# - 연령대별로 열을 구성하도록 columns = 'ageg'를 입력
# - 각 항목 값을 비율로 채우도록 values = 'proportion'을 입력

# 행은 지역, 열은 연령대로 구성하여 지역 및 연령대별 비율을 나타낸다.
print('지역별 연령대 비율')
pivot_df = region_ageg[['region','ageg','proportion']].pivot(index='region', columns='ageg', values='proportion')
print(pivot_df)
# ageg            middle   old  youngㅕ
# region
# 강원/충북           30.9  45.9   23.2
# 광주/전남/전북/제주도 31.8  44.9   23.3
# 대구/경북           29.6  50.4   20.0
# 대전/충남           33.6  41.3   25.0
# 부산/경남/울산       33.4  43.8   22.9
# 서울               38.5  37.6   23.9
# 수도권(인천/경기)    38.8  32.5   28.7

# 누적 비율 막대 그래프
# 가로 막대 그래프를 만들도록 df.plot_barh()를 이용하고, 막대를 누적하도록 stacked = true를 입력 한다.
pivot_df.plot.barh(stacked = True)
plt.title('지역별 연령대 비율(정렬 전)')
plt.show()

# 막대 그래프 정렬하기 : young - middle - old 순으로 정렬해서 출력
# 노년층 비율을 기준으로 정렬, young - middle - old 순으로 정렬
reorder_df = pivot_df.sort_values('old')[['young','middle','old']]
print(reorder_df)

# 누적 가로 막대 그래프로 출력
# 막대 그래프가 노년층의 비율이 높은 순으로 정렬되고, 막대 색깔도 연령대 순으로 나열되어 지역끼리 쉽게 비교할 수 있다.
reorder_df.plot.barh(stacked = True)
plt.title('지역별 연령대 비율(정렬 후)')
plt.show()

# 출력된 그래프의 결과를 보면 '대구/경북'의 노년층 비율이 가장 높고, 그 뒤로는 '강원/충북', '광주/전남/전북/제주도', '부산/경남/울산' 순으로 높다.
