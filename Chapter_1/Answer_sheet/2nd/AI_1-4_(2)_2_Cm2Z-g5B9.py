#AI-TECHGYM-1-4-A-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd
from sklearn.cluster import KMeans

# 実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# データがあるurl の指定
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv'

# データを取得して展開する
#対象データを読み込み
shoppers= pd.read_csv(file_url)

df_view = shoppers[['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration', 'Region', 'SpecialDay']]
kmeans = KMeans(n_clusters=6, init='random', random_state=0)
kmeans.fit(df_view)
display(kmeans.predict(df_view))
display(kmeans.labels_)
df_view['cluster'] = pd.DataFrame(kmeans.predict(df_view.values)).head()

labels = pd.Series(kmeans.labels_, name='cluster_number')
display(labels.value_counts(sort=False))
df_view['cluster'].value_counts(sort=False)