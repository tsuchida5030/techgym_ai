#AI-TECHGYM-1-4-A-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd

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

# 先頭の5行を表示
display(shoppers.head(5))

#データ形式、欠損データ
print('データ形式(X,y):{}'.format(shoppers.shape))
print('欠損データの数:{}'.format(shoppers.isnull().sum().sum()))

view_columns = ['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration', 'Region', 'SpecialDay']

kmeans = KMeans(n_clusters=6, init='random', random_state=0)
kmeans.fit(shoppers[view_columns])
y_pred = kmeans.predict(shoppers[view_columns])

print(y_pred.value_counts(sort=False))
print(type(y_pred))
print(len(y_pred))