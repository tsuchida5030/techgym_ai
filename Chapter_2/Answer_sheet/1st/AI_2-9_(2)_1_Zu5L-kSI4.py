#AI-TECHGYM-2-9-A-1
#特徴量エンジニアリング

# 実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_2\Answer_sheet\AI_Chapter2_saved_files")

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
import os

#ファイルがなければ前の問題を実施する
title = "FIFA_data_pre.csv"
if not os.path.exists(title):
    print("Run Previous problem.")
else :
    print(title + " EXIST.")
    df=pd.read_csv('./FIFA_data_pre.csv')

#スタイルの指定
plt.style.use('fivethirtyeight')
sns.set(style = "dark", palette = "colorblind", color_codes = True)

#必要に応じて表示
#display(df.head())
#display(df.columns)

st_time = time.time()


#特別なスコア
df['Weight_num'] = df['Weight'].apply(lambda x: x.rstrip('lbs'))
plt.figure(figsize = (15, 5))
ax = sns.distplot(df['Weight_num'], bins = 58, kde = True, color = 'green')
ax.set_xlabel(xlabel = 'Weight range', fontsize = 16)
ax.set_ylabel(ylabel = 'Count of the Players',fontsize = 16)
ax.set_title(label = 'Distribution of Weight of Players', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

#ポテンシャル
df['Wage_num'] = df['Wage'].apply(lambda x: x.strip('€K'))
plt.figure(figsize = (15, 5))
ax = sns.distplot(df['Wage_num'], bins = 58, kde = True, color = 'blue')
ax.set_xlabel(xlabel = 'Wage range', fontsize = 16)
ax.set_ylabel(ylabel = 'Count of the Players',fontsize = 16)
ax.set_title(label = 'Distribution of Wage of Players', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

df.to_csv('FIFA_data_pre2.csv')

en_time = time.time()
wst_time = en_time - st_time
print(wst_time)