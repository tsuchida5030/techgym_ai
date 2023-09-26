#AI-TECHGYM-2-11-Q
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_2\Answer_sheet\AI_Chapter2_saved_files")

#ファイルがなければ前の問題を実施する
title = "FIFA_data_pre2.csv"
if not os.path.exists(title):
    print("Run Previous problem.")
else :
    print(title + " EXIST.")
    df=pd.read_csv('./FIFA_data_pre2.csv')

#スタイル指定
plt.style.use('fivethirtyeight')
sns.set(style = "dark", palette = "colorblind", color_codes = True)

#不要な列を削除する
drop_cols = df.columns[28:54]
df = df.drop(drop_cols, axis = 1)
df = df.drop(['Unnamed: 0','Unnamed: 0.1','ID','Jersey Number','Joined','Loaned From',
              'Body Type', 'Release Clause','Contract Valid Until','LS','ST',
              'Value','Name','Club'], axis = 1)

x_columns = ['Defending', 'General', 'Mental', 'Passing', 'Mobility', 'Power', 'Shooting']

# 線形回帰インスタンス
REG = LinearRegression()
# 説明変数
X = df.loc[:, x_columns].values
# 目的変数
Y = df['Overall'].values
# 予測モデルを計算、ここでa,bを算出
REG.fit(X, Y) 

# 回帰係数
display('回帰係数:', REG.coef_)
# 切片 
display('切片:', REG.intercept_)

# 決定係数
display('決定係数:', REG.score(X, Y))

# RSME
pred = REG.predict(X)
display('RMSE:', np.sqrt(mean_squared_error(Y,pred)))