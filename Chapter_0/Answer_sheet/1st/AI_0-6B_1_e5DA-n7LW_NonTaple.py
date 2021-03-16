#AI-TECHGYM-N-6B

import pandas as pd

num = ['0','1','2','3','4','5','6','7','8','9']
feature1 =['gender','age','win','lose','draw']

hand = {'性別'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
        '年齢'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
        '勝ち'  :[20,21, 4,60,14,10,12,19,12,14],
        '負け'  :[24,15,35, 3,35,29, 2,12,11,43],
        'あいこ':[15,40,34,29,14, 4,22,17,12,10]}
hand_df1 = pd.DataFrame(hand)

#index,columnsをつける
hand_df1.columns = [feature1]
hand_df1.columns.names = ['feature']

#必要であれば表示して確認する
#display(hand_df1)

#idを追加してindexとして用いる
id1 = ['100','101','102','103','104','105','106','107','108','109']
hand_df1.index = id1
hand_df1.index.names = ['id']

#必要であれば表示して確認する
#display(hand_df1)

feature2 =['address','hobby','job']

hand2 = {'住所'  :['東京','大阪','名古屋','北海道','東京','鹿児島','大阪','名古屋','東京','大阪'],
        '趣味'  :['野球','賭博','じゃんけん','野球','賭博','野球','じゃんけん','賭博','野球','じゃんけん'],
        '仕事'  :['IT','医療','弁護士','事務','事務','弁護士','IT','IT','IT','事務']}

hand_df2 = pd.DataFrame(hand2)
hand_df2.columns = [feature2]
hand_df2.columns.names = ['feature']

#必要であれば表示して確認する
#display(hand_df2)

#idを追加してindexとして用いる
id2 = pd.Series(['100','101','102','103','110','111','106','113','108','114'])
hand_df2.index = id2
hand_df2.index.names = ['id']

#必要であれば表示して確認する
print(f'デバッグ：index[0]')
print(hand_df2.index[0])
print(type(hand_df2.index[0]))

#内部結合する(両方にキーidがあるデータで結合)
display(pd.merge(hand_df1, hand_df2, on = 'id'))

#全結合する(どちらかにキーidがあるデータで結合)
display(pd.merge(hand_df1, hand_df2, on = 'id', how = 'outer'))

#左外部結合する(hand_df1のデータを全て取り出し、hand_df2のデータがあるときは結合する)
display(pd.merge(hand_df1, hand_df2, on = 'id', how = 'left'))


#右外部結合する(hand_df2のデータを全て取り出し、hand_df1のデータがあるときは結合する)
display(pd.merge(hand_df1, hand_df2, on = 'id', how = 'right'))

