﻿#AI-TECHGYM-1-4-A-2
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd
from pandas import Series, DataFrame

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

# データがあるurl の指定
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv'

# データを取得して展開する
#対象データを読み込み
shoppers= pd.read_csv(file_url)

# データの列の絞り込み
shoppers_sub = shoppers[['Administrative_Duration','Informational_Duration','ProductRelated_Duration','Region','SpecialDay']]

# KMeansクラスの初期化
kmeans = KMeans(init='random', n_clusters=6, random_state=0)

# クラスターの重心を計算
kmeans.fit(shoppers_sub)

# クラスター番号をpandasのSeriesオブジェクトに変換
labels = pd.Series(kmeans.labels_, name='cluster_number')

# クラスター番号と件数を表示
# print(labels.value_counts(sort=False))

df_view = pd.concat([shoppers_sub, labels], axis=1)

df_views = []

print('SpecialDay の値で集計')
for i in range(6):
  df_views.append(df_view[df_view['cluster_number'] == i])
  print(f'クラスター番号{i}')
  display(df_views[i].loc[:, 'SpecialDay'].value_counts(sort=False))
  print()

print('Region の値で集計')
for i in range(6):
  print(f'クラスター番号{i}')
  display(df_views[i].loc[:, 'Region'].value_counts(sort=False))
  print()