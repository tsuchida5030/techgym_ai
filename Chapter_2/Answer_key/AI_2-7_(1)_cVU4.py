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

#LabelEncoderのインスタンスを生成
le = LabelEncoder()

#ラベルを覚えさせる,ラベルを整数に変換
le_a = le.fit_transform(auto['make'])
auto['label_make'] = le_a

#count encoding
count = auto.groupby('make').label_make.count()                                  #make列内の項目毎に、出現回数をカウントした配列を作る
auto['count_make'] = auto['make'].map(count)                                     #make列内の項目毎に出現回数をカウントした配列の要素を、make列の値に従ってcount_make列にマッピングする

display(auto[['make','label_make','count_make']])
