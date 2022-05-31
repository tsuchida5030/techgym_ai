#AI-TECHGYM-1-14-A-1
#自然言語処理

import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
import numpy as np
import pandas as pd

#主成分分析
from sklearn.decomposition import PCA

# k-means
from sklearn.cluster import KMeans

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


title = "stanby-jobs-200d-word2vector.bin"
if not os.path.exists(title):
    print(title + " DOWNLOAD.")
    url = "https://github.com/bizreach/ai/releases/download/2018-03-13/stanby-jobs-200d-word2vector.bin"
    req.urlretrieve(url,"{0}".format(title))
else :
    print(title + " EXIST.")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# データの読み込み
df = pd.read_csv("words.csv") 

#ベクトルの取得
vectors = []
zero_vec = np.zeros(200)

for w in df["words"].values:
    try:
        vectors.append(w2v[w])
    except Exception as e:
        vectors.append(zero_vec)

#PCA
pca = PCA(n_components=2)
V = pca.fit_transform(vectors)

#kmeans
kmeans = KMeans(n_clusters=10, init='random')
kmeans.fit(V)
df_view['cluster'] = kmeans.labels_
df_view['words'] = df['words']
df_view['x'] = pd.DataFrame(V[:,0])
df_view['y'] = pd.DataFrame(V[:,1])

#色指定
color = df_V.cluster.astype(float)
df_view['color'] = pd.DataFrame(color)

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


#ベクトルを平面にプロット
for cluster in set(df_view['cluster']):
    V_roop = df_view[df_view['cluster']==cluster]
    X = V_roop.loc[:,'x']
    Y = V_roop.loc[:,'y']
    W = V_roop.loc[:,'words']
    C = V_roop.loc[:,'color']
    plt.scatter(X, Y, c=C)
    #文字のプロット
    for w, x, y in zip(W, X, Y):
        plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=12)

#グラフ表示
plt.show()
