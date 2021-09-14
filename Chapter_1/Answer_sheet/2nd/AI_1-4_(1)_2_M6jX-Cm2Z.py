﻿#AI-TECHGYM-1-4-Q-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd

# 実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# データがあるurl の指定
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv'

# データを取得して展開する
# 対象データを読み込み
shoppers= pd.read_csv(file_url)

# 先頭5行
display(shoppers.head())

# データの形式：行と列の数
display(len(shoppers.index))
display(len(shoppers.columns))

# 欠損データの数
display(shoppers.isnull().values.sum())