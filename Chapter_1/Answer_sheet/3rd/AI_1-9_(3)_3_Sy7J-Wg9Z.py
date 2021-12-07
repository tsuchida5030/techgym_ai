#AI-TECHGYM-1-9-Q
#自然言語処理

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
from gensim.models import Word2Vec
import numpy as np

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, min_count=1)

vec_cat = model.wv['猫']
vec_dog = model.wv['犬']

print(np.dot(vec_cat, vec_dog)/(np.linalg.norm(vec_cat)*np.linalg.norm(vec_dog)))
print(model.wv.n_similarity('猫', '犬'))