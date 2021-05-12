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
from sklearn.datasets import load_breast_cancer

#乳がんデータの取得
cancer = load_breast_cancer()

# display(cancer)

X = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

# Figureを追加
fig = plt.figure(figsize = (8, 8))

# 3DAxesを追加
ax = fig.add_subplot(111, projection='3d')

# 軸ラベルを設定
ax.set_xlabel("mean radius", size = 14, color = "r")
ax.set_ylabel("mean texture", size = 14, color = "r")
ax.set_zlabel("mean perimeter", size = 14, color = "r")

ax.scatter(X["mean radius"], X["mean texture"], X["mean perimeter"], s=20, c='black')

sc = StandardScaler()
X_std = sc.fit_transform(X)

pca = PCA(n_components=3)
pca.fit(X_std.iloc[:, 0:3])

print(pca.shape_)