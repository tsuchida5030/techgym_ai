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

#アヤメのデータの取得
iris = load_iris()

df_iris = pd.DataFrame(iris.data) 
df_iris.columns = iris.feature_names

# display(df_iris)

x = df_iris.iloc[:,0]
y = df_iris.iloc[:,1]
z = df_iris.iloc[:,2]
# Axes3Dオブジェクトの生成
fig = plt.figure(figsize = (12, 12))
ax = fig.add_subplot(111, projection="3d")

# 各種描画処理
xmax, xmin = 0,5
ymax, ymin = 0,6
zmax, zmin = 0,7

ax.set_xlim3d(xmin, xmax)
ax.set_ylim3d(ymin, ymax)
ax.set_zlim3d(zmin, zmax)

ax.set_xlabel(df_iris.columns[0])
ax.set_ylabel(df_iris.columns[1])
ax.set_zlabel(df_iris.columns[2])

ax.set_box_aspect((xmax-xmin,ymax-ymin,zmax-zmin))
ax.view_init(elev=15, azim=10)
# plt.axis('off')
ax.scatter(x, y, z)

# プロットの表示
plt.show()

# 標準化
sc = StandardScaler()
X_std = sc.fit_transform(iris.data)
# print(X_std)

# 主成分分析
pca = PCA(n_components=2)
pca.fit(X_std)
X_pca = pca.transform(X_std)

EVR = pca.explained_variance_ratio_
x = float(format(EVR[0], '.3f'))
y = float(format(EVR[1], '.3f'))

print('X_pca shape:{}'.format(X_pca.shape))
print('Explained variance ratio:{}'.format([x,y]))

print()

df_pca = pd.DataFrame(X_pca)
df_pca['target'] = iris.target

display(df_pca.head())

df0 = df_pca[df_pca.target == 0]
df1 = df_pca[df_pca.target == 1]
df2 = df_pca[df_pca.target == 2]

plt.figure(figsize=(8,8))
plt.xlim(-4,4)
plt.ylim(-4,4)
# y=0に水平線を引く
plt.axhline(0, ls = "-.", color = "m")
# x=0に垂直線を引く
plt.axvline(0, ls = "--", color = "purple")

plt.scatter(df0[0], df0[1], label='setosa', color='red')
plt.scatter(df1[0], df1[1], label='versicolor', color='blue')
plt.scatter(df2[0], df2[1], label='virginica', color='green')

plt.legend(loc='upper right')