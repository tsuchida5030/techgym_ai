#AI-TECHGYM-1-7-A-2
#教師なし学習 アソシエーション分析

import pandas as pd
import urllib.request as req

%matplotlib inline

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#githubからファイルをDownloadできない場合は以下を実行
#url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
#req.urlretrieve(url, "Online_Retail.xlsx")
#trans = pd.read_excel('Online_Retail.xlsx', sheet_name='Online Retail')
#trans.to_csv("./Online_Retail.csv")

#購買データの読み込み
trans = pd.read_csv('Online_Retail.csv')

#####前処理#####
#キャンセルデータと不明なデータを除くための処理をする

# InoivceNoの先頭1文字をcancel_flgとして追加
trans['cancel_flg'] = trans.InvoiceNo.map(lambda x:str(x)[0])

# cancel_flgでグルーピングして集計
trans.groupby('cancel_flg').size()

#有効なデータに上書きする
trans = trans[(trans.cancel_flg == '5') & (trans.CustomerID.notnull())]
################

#すべてのInvoiceNoをtrans_allとして抽出
trans_ALL = set(trans.InvoiceNo) 
# print("すべての購買データ　　　　　 :",end='')
# print(len(trans_ALL))

trans_X = set(trans[trans['StockCode']=='85123A'].InvoiceNo)
trans_Y = set(trans[trans['StockCode']=='47566'].InvoiceNo)

#商品85123Aかつ商品47566を購入したデータをtrans_XYとする
trans_XY = trans_X & trans_Y

#商品85123Aを購入した人の中で、商品47566を購入した人の割合を示す信頼度(C)
C = len(trans_XY)/len(trans_X)
print("商品85123Aを購入している時、商品47566を購入する信頼度　　　　　　 :",end='')
print(C)

#商品85123Aと商品47566が同時に購入されたかどうかを示す支持度(S_XY)
S_XY = len(trans_XY) / len(trans_ALL)
print("商品85123Aと商品47566を同時に購入する支持度　　　　　　　:",end='')
print(S_XY)

#商品85123Aを購入するなら商品47566も購入するというルールのリスト値
print("商品85123Aを購入するなら商品47566も購入するというルールのリフト値　　　　　　　:",end='')
print(C / S_XY)