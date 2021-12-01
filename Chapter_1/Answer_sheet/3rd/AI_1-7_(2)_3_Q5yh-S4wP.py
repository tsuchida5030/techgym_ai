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
# display(trans.groupby('cancel_flg').size())

#有効なデータに上書きする
trans = trans[(trans.cancel_flg == '5') & (trans.CustomerID.notnull())]
################

display(trans.groupby('StockCode').size().sort_values(ascending=False).head())

print('全ての購買データのバスケット数:{}'.format(len(set(trans.InvoiceNo))))
print('商品85123Aを購入したバスケット数:{}'.format(len(set(trans[trans.StockCode == '85123A'].InvoiceNo))))
print('商品47566を購入したバスケット数:{}'.format(len(set(trans[trans.StockCode == '47566'].InvoiceNo))))
print('商品85123Aかつ商品47566を購入したバスケット数:{}'.format(len(set(trans[(trans.StockCode == '85123A') & (trans.StockCode == '47566')].InvoiceNo))))