﻿#AI-TECHGYM-1-2-Q
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

data_set = make_blobs(random_state=5)

# グラフの縦軸・横軸の目盛間隔を揃える
plt.figure(figsize=(10,12))
plt.xlim(-10,10)
plt.ylim(-12,12)

# y=0に水平線を引く
plt.axhline(0, ls = "-.", color = "m")
# x=0に垂直線を引く
plt.axvline(0, ls = "--", color = "b")

X = data_set[0][:,0]
Y = data_set[0][:,1]

plt.scatter(X,Y,color='black')
plt.show()