#AI-TECHGYM-1-2-A-1
#教師なし学習 k-mean法

#1-2
#□データセットを生成して、散布図を書こう(描画するドットは黒色にする)
#□KMeansクラスを初期化しよう、初期化の方法はランダムで、クラスタ数は2とする
#□分類したクラスタ番号を表示してみる

#実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# データ加工・処理・分析ライブラリ
import numpy as np
import numpy.random as random
import pandas as pd

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#分類データセット生成
from sklearn.datasets import make_blobs

X, y = make_blobs(random_state=5)

kmeans = KMeans(n_clusters=2, init='random')
kmeans.fit(X)

cluster_df = pd.DataFrame(X,columns=['X','Y'])
cluster_df['cluster'] = kmeans.labels_

df0 = cluster_df[cluster_df['cluster']==0]
df1 = cluster_df[cluster_df['cluster']==1]

plt.scatter(df0['X'], df0['Y'], color='blue', label='cluster0')
plt.scatter(df1['X'], df1['Y'], color='red', label='cluster1')

plt.legend(loc='upper right')