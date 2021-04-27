#AI-TECHGYM-1-4-Q-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd

import os
os.chdir('C:/Users/tsuchida/Documents/techgym_セミナー/TortoiseGit_resorce/techgym_ai/Chapter_1/AI_Chapter1_saved_files')

# データがあるurl の指定
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv'

# データを取得して展開する
#対象データを読み込み
shoppers= pd.read_csv(file_url)

display(shoppers.head())
display(f"データの形式(X,y)：({len(shoppers.index)}, {len(shoppers.columns)})")
display(shoppers.isnull())