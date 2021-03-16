#AI-TECHGYM-N-1

#pandasライブラリの読み込み
import pandas as pd

hand_df = pd.Series(['グー','チョキ','パー'])

#データフレームの表示
print(hand_df)

#チョキのみを表示
print(hand_df[1])

#データ型の表示
print(hand_df.dtypes)

#indexの変更
hand_df = pd.Series(['グー','チョキ','パー'], index=['a', 'b', 'c'])
print(hand_df)

#indexの表示
print(hand_df.index)