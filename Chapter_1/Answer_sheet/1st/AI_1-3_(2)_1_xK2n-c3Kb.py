#AI-TECHGYM-1-3-Q-1
#教師なし学習 k-mean法

#1-3
#□データセットを生成して、散布図を書こう(描画するドットは黒色にする)

import numpy as np
import pandas as pd

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#分類データセット生成
from sklearn.datasets import make_blobs

plt.figure(figsize = (14,6))
x = np.linspace(1, 10, 10)

random_state_numbers = [1, 20]
for i, random_n in enumerate(random_state_numbers):
  X, y = make_blobs(random_state=random_n)
  cluster_df = pd.DataFrame(X, columns=['X','Y'])

  SSE_set = []
  for number in range(10):
    kmeans = KMeans(init='random',n_clusters=number+1)
    kmeans.fit(cluster_df)
    SSE_set.append(kmeans.inertia_)

  plt.xlabel('Number of clusters')
  plt.ylabel('Distortion')
  plt.subplot(1,2,i+1)
  plt.plot(x,SSE_set)