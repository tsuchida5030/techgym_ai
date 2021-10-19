#AI-TECHGYM-1-13-Q-1
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# word2vec データ読み込み
from gensim.models import KeyedVectors

#ファイルの準備
import os
import urllib.request

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

#計算した結果近い単語が出てくる
print("「Java」と「PHP」のコサイン類似度")
print(w2v.similarity('Java', 'PHP'))