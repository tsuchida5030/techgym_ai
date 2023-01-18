#AI-TECHGYM-2-6-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd

#読み込みデータ
pg_data = {'0':['Python'],'1':['Ruby'],'2':['PHP'],'3':['Java'],'4':['JavaScript']} #pg_data:項目名の辞書型
df_row = pd.DataFrame(pg_data)                                                      #df_row:項目名が一行目に横に並ぶデータフレーム
df = df_row.T                                                                       #df:項目名が一列目に縦に並ぶデータフレーム
#display(df)

#one hot encoding
df_c = pd.get_dummies(df)                                                           #カテゴリ変数となる項目名が一列目に縦に並ぶデータフレームに対して、ワンホットエンコーディングを実行し、カテゴリ変数に対して0／1が入った行列を作る
#出力されるデータフレームの列名はオプションを指定しなければデフォルトで、<元のデータフレームの列名>_<カテゴリ変数名>となる
#get_dummiesのオプション・・・prefix, prefix_sep, columns(https://note.nkmk.me/python-pandas-get-dummies/)

#表示用並び替え
df_d = df_c.iloc[:,[3,4,2,0,1]]                                                     #ワンホットエンコーディングしたデータフレームの列順を、1が対角項に来るよう並び変える
display(df_d)                                                                       #1が対角項に並んだ、カテゴリ変数の行列を表示する

#columnを設定して、値を取得
new_df = pd.DataFrame(columns=["row", "vector"])                                    #列名だけの空のデータフレーム。rowはカテゴリ変数、vectorはカテゴリ変数の行列の縦ベクトル
values = df[0].values                                                               #df(項目名が一列目に縦に並ぶデータフレーム)の1列目をシリーズ型にしたもの

#one hot encoding
for i, row in enumerate(values):                                                    #項目名ひとつ毎につき１ループ。iはループ回数、rowは項目名
    vector    = [0] * len(values)                                                   #vector:ワンホットベクトルのベースとなる0ベクトル
    vector[i] = 1                                                                   #vector:ワンホットベクトルの1の場所を、他のループでつくるワンホットベクトルの1の場所と被らないよう、ループ回数iで指定する
    tmp_se    = pd.Series([row, vector], index=new_df.columns)                      #tmp_se:上述のrowとvectorを値としてシリーズ型にしたもの
    new_df    = new_df.append(tmp_se, ignore_index=True)                            #空のデータフレームnew_dfに、tmp_seのシリーズを横に連結（２列分追加）する

#表示
display(new_df)
