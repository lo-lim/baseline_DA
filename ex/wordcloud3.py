# 육아휴직 관련 법안에 대한 분석

import nltk
from konlpy.corpus import kobill

# KoNLPy가 내장하고 있는 법률문서 중 육아휴직 법안 제 18098990호를 읽어온다.
files_ko = kobill.fileids()
doc_ko = kobill.open('1809890.txt').read()
# doc_ko = open('hong.txt').read()              # hong.txt 파일 읽어오기
print(doc_ko)

# Twitter 분석기로 명사 추출 : KoNLPy버전에 따른 경고 메세지 출력
# UserWarning: "Twitter" has changed to "Okt" since KoNLPy v0.4.5.
#   warn('"Twitter" has changed to "Okt" since KoNLPy v0.4.5.')
# from konlpy.tag import Twitter; t = Twitter()
from konlpy.tag import Okt; t = Okt()
tokens_ko = t.nouns(doc_ko)
print(tokens_ko)

# 명사로 파싱된 변수를 읽어온다.
ko = nltk.Text(tokens_ko, name='대한민국 국회 의안 제 1809890호')
print(len(ko.tokens))          # 수집된 단어의 총갯수
print(len(set(ko.tokens)))     # 중복을 제외한 단어 갯수

import matplotlib.pyplot as plt
import matplotlib

# '맑은 고딕'으로 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 각 단어들의 빈도수를 그래프로 출력
plt.figure(figsize=(12,6))
ko.plot(50)                     # 빈도수가 높은 단어 50개를 그래프에 출력
plt.show()

# 위 그래프의 출력 결과를 보고, 불필요한 stopwords 등록해서 제거한다,
# 영어와 달리 한글을 stopword를 지정하는 것은 쉽지않다.
# case-by-case 로 stopword를 등록하자
stop_words = ['.', '(', ')', ',', "'", '%', '-', 'X', ').', '×','의','자','에','안','번',
                      '호','을','이','다','만','로','가','를','액','세','제','위','월','수','중','것','표','명']

ko = [each_word for each_word in ko if each_word not in stop_words]

# stopword를 등록한 다음에 다시 그래프를 그려보자
ko = nltk.Text(ko, name='대한민국 국회 의안 제 1809890호')
plt.figure(figsize=(12,6))
ko.plot(50)                             # 빈도수가 높은 단어 50개를 그래프에 출력
plt.show()

# wordcloud 그리기
data = ko.vocab().most_common(150)      # wordcloud로 출력할 단어의 갯수 150개

from wordcloud import WordCloud

wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',
                      relative_scaling=0.2,
                      background_color='white',).generate_from_frequencies(dict(data))
print(wordcloud.words_)
plt.figure(figsize=(12,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
