#AI-TECHGYM-1-4-A-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd

# 実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

# データがあるurl の指定
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv'

# データを取得して展開する
#対象データを読み込み
shoppers= pd.read_csv(file_url)

#データ形式、欠損データ
print('データ形式(X,y):{}'.format(shoppers.shape))
print('欠損データの数:{}'.format(shoppers.isnull().sum().sum()))

view_columns = ['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration', 'Region', 'SpecialDay']
df_view = shoppers.loc[:, view_columns]
kmeans = KMeans(init='random', n_clusters=6)
kmeans.fit(df_view)
df_view['cluster'] = pd.Series(kmeans.labels_)

# 各クラスタの数を表示
clusters = df_view['cluster'].value_counts().sort_index()
display(clusters)

# 各クラスタの数をグラフにプロット
plt.bar(clusters.index, clusters)
plt.show()