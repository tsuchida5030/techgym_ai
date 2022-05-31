#AI-TECHGYM-1-14-Q-1
#自然言語処理

#実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
import numpy as np
import pandas as pd

#主成分分析
from sklearn.decomposition import PCA

#グラフ
from matplotlib import pylab as plt
import matplotlib.font_manager as font_manager

# word2vec データ読み込み
from gensim.models import KeyedVectors

#フォントの準備
import urllib.request as req
url = "https://github.com/hokuto-HIRANO/Word2Vec/raw/master/font/Osaka.ttc"
req.urlretrieve(url, "./Osaka.ttc")

#フォント指定
FONTPATH='./Osaka.ttc'
prop = font_manager.FontProperties(fname=FONTPATH)

#グラフサイズ
plt.figure(figsize=(20,20))

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# データの読み込み
df = pd.read_csv("words.csv") 

#ベクトルの取得
vectors = []
zero_vec = np.zeros(200)

for word in df['words']:
  try:
    vectors.append(w2v[word])
  except:
    vectors.append(zero_vec)

#単語のベクトル表現を2次元に圧縮する
pca = PCA(n_components=2)
pca.fit(vectors)
vectors_pca= pca.transform(vectors)

df_pca = pd.DataFrame(vectors_pca, columns=['x','y'])
df_view = pd.concat([df_pca, df], axis=1)

display(df_view.head())

# グラフの縦軸・横軸の目盛間隔を揃える
plt.figure(figsize = (18, 18))
plt.gca().set_xlim(-3, 3)
plt.gca().set_ylim(-3, 3)

# plt.grid(color='k', linestyle='--', linewidth=0.5)

# y=0に水平線を引く
# plt.axhline(0, ls = "-.", color = "magenta")
plt.axhline(0, ls = "-.", color = "m")

# x=0に垂直線を引く
# plt.axvline(0, ls = "--", color = "navy")
plt.axvline(0, ls = "--", color = "b")

for w in df_view['words']:
  df_show = df_view[df_view['words']==w]
  x = df_show.iloc[:,0]
  y = df_show.iloc[:,1]
  plt.scatter(x, y, color='b')
  plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=15)
plt.show()