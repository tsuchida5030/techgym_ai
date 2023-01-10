#AI-TECHGYM-2-6-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd

#読み込みデータ
pg_data = {'0':['Python'],'1':['Ruby'],'2':['PHP'],'3':['Java'],'4':['JavaScript']} #項目名の辞書型
df_row = pd.DataFrame(pg_data)                                                      #項目名が一行目に横に並ぶデータフレーム
df = df_row.T                                                                       #項目名が一列目に縦に並ぶデータフレーム
#display(df)

#one hot encoding
df_c = pd.get_dummies(df)                                                           #カテゴリ変数となる項目名が一列目に縦に並ぶデータフレームに対して、ワンホットエンコーディングを実行し、カテゴリ変数の行列を作る
#出力されるデータフレームの列名は、<元の列名"0">_<カテゴリ変数名>となる
#get_dummiesのオプション・・・prefix, prefix_sep, columns

#表示用並び替え
df_d = df_c.iloc[:,[3,4,2,0,1]]                                                     #ワンホットエンコーディングしたデータフレームの列順を、1が対角項に来るよう並び変える
display(df_d)                                                                       #1が対角項に並んだ、カテゴリ変数の行列

#columnを設定して、値を取得
new_df = pd.DataFrame(columns=["row", "vector"])
values = df[0].values

#one hot encoding
for i, row in enumerate(values):
    vector    = [0] * len(values)
    vector[i] = 1
    tmp_se    = pd.Series([row, vector], index=new_df.columns)
    new_df    = new_df.append(tmp_se, ignore_index=True)

#表示
display(new_df)
