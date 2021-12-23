#AI-TECHGYM-1-13-Q-1
#自然言語処理

# word2vec データ読み込み
from gensim.models import KeyedVectors

#ファイルの準備
import os
import urllib.request
import itertools

title = "stanby-jobs-200d-word2vector.bin"
if not os.path.exists(title):
  print(title + " DOWNLOAD.")
  url = "https://github.com/bizreach/ai/releases/download/2018-03-13/stanby-jobs-200d-word2vector.bin"
  urllib.request.urlretrieve(url,"{0}".format(title))
else :
  print(title + " EXIST.")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

#計算した結果近い単語が出てくる
print("「テクノロジー」")
words = w2v.most_similar('テクノロジー', topn=5)
for word in words:print(word)
print('\n')

lis_similarity = []
for pair in itertools.combinations(w2v.index2entity, 2):
  lis_similarity.append(w2v.n_similarity(pair[0], pair[1]))

df_sim = pd.concat([pd.Series(w2v.index2entity[0]), pd.Series(w2v.index2entity[1]), pd.Series(lis_similarity)])
display(df_sim.head())

# tsucchy言語
# matz ・・・ ruby言語