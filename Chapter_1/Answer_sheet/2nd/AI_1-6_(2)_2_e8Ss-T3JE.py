#AI-TECHGYM-1-6-Q-1
#教師なし学習 PCA

#データ加工・処理・分析ライブラリ
import pandas as pd

#可視化ライブラリ
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline

#インポート
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#乳がんデータを読み込むためのインポート
from sklearn.datasets import load_iris

#乳がんデータの取得
iris = load_iris()

#三次元のグラフ
fig = plt.figure()
ax_3d = Axes3D(fig)
ax_3d.set_xlabel(iris.feature_names[0])
ax_3d.set_ylabel(iris.feature_names[1])
ax_3d.set_zlabel(iris.feature_names[2])
ax_3d.view_init(elev=10., azim=-15)
ax_3d.plot(iris.data[:,0],iris.data[:,1],iris.data[:,2],marker="o",linestyle='None',color='black')
plt.show()

#標準化
sc = StandardScaler()
sc.fit(iris.data)
X_std = sc.transform(iris.data)

#主成分分析
pca = PCA(n_components=2)
pca.fit(X_std)
X_pca = pca.transform(X_std)

#主成分分析の前と後で次元を確認する
print(len(X_std[0]))
print(len(X_pca[0]))

#列にラベルをつける、1つ目が第1主成分、2つ目が第2主成分
X_pca = pd.DataFrame(X_pca, columns=['pc1','pc2'])

#上のデータに、目的変数（cancer.target）を紐づける、横に結合
X_pca = pd.concat([X_pca, pd.DataFrame(iris.target, columns=['target'])], axis=1)

#悪性、良性を分ける
pca_1 = X_pca[X_pca['target']==0]
pca_2 = X_pca[X_pca['target']==1]
pca_3 = X_pca[X_pca['target']==2]

#悪性、良性をプロット
ax = pca_1.plot.scatter(x='pc1', y='pc2', color='blue', label='target-0')
pca_2.plot.scatter(x='pc1', y='pc2', color='red', label='target-1', ax=ax)
pca_3.plot.scatter(x='pc1', y='pc2', color='green', label='target-2', ax=ax)