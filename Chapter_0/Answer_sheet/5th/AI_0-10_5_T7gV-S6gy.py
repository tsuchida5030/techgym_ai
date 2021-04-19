#AI-TECHGYM-N-10

import pandas as pd
import numpy as np

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

#欠損データの扱い
hand_df1.iloc[1,0] =  np.nan
hand_df1.iloc[6,6] = np.nan
hand_df1.iloc[2:4,2] = np.nan
hand_df1.iloc[5:,3] = np.nan

display(hand_df1)

#欠損値の数
display(hand_df1.isnull().sum())

#リストワイズ
display(hand_df1.dropna())

#０で埋める
display(hand_df1.fillna(0))

#前の値で埋める
display(hand_df1.fillna(method = 'ffill'))

#平均値で埋める
display(hand_df1.fillna(hand_df1.mean()))

