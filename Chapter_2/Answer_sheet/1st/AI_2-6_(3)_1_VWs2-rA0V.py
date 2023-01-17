#AI-TECHGYM-2-6-A-2
#特徴量エンジニアリング

#インポート
import pandas as pd

#読み込みデータ
pg_data = {'0':['Python'],'1':['Ruby'],'2':['PHP'],'3':['Java'],'4':['JavaScript']} #項目名の辞書型
df_row = pd.DataFrame(pg_data)                                                      #項目名が一行目に横に並ぶデータフレーム
df = df_row.T                                                                       #項目名が一列目に縦に並ぶデータフレーム
#display(df)

#===LabelEncoder====
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()                                                               #インスタンス化されたワンホットエンコーダのクラス
array_enc = enc.fit_transform(df)                                                  #カテゴリ変数となる項目名が一列目に縦に並ぶデータフレームから、ワンホットの配列を作る

columns = ['Java','JavaScript','PHP','Python','Ruby']
df1 = pd.DataFrame(data = array_enc, columns = columns,dtype=int)                   #ワンホットの配列をデータフレームに変換する

#表示用の入れ替え
df1_d = df1.iloc[:,[3,4,2,0,1]]
display(df1_d)
