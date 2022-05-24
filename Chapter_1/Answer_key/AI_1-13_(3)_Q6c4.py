#AI-TECHGYM-1-13-A-3
#自然言語処理

#word2vec データ読み込み
from gensim.models import KeyedVectors
import pandas as pd
import urllib.request

import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

title = "stanby-jobs-200d-word2vector.bin"
if not os.path.exists(title):
    print(title + " DOWNLOAD.")
    url = "https://github.com/bizreach/ai/releases/download/2018-03-13/stanby-jobs-200d-word2vector.bin"
    urllib.request.urlretrieve(url,"{0}".format(title))
else :
    print(title + " EXIST.")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# データの読み込み
df = pd.read_csv("word.csv") 

# 読み込んだデータのサンプルを取得
co_df = df
display(co_df.head())

# 閾値を決める
THRESHOLD = 0.7

# 結果をlistで保存
result = []

# 類似度を計算
for i in df["words"].values:
    for j in co_df["words"].values:
        tmp = []
        # word2vecにない単語はスルーする
        try:
            similarity = w2v.similarity(i, j)
            # 類似度が0.99以上は同じ単語とする
            # 類似度がTHRESHOLD以上のものを抽出
            if similarity < 0.99 and similarity > THRESHOLD:
                tmp = [i,j,str(similarity)]
                result.append(tmp)
        except:
            pass

#リストを表示
print(result)

#データフレーム
df_result = pd.DataFrame(result,columns=["単語A","単語B","類似度"])
display(df_result)

#CSVファイルに保存
df_result.to_csv('./w2v_result.csv',index=False,encoding='shift-jis')

