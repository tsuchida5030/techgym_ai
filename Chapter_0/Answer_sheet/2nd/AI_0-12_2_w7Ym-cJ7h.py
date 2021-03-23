#AI-TECHGYM-N-12

import pandas as pd

import os
os.chdir('C:/Users/tsuchida/Documents/techgym_セミナー/TortoiseGit_resorce/techgym_ai/Chapter_0/Answer_sheet/AI_Chapter0_saved_files')

#スクレイピングのために読み込み
import urllib

#データをCSVファイルから読み込む
data = "http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data"
urllib.request.urlretrieve(data, './adult+stretch.data')
balloons = pd.read_csv('adult+stretch.data', header=None)

#データの説明文をダウンロードする
txt = "http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/balloons.names"
urllib.request.urlretrieve(txt, './balloons.names')


#説明文の表示(必要であれば表示)
#f = open("./balloons.names","r")
#for line in f:
#    print(line)
#f.close()

#データの個数や型を確認
balloons.info()

#説明文からindexをつける
columns_name = ['color','size','act','age','inflated']
balloons.columns = columns_name

#表示
display(balloons)
