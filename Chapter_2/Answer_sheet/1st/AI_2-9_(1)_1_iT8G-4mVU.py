#AI-TECHGYM-2-9-Q
#特徴量エンジニアリング

# 実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_2\Answer_sheet\AI_Chapter2_saved_files")

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

#ファイルがなければ前の問題を実施する
title = "FIFA_data_pre.csv"
if not os.path.exists(title):
    print("Run Previous problem.")
else :
    print(title + " EXIST.")
    df=pd.read_csv('./FIFA_data_pre.csv')

st_time = time.time()

#スタイルの指定
plt.style.use('fivethirtyeight')
sns.set(style = "dark", palette = "colorblind", color_codes = True)
plt.figure(figsize = (15,5))
plt.tick_params(labelsize = 16)

#必要に応じて表示
#display(df.head())
#display(df.columns)

sns.countplot()

en_time = time.time()
wst_time = en_time - st_time
print(wst_time)