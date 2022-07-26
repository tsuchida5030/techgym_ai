#AI-TECHGYM-1-6-Q-1
#教師なし学習 PCA

#実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

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

ls_data = []
ls_columns = []
for i in range(3):
  ls_data.append(cancer.data[:,i])
  ls_columns.append(cancer.feature_names[i])

ls_data_T = [list(x) for x in zip(*ls_data)]

df_cancer = pd.DataFrame(ls_data_T)
df_cancer.columns = ls_columns

display(df_cancer.head())

x = df_cancer.iloc[:,0]
y = df_cancer.iloc[:,1]
z = df_cancer.iloc[:,2]
# Axes3Dオブジェクトの生成
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.view_init(elev=15, azim=10)
# 各種描画処理
# ax.set_xlim3d(0, 3)
# ax.set_ylim3d(0, 3)
# ax.set_zlim3d(0, 3)
ax.scatter(x, y, z)

# プロットの表示
plt.show()

# 標準化
sc = StandardScaler()
X_std = sc.fit_transform(cancer.data)
print(X_std)

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
df_pca['target'] = cancer.target

display(df_pca.head())

df0 = df_pca[df_pca.target == 0]
df1 = df_pca[df_pca.target == 1]

plt.scatter(df0[0], df0[1], label='malignant', color='red')
plt.scatter(df1[0], df1[1], label='benign', color='blue')

plt.legend(loc='upper right')