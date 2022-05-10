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

#アヤメデータを読み込むためのインポート
from sklearn.datasets import load_iris

#アヤメデータの取得
iris = load_iris()

#三次元のグラフ
fig = plt.figure()
ax_3d = fig.add_subplot(111, projection='3d')
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

#属性表示
print('X_std shape:{}'.format(X_std.shape))
print('X_pca shape:{}'.format(X_pca.shape))

#列にラベルをつける、1つ目が第1主成分、2つ目が第2主成分
X_pca = pd.DataFrame(X_pca, columns=['pc1','pc2'])

#上のデータに、目的変数（cancer.target）を紐づける、横に結合
X_pca = pd.concat([X_pca, pd.DataFrame(iris.target, columns=['target'])], axis=1)

#品種を分ける
pca_Setosa = X_pca[X_pca['target']==0]
pca_Versicolour = X_pca[X_pca['target']==1]
pca_Virginica = X_pca[X_pca['target']==2]

#悪性、良性をプロット
ax = pca_Setosa.plot.scatter(x='pc1', y='pc2', color='blue', label='Setosa')
pca_Versicolour.plot.scatter(x='pc1', y='pc2', color='red', label='Versicolour', ax=ax)
pca_Virginica.plot.scatter(x='pc1', y='pc2', color='green', label='Virginica', ax=ax)