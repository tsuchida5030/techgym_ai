#AI-TECHGYM-1-2-Q
#教師なし学習 k-mean法

#1-2
#データセットを生成して、散布図を書こう(描画するドットは黒色にする)
#KMeansクラスを初期化しよう、初期化の方法はランダムで、クラスタ数は2とする
#分類したクラスタ番号を表示してみる

# データ加工・処理・分析ライブラリ
import numpy as np
import numpy.random as random
import pandas as pd

#実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#分類データセット生成
from sklearn.datasets import make_blobs

data = make_blobs(random_state=5)
# print(data)

cluster_df = pd.DataFrame(data[0])

kmeans = KMeans(n_clusters=2, init='random')
kmeans.fit(cluster_df)

cluster_df['2'] = kmeans.labels_
cluster_df.columns = ['X', 'Y', 'cluster']

df0 = cluster_df[cluster_df['cluster'] == 0]
df1 = cluster_df[cluster_df['cluster'] == 1]

# グラフの縦軸・横軸の目盛間隔を揃える
plt.figure(figsize = (8, 8))
plt.gca().set_xlim(-10, 4)
plt.gca().set_ylim(-2, 12)

# y=0に水平線を引く
plt.axhline(0, ls = "-.", color = "m")
# x=0に垂直線を引く
plt.axvline(0, ls = "--", color = "purple")
plt.scatter(df0['X'],df0['Y'], label='cluster_0', color='blue')
plt.scatter(df1['X'],df1['Y'], label='cluster_1', color='red')
plt.legend(loc='upper right')
plt.show()