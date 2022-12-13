#AI-TECHGYM-2-5-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import scipy.stats as sp
from sklearn.preprocessing import MinMaxScaler

#行列
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

#正規化
sc = MinMaxScaler()
sc.fit(matrix)
matrix_mms = sc.transform(matrix)
df_matrix_mms = pd.DataFrame(matrix_mms)
display(df_matrix_mms)

#データフレーム
df = pd.DataFrame(matrix)

#正規化 : 各変数 - 最小値 / 最大値 - 最小値
df_mms = (df - df.min())/(df.max() - df.min())
display(df_mms)

#検算
display(df_mms.min())
display(df_mms.max())
