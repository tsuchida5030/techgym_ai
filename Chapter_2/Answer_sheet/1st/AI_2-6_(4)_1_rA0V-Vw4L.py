#AI-TECHGYM-2-6-A-3
#特徴量エンジニアリング

#インポート
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#読み込みデータ
columns = ['Python','Ruby','PHP','Java','JavaScript']

#LabelEncoderのインスタンスを生成
le = LabelEncoder()

#ラベルを覚えさせる,ラベルを整数に変換
le_a = le.fit_transform(columns)
df_le = pd.DataFrame(le_a,index=columns,columns=['Label'])
display(df_le)


# hash関数とは？　「土田」という値に紐づける適当な数値(ハッシュ値)を当てる関数