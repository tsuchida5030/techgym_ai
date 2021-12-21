#AI-TECHGYM-1-12-Q-1
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

#PCA
from sklearn.decomposition import PCA

#フォントの準備
import urllib.request as req
url = "https://github.com/hokuto-HIRANO/Word2Vec/raw/master/font/Osaka.ttc"
req.urlretrieve(url, "./Osaka.ttc")

#フォントの指定
FONTPATH='./Osaka.ttc'
prop = font_manager.FontProperties(fname=FONTPATH)

#モデルの読み込み
model_path = './words.model'
model = word2vec.Word2Vec.load(model_path)

#単語ベクトルの可視化
def draw_2d_2groups(vectors, target1, target2, topn=100):
  similars1 = [w[0] for w in vectors.wv.most_similar(target1, topn=topn)]
  similars1.insert(0, target1)
  similars2 = [w[0] for w in vectors.wv.most_similar(target2, topn=topn)]
  similars2.insert(0, target2)
  similars = similars1 + similars2
  colors = ['b']+['g']*(topn)+ ['cyan']+['orangered']*(topn)
  X = [vectors.wv[w] for w in similars]
  pca = PCA(n_components=2)
  Y = pca.fit_transform(X)
  # plt.figure(figsize=(20,20))
  plt.scatter(Y[:,0], Y[:,1], color=colors)
  for w, x, y, c in zip(similars[:], Y[:,0], Y[:,1], colors):
    plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=8, color=c)
  plt.show()

#対象の単語
words = []
words.append("老人")
words.append("海")
words.append("ヘミングウェイ")
words.append("魚")
words.append("彼")

vectors =[]
for word in words:
  vectors.append(model.wv[word])

#主成分分析
pca = PCA(n_components=2)
pca.fit(vectors)
vectors_2D = pca.transform(vectors)

# for vec in vectors_2D:
#   print(vec)

# グラフの縦軸・横軸の目盛間隔を揃える
plt.figure(figsize = (12, 12))
plt.gca().set_xlim(-4, 6)
plt.gca().set_ylim(-5, 5)

# y=0に水平線を引く
plt.axhline(0, ls = "-.", color = "m")
# x=0に垂直線を引く
plt.axvline(0, ls = "--", color = "purple")

# colors = ['b']+['orangered']+['g']+['r']+['cyan']
# plt.scatter(vectors_2D[:,0], vectors_2D[:,1], color=colors)
# for w, x, y in zip(words, vectors_2D[:,0], vectors_2D[:,1]):
#   plt.annotate(w, xy=(x, y), xytext=(10,10), textcoords='offset points', fontproperties=prop, fontsize=15)
# plt.axis('equal')
# plt.show()

draw_2d_2groups(model,'老人','海',topn=100)