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

kmeans=KMeans(n_clusters=2, init='random')

data_set = make_blobs(random_state=5)[0]
clusters = make_blobs(random_state=5)[1]

plt.scatter(data_set[:,0], data_set[:,1], color='black')

# kmeans.fit(data_set)
# kmeans.predict(data_set)