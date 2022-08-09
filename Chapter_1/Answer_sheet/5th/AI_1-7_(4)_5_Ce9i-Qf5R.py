#AI-TECHGYM-1-7-Q-1
#教師なし学習 アソシエーション分析

#インポート
import pandas as pd
import urllib.request as req

%matplotlib inline

#実行フォルダ
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#githubからファイルをDownloadできない場合は以下を実行
# url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
# req.urlretrieve(url, "Online_Retail.xlsx")
# trans = pd.read_excel('Online_Retail.xlsx', sheet_name='Online Retail')
# trans.to_csv("./Online_Retail.csv")

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

# trans.groupby('StockCode').size().sort_index()

set_Invoice = set(trans.InvoiceNo)
print(len(set_Invoice))

set_85123A = set(trans[trans.StockCode == '85123A'].InvoiceNo)
print(len(set_85123A))

set_47566 = set(trans[trans.StockCode == '47566'].InvoiceNo)
print(len(set_47566))

set_And = set_85123A & set_47566
print(len(set_And))

C = len(set_And) / len(set_85123A)
S_XY = len(set_And) / len(set_Invoice)
S_Y = len(set_47566) / len(set_Invoice)

print(C)
print(S_XY)
print(C / S_Y)

print('考察：購入者全員に対する旗を買う人の比率よりも、ハート形のキャンドルを買った人のうちで旗も一緒に買う人の比率の方が多い')