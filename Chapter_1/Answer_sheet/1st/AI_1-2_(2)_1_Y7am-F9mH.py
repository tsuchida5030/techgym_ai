#AI-TECHGYM-1-2-Q
#教師なし学習 k-mean法

#1-2
#□データセットを生成して、散布図を書こう(描画するドットは黒色にする)
#□KMeansクラスを初期化しよう、初期化の方法はランダムで、クラスタ数は2とする
#□分類したクラスタ番号を表示してみる

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

plt.figure(figsize=(8, 10))
plt.subplot(2,1,1)

data, Y = make_blobs(random_state=5)
plt.scatter(data[:,0], data[:,1], color='black')

cluster_df = pd.DataFrame(data, columns=['X','Y'])

display(cluster_df.head())

kmeans = KMeans(init='random',n_clusters=2)
kmeans.fit(cluster_df)

y_pred = kmeans.predict(cluster_df)
cluster_df['cluster'] = y_pred

df0 = cluster_df[cluster_df.cluster == 0]
df1 = cluster_df[cluster_df.cluster == 1]

plt.subplot(2,1,2)

#グラフのプロット
plt.scatter(df0['X'],df0['Y'],color='blue',label='cluster0')
plt.scatter(df1['X'],df1['Y'],color='red',label='cluster1')

#凡例
plt.legend(loc='upper right')