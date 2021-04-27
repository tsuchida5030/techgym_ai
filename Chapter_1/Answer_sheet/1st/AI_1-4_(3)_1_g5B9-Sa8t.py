#AI-TECHGYM-1-4-Q-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd

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

shoppers_with_cluster = pd.concat([shoppers, labels], axis=1)

bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
cut_SPDay = pd.cut(shoppers_with_cluster.SpecialDay, bins)
df = pd.concat([shoppers_with_cluster.cluster_number, cut_SPDay], axis=1)

cross_cluster_SPDay = df.groupby(['cluster_number', 'SpecialDay']).size().unstack()
display(cross_cluster_SPDay)

bins = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cut_SPDay = pd.cut(shoppers_with_cluster.Region, bins)
df = pd.concat([shoppers_with_cluster.cluster_number, cut_SPDay], axis=1)

cross_cluster_SPDay = df.groupby(['cluster_number', 'Region']).size().unstack()
display(cross_cluster_SPDay)