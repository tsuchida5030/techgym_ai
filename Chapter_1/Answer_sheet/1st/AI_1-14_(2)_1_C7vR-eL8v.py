﻿#AI-TECHGYM-1-14-Q-1
#自然言語処理

#インポート
import numpy as np
import pandas as pd
import os

#ファイルの場所
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#主成分分析
from sklearn.decomposition import PCA

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#グラフ
from matplotlib import pylab as plt
import matplotlib.font_manager as font_manager

# word2vec データ読み込み
from gensim.models import KeyedVectors

# データの読み込み
df = pd.read_csv("words.csv")

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

for i in df['words'].values:
  try:
    vectors.append(w2v[i])
  except Exception as e::
    vectors.append(zero_vec)
    print(f'The word "{i}" doesn\'t have a vector')

print(f'The length of vectors is {len(vectors)}')



#PCA
pca = PCA(n_components=2)
V = pca.fit_transform(vectors)

#ベクトルを平面にプロット
plt.scatter(V[:, 0], V[:,1])

#文字のプロット
for w, x, y in zip(df["words"].values, V[:,0], V[:,1]):
    plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=12)

#グラフ表示
plt.show()