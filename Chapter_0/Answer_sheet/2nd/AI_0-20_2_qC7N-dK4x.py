#AI-TECHGYM-N-20

import urllib
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

#線形重回帰
from sklearn.linear_model import LinearRegression

#データの分割
from sklearn.model_selection import train_test_split

import os
os.chdir('C:/Users/tsuchida/Documents/techgym_セミナー/TortoiseGit_resorce/techgym_ai/Chapter_0/Answer_sheet/AI_Chapter0_saved_files')

#データの取得
data = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine = pd.read_csv(data)

#indexを説明からつける
#アルコール,リンゴ酸,灰,灰分のアルカリ度,マグネシウム,総フェノール,フラバノイド
#非フラバノイドフェノール,プロアントシアニン,色の濃さ,色相,希釈ワインのOD 280 / OD 315,プロリン
columns_name = ['class','Alcohol','Malic_acid','Ash',
                'Alcalinity_of_ash','Magnesium','Total_phenols',
                'Flavanoids','Nonflavanoid_phenols','Proanthocyanins',
                'Color_intensity','Hue','OD280_OD315','Proline']
wine.columns = columns_name

#目的変数にAlcoholを設定、それ以外を説明変数にする
x = wine[columns_name].drop('Alcohol', axis = 1)
y = wine['Alcohol']

# 重回帰クラスの初期化と学習
model = LinearRegression()
model.fit(x,y)

#決定係数の計算
k_all = model.score(x, y)

# 決定係数を表示
print('決定係数(all):{:.3f}'.format(k_all))

# 回帰係数と切片を表示
print('回帰係数{}'.format(pd.Series(model.coef_, index=x.columns)))
print('切片: {:.3f}'.format(model.intercept_))

#単回帰分析の結果
k_single = 0.5478829286096659

#決定係数の差分
print('決定係数(差分):{:.3f}'.format(k_all - k_single))
