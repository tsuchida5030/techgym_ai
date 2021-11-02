#AI-TECHGYM-1-3-Q-1
#教師なし学習 k-mean法

#1-3
#□データセットを生成して、散布図を書こう(描画するドットは黒色にする)

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#分類データセット生成
from sklearn.datasets import make_blobs

#実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

plt.figure(figsize = (12,6))

# X, y = make_blobs(random_state=1)
# plt.subplot(3,3,1)
# plt.scatter(X[:,0], X[:,1], color='black')

X, y = make_blobs(random_state=5)
# plt.subplot(3,3,2)
# plt.scatter(X[:,0], X[:,1], color='black')

# X, y = make_blobs(random_state=10)
# plt.subplot(3,3,3)
# plt.scatter(X[:,0], X[:,1], color='black')

# X, y = make_blobs(random_state=15)
# plt.subplot(3,3,4)
# plt.scatter(X[:,0], X[:,1], color='black')

# X, y = make_blobs(random_state=20)
# plt.subplot(3,3,5)
# plt.scatter(X[:,0], X[:,1], color='black')

elbow = []
for i in range(10):
  kmeans = KMeans(n_clusters=i+1).fit(X)
  elbow.append([i+1, kmeans.inertia_])
plt.subplot(1,2,1)
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.ylim(0,5000)
plt.plot([r[0] for r in elbow], [r[1] for r in elbow], '+-', label='random_state 5')
plt.legend()

X, y = make_blobs(random_state=25)
# plt.subplot(3,3,6)
# plt.scatter(X[:,0], X[:,1], color='black')

elbow = []
for i in range(10):
  kmeans = KMeans(n_clusters=i+1).fit(X)
  elbow.append([i+1, kmeans.inertia_])
plt.subplot(1,2,2)
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.ylim(0,5000)
plt.plot([r[0] for r in elbow], [r[1] for r in elbow], '+-', label='random_state 25')
plt.legend()