#AI-TECHGYM-1-13-Q-1
#自然言語処理

# word2vec データ読み込み
from gensim.models import KeyedVectors

#ファイルの準備
import os
import urllib.request
import csv

# モデルとフォント形式ファイルの場所
os.chdir(r"C:\Users\tsuchida\OneDrive - 田中鉄工株式会社\ドキュメント\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

with open("word.csv", encoding="utf_8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


#コサイン類似度
ret_s = w2v.n_similarity(['JAVA'],['PHP']) 
print(ret_s)

#numpyを使って計算
#コサイン類似度を使う
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

word1 = "JAVA"
word2 = "PHP"
print(cos_sim(w2v[word1], w2v[word2]))