#AI-TECHGYM-2-7-A-1
#特徴量エンジニアリング

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_2\Answer_sheet\AI_Chapter2_saved_files")

#インポート
import pandas as pd
import requests,io
from sklearn.preprocessing import LabelEncoder

#自動車価格データの取得
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
res = requests.get(url).content
auto = pd.read_csv(io.StringIO(res.decode('utf-8')), header=None)
auto.columns =['symboling','normalized-losses','make','fuel-type' ,'aspiration','num-of-doors',
                            'body-style','drive-wheels','engine-location','wheel-base','length','width','height',
                            'curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore',
                            'stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']
#データ表示
#display(auto)

#one hot encoding
df_c = pd.get_dummies(auto[['body-style','engine-type']],)                                                           #カテゴリ変数となる項目名が一列目に縦に並ぶデータフレームに対して、ワンホットエンコーディングを実行し、カテゴリ変数に対して0／1が入った行列を作る
#出力されるデータフレームの列名はオプションを指定しなければデフォルトで、<元のデータフレームの列名>_<カテゴリ変数名>となる
#get_dummiesのオプション・・・prefix, prefix_sep, columns(https://note.nkmk.me/python-pandas-get-dummies/)

display(df_c)
