#AI-TECHGYM-2-7-A-3
#特徴量エンジニアリング

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_2\Answer_sheet\AI_Chapter2_saved_files")

#インポート
import pandas as pd
import requests,io
import category_encoders as ce
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

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

#===重回帰分析===
#重回帰分析の説明変数をリストで指定(複数も指定可能)
list_cols = ['width','engine-size', 'make', 'body-style', 'engine-type', 'fuel-system']
auto_c = auto[list_cols]

#?やNaNの行を削除し、重回帰分析したい列を指定
auto_c = auto_c.dropna()
ce_ohe = ce.OneHotEncoder(cols=list_cols)

X_train, X_test, y_train, y_test = train_test_split(
    auto[list_cols], auto['price'], stratify = auto['price'], random_state=0)

model = LogisticRegression(random_state=0,solver='liblinear')
model.fit(X_train,y_train)

print("標準化前")
print('正解率(train):{:.3f}'.format(model.score(X_train, y_train)))
print('正解率(test):{:.3f}'.format(model.score(X_test, y_test)))