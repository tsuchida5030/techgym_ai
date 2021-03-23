#AI-TECHGYM-N-14

import pandas as pd
import urllib

import os
os.chdir('C:/Users/tsuchida/Documents/techgym_セミナー/TortoiseGit_resorce/techgym_ai/Chapter_0/Answer_sheet/AI_Chapter0_saved_files')

#Seaborn
import seaborn as sns

import matplotlib.pyplot as plt
%matplotlib inline

#データの取得
data = "https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data"
TTT = pd.read_csv(data,header=None)

txt= "https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.names"
urllib.request.urlretrieve(txt, './tic-tac-toe.names')

#説明文の表示(必要であれば表示)
#f = open("./tic-tac-toe.names","r")
#for line in f:
#    print(line)
#f.close()

#データの個数や型を確認
TTT.info()

#indexを説明からつける
columns_name = ['top-left','top-middle','top-right',
                'middle-left','middle-middle','middle-right',
                'bottom-left','bottom-middle','bottom-right','P-N']
TTT.columns = columns_name

#必要であれば表示して確認
# display(TTT)


# グラフの大きさを指定
plt.figure(figsize=(10, 10))
sns.countplot(x='P-N',data=TTT,hue='middle-middle',hue_order=['x','o','b'])

#真ん中をとったときの調査
pd.crosstab(TTT['middle-middle'], TTT['P-N'])