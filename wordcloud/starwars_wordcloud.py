# 스타워즈의  A New Hope

import numpy as np
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

# a_new_hope.txt 파일과 stormtrooper_mask.png 이미지를 읽어와서 변수에 저장함.
text = open('a_new_hope.txt').read()
mask = np.array(Image.open('stormtrooper_mask.png'))

# text = text.replace('HAN', 'Han')
# text = text.replace("LUKE'S", 'Luke')

# star wars에서 많이 등장하는 int, ext 라는 단어는 카운트에서 제거함.
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

# wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10, random_state=1)
wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords)
wc.generate(text)
print(wc.words_)            # 최빈 단어를 찾는다 . Luck가 가장 많이 등장
# default_color = wc.to_array()

# def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
#                     return 'hsl(0, 0%%, %d%%)' % random.randint(60, 100)


plt.figure(figsize=(12,12))
# plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation='bilinear')
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()



