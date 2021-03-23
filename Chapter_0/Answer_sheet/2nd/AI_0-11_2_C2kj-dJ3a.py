#AI-TECHGYM-N-11

import pandas as pd

import os
os.chdir('C:/Users/tsuchida/Documents/techgym_セミナー/TortoiseGit_resorce/techgym_ai/Chapter_0/Answer_sheet/AI_Chapter0_saved_files')

# データの準備
hand1 = {'id'  :['100','101','102','103','104','105','106','107','108','109'],
         'gender'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
         'age'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
         'address'  :['東京','大阪','名古屋','北海道','東京','鹿児島','大阪','名古屋','東京','大阪'],
         'hobby'  :['野球','ルーレット','じゃんけん','野球','ルーレット','野球','じゃんけん','ルーレット','野球','じゃんけん'],
         'job'  :['IT','医療','弁護士','事務','事務','弁護士','IT','IT','IT','事務'],
         'win'  :[20,21, 4,60,14,10,12,19,12,14],
         'lose'  :[24,15,35, 3,35,29, 2,12,11,43],
         'draw':[15,40,34,29,14, 4,22,17,12,10]}

hand_df1 = pd.DataFrame(hand1)

#CSVファイルへの書き込み
hand_df1.to_csv("hand_df1.csv")

#CSVファイルの読み込み
hand_df2 = pd.read_csv("hand_df1.csv")

#表示
display(hand_df2)

