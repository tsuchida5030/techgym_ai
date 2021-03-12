#AI-TECHGYM-N-17

import pandas as pd
import urllib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model.base import LinearRegression
%matplotlib inline

import os
os.chdir('C:/Users/tsuchida/Documents/techgym_セミナー/TortoiseGit_resorce/techgym_ai/Chapter_0/Answer_sheet/AI_Chapter0_saved_files')

#相関係数のため読み込み
import scipy as sp

#線形単回帰
from sklearn import linear_model

#データの取得
data = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine = pd.read_csv(data)

txt= "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.names"
urllib.request.urlretrieve(txt, './wine.names')

#説明文の表示(必要に応じて表示)
#f = open("./wine.names","r")
#for line in f:
#    print(line)
#f.close()

#indexを説明からつける
#アルコール,リンゴ酸,灰,灰分のアルカリ度,マグネシウム,総フェノール,フラバノイド
#非フラバノイドフェノール,プロアントシアニン,色の濃さ,色相,希釈ワインのOD 280 / OD 315,プロリン
columns_name = ['class','Alcohol','Malic_acid','Ash',
                'Alcalinity_of_ash','Magnesium','Total_phenols',
                'Flavanoids','Nonflavanoid_phenols','Proanthocyanins',
                'Color_intensity','Hue','OD280_OD315','Proline']
wine.columns = columns_name


# 線形回帰インスタンス
REG = linear_model.LinearRegression()

p=1 #グラフ
attribute = ['Malic_acid', 'Ash', 'Total_phenols', 'Color_intensity']
for w in attribute:

  # 説明変数
  X = wine.loc[:, ['Alcohol']]

  # 目的変数
  Y = wine.loc[:, w]

  # 予測モデルを計算、ここでa,bを算出
  REG.fit(X, Y)

  # 回帰係数
  display('回帰係数:', REG.coef_)
  # 切片 
  display('切片:', REG.intercept_)

  # グラフの大きさを指定
  plt.figure(figsize=(10, 10))

  # 先ほどと同じ散布図,その上に線形回帰直線を引く
  plt.subplot(2,2,p)
  plt.scatter(X, Y)

  x = np.linspace(X.loc[:, 'Alcohol'].min(), X.loc[:, 'Alcohol'].max(), 100).reshape(-1, 1)
  y_pred = REG.predict(x)
  plt.scatter(x, y_pred, s=10)

  plt.grid(True)
  plt.xlabel('Alcohol')
  plt.ylabel(w)

  # 決定係数
  print('決定係数:', REG.score(X, Y))

  #相関係数
  display('相関係数:', sp.stats.pearsonr(X.loc[:, 'Alcohol'], Y))

  #次のグラフ
  p = p + 1

#分析結果
display("もっとも相関があるのは「アルコール度数」と「色の濃さ」である")
display("相関係数は",sp.stats.pearsonr(X.loc[:, 'Alcohol'], wine.loc[:, 'Color_intensity']))
