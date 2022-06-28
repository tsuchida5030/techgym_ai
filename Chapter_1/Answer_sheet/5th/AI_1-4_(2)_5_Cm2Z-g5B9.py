#AI-TECHGYM-1-4-A-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd

# 実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

# データがあるurl の指定
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv'

# データを取得して展開する
#対象データを読み込み
shoppers= pd.read_csv(file_url)

# 先頭の5行を表示
display(shoppers.head(5))

#データ形式、欠損データ
print('データ形式(X,y):{}'.format(shoppers.shape))
print('欠損データの数:{}'.format(shoppers.isnull().sum().sum()))

view_list = ['Administrative_Duration','Informational_Duration','ProductRelated_Duration','Region','SpecialDay',]
df_view = shoppers[view_list]
# display(shoppers[view_list])

kmeans = KMeans(n_clusters=6)
kmeans.fit(df_view)
df_view.loc[:,'cluster'] = kmeans.labels_

# display(df_view.head(5))

print(df_view.groupby('cluster').count())