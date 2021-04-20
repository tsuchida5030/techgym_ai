﻿#AI-TECHGYM-1-1-A-2
#教師なし学習 k-mean法

#□Sampleをデータフレームに入れて、散布図を書こう(描画するドットは黒色にする)
#□KMeansクラスを初期化しよう、初期化の方法はランダムで、クラスタ数は3とする
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

Sample = np.array([[ -2.32496308,  -6.6999964 ],
       [  0.51856831,  -4.90086804],
       [  2.44301805,   3.84652646],
       [  5.82662285,  -9.92259335],
       [  2.03300209,   5.28990817],
       [  3.37979515,   4.18880872],
       [  6.04774884, -10.30504657],
       [ -0.42084194,  -4.24889336],
       [  3.78067293,   5.22062163],
       [  5.69248303,  -7.19999368],
       [  5.15909568, -10.13427003],
       [  1.16464321,   5.59667831],
       [  2.94601402,   3.3575069 ],
       [  1.1882891 ,  -5.56058781],
       [ -0.31748917,  -6.86337766],
       [  4.32968132,   5.64396726],
       [  4.28981065,  -9.44982413],
       [  3.49996332,   3.02156553],
       [  5.31414039,  -9.94714146],
       [  2.61105267,   4.22218469],
       [  4.88653379,  -8.87680099],
       [  1.95552599,  -4.05690149],
       [  2.09985134,   3.6556301 ],
       [  1.31468967,  -5.01055177],
       [  5.52556208,  -8.18696464],
       [  0.81677922,   4.75330395],
       [  2.52859794,   4.5759393 ],
       [  3.69548081,   5.14288792],
       [  2.37698085,   5.82428626],
       [  5.69192445,  -9.47641249],
       [  0.91726632,  -6.52637778],
       [  1.44712872,   4.75428451],
       [  2.96590542,   4.5052704 ],
       [  6.68288513, -10.31693051],
       [ -0.43558928,  -4.7222919 ],
       [  0.34789333,  -3.88965912],
       [  0.97700138,  -5.7984931 ],
       [  2.45717481,   5.96515011],
       [  2.60711685,   2.84436554],
       [  2.89022984,   2.98168388]])

cluster_df = pd.DataFrame(Sample)

#display(cluster_df)

# 散布図(colorのオプションで色付け)
plt.figure(figsize=(12,16))

plt.subplot(2, 1, 1)
plt.scatter(cluster_df[0],cluster_df[1],color='black')

#
# KMeansクラスの初期化
kmeans = KMeans(init='random',n_clusters=3)

# クラスターの重心を計算
kmeans.fit(cluster_df)

# クラスター番号を分類
y_pred = kmeans.predict(cluster_df)

#クラスター番号を表示(必要に応じて)

#データフレームに追加
cluster_df['2'] = y_pred

# 上記のデータにて、X軸の値をX、Y軸の値をY、クラスター番号をclusterと列名指定
cluster_df.columns = ['X','Y','cluster']

#必要であればデータを表示してクラスタ番号が追加されていることを確認する
#display(cluster_df['cluster'])

df0 = cluster_df[cluster_df['cluster']==0]
df1 = cluster_df[cluster_df['cluster']==1]
df2 = cluster_df[cluster_df['cluster']==2]

plt.subplot(2, 1, 2)
plt.scatter(df0['X'], df0['Y'], color='blue', label='cluster0')
plt.scatter(df1['X'], df1['Y'], color='red', label='cluster1')
plt.scatter(df2['X'], df2['Y'], color='green', label='cluster2')

plt.legend(loc='upper left')