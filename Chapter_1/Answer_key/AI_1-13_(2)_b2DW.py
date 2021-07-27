#AI-TECHGYM-1-13-A-2
#自然言語処理

#インポート
import numpy as np

# word2vec データ読み込み
from gensim.models import KeyedVectors

import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

#コサイン類似度
ret_s = w2v.n_similarity(['Java'],['PHP']) 
print("コサイン類似度")
print(ret_s)

#numpyを使って計算する場合(コサイン類似度)
'''
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

word1 = "Java"
word2 = "PHP"
print(cos_sim(w2v[word1], w2v[word2]))
'''