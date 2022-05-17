#AI-TECHGYM-1-12-A-2
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd

#PCA
from sklearn.decomposition import PCA

# k-means
from sklearn.cluster import KMeans

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

#対象の単語
words = []
words.append("老人")
words.append("海")
words.append("ヘミングウェイ")
words.append("魚")
words.append("彼")

#単語ベクトルの可視化
def draw_2d_2groups(vectors, target1, target2, topn=100):
  similars1 = [w[0] for w in vectors.wv.most_similar(target1, topn=topn)]
  similars1.insert(0, target1)
  similars2 = [w[0] for w in vectors.wv.most_similar(target2, topn=topn)]
  similars2.insert(0, target2)
  similars = similars1 + similars2
  X = [vectors.wv[w] for w in similars]
  pca = PCA(n_components=2)
  Y = pca.fit_transform(X)

  df_view = pd.DataFrame(Y, columns=['x','y'])
  kmeans = KMeans(n_clusters=3, init='random')
  kmeans.fit(df_view)
  df_view['cluster'] = kmeans.labels_
  df0 = df_view[df_view['cluster'] == 0]
  df1 = df_view[df_view['cluster'] == 1]
  df2 = df_view[df_view['cluster'] == 2]

  # plt.figure(figsize=(20,20))
  plt.scatter(df0.iloc[:,0], df0.iloc[:,1], color='g')
  plt.scatter(df1.iloc[:,0], df1.iloc[:,1], color='r')
  plt.scatter(df2.iloc[:,0], df2.iloc[:,1], color='b')
  for w, x, y in zip(similars[:], Y[:,0], Y[:,1]):
    plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=15)
  plt.show()

# グラフの縦軸・横軸の目盛間隔を揃える
plt.figure(figsize = (18, 18))
plt.gca().set_xlim(-6, 6)
plt.gca().set_ylim(-6, 6)

# plt.grid(color='k', linestyle='--', linewidth=0.5)

# y=0に水平線を引く
# plt.axhline(0, ls = "-.", color = "magenta")
plt.axhline(0, ls = "-.", color = "m")

# x=0に垂直線を引く
# plt.axvline(0, ls = "--", color = "navy")
plt.axvline(0, ls = "--", color = "b")

#グラフ表示
draw_2d_2groups(model, '老人', '海')