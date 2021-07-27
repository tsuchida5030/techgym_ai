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

data_set = make_blobs(random_state=5)[0]

kmeans=KMeans(n_clusters=2, init='random')
kmeans.fit(data_set)
clusters = kmeans.predict(data_set)

df = pd.DataFrame([data_set.T[0], data_set.T[1], clusters]).T

df.columns = ['X', 'Y', 'cluster']
df0 = df[df['cluster'] == 0]
df1 = df[df['cluster'] == 1]

plt.scatter(df0['X'], df0['Y'], color='blue', label='cluster0')
plt.scatter(df1['X'], df1['Y'], color='red', label='cluster1')

plt.legend(loc='upper right')