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
le_a = le.fit_transform(columns)                                              #リスト内の項目毎に、ユニークな整数をエンコードした配列を作る
df_le = pd.DataFrame(le_a,index=columns,columns=['Label'])                    #配列をデータフレームに変換する
display(df_le)
