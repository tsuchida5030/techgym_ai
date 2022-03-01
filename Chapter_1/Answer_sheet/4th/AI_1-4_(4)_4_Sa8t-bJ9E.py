#AI-TECHGYM-1-4-A-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd
# k-means法を使うためのインポート
from sklearn.cluster import KMeans

# 実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# データがあるurl の指定
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv'

# データを取得して展開する
#対象データを読み込み
shoppers= pd.read_csv(file_url)

# 先頭の5行を表示
# display(shoppers.head(5))

#データ形式、欠損データ
# print('データ形式(X,y):{}'.format(shoppers.shape))
# print('欠損データの数:{}'.format(shoppers.isnull().sum().sum()))

view_list = ['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration', 'SpecialDay', 'Region']
df_view = shoppers.loc[:,view_list]

kmeans = KMeans(n_clusters=6, init='random')
kmeans.fit(df_view)

df_view['cluster'] = kmeans.labels_

# labels = df_view['cluster'].value_counts()
# display(labels)

bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
df_view['SPDay_bin'] = pd.cut(df_view['SpecialDay'], bins, right=False)
df_SPDay = df_view.loc[:,['cluster','SPDay_bin']]
display(df_SPDay.groupby(['cluster','SPDay_bin']).size().unstack())

bins_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
df_view['Region_bin'] = pd.cut(df_view['Region'], bins_2, right=False)
df_SPDay = df_view.loc[:,['cluster','Region_bin']]
display(df_SPDay.groupby(['cluster','Region_bin']).size().unstack())

print('Region 1 の地域の人が、サイトへのアクセス件数が多い')
print('クラスター 4 に分類される人は少数派で、ほとんどがRegion 1 の人であり、特別な日の前後の日にアクセスをしている')
print('クラスター 4 を除き、大体どの購買層も全ての地域に満遍なく分布しているが、クラスター 5 に分類される人のみで、Region 8 からのアクセスはない')