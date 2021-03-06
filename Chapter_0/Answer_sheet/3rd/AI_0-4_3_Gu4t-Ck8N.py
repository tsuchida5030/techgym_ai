#AI-TECHGYM-N-4

import pandas as pd

#欠損値NaNを扱うためにnumpyをimportする
import numpy as np

hand = {'性別'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
        '年齢'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
        '勝ち'  :[20,21, 4,60,14,10,12,19,12,14],
        '負け'  :[24,15,35, 3,35,29, 2,12,11,43],
        'あいこ':[15,40,34,29,14, 4,22,17,12,10]}
hand_df = pd.DataFrame(hand)

#男女別に勝ちの平均回数、勝ちの最大値、勝ちの最小値を表示
display(hand_df.groupby('性別')['勝ち'].mean())
display(hand_df.groupby('性別')['勝ち'].max())
display(hand_df.groupby('性別')['勝ち'].min())

#勝ちの回数でソートする
display(hand_df.勝ち.sort_values())

#あいこを欠損値にする
hand_df.あいこ = np.nan
display(hand_df)

#欠損値がいくつあるかを調べる
display(hand_df.isnull().sum())