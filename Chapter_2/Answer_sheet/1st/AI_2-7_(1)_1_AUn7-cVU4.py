#AI-TECHGYM-2-7-Q
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

cols = auto.make

#LabelEncoderのインスタンスを生成
le = LabelEncoder()

#ラベルを覚えさせる,ラベルを整数に変換
le_a = le.fit_transform(cols)                                              #リスト内の項目毎に、ユニークな整数をエンコードした配列を作る
df_le = pd.DataFrame(le_a,columns=['label_make'])                    #配列をデータフレームに変換する
# df_le = pd.DataFrame(le_a,index=cols,columns=['count_make'])

df_auto = pd.concat([auto, df_le], axis=1)
display(df_auto)