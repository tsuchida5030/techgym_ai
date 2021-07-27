#AI-TECHGYM-1-13-Q-1
#自然言語処理

# word2vec データ読み込み
from gensim.models import KeyedVectors

#ファイルの準備
import os
import urllib.request

# モデルとフォント形式ファイルの場所
import os
os.chdir(r"C:\Users\tsuchida\OneDrive - 田中鉄工株式会社\ドキュメント\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

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