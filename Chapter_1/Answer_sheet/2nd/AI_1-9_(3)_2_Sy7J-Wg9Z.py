#AI-TECHGYM-1-9-A-2
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
from gensim.models import Word2Vec
import numpy as np

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, min_count=1)

#類似している単語を出力する
cat = model.wv['猫'] 
dog = model.wv['犬']

# 「犬」と「猫」コサイン類似度
print(np.dot(cat, dog) / (np.linalg.norm(cat) * np.linalg.norm(dog)))
print(model.wv.n_similarity("猫", "犬"))