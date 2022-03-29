#AI-TECHGYM-1-10-Q-1
#自然言語処理

import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec
import numpy as np

#形態素解析のオブジェクト
t = Tokenizer()

#txtファイルからデータの読み込み
with open("./techgym-AI.txt") as f:
  txt = f.read()

#読み込んだデータを表示
results = []
lines = txt.split("\n")
for i in lines:
  tokens = t.tokenize(i, wakati=True)
  results.append(tokens)

# print(results)

model = Word2Vec(results, min_count=1)
print(model.wv['プログラミング'])

programing = model.wv.most_similar(positive=['プログラミング'])
for item in programing[:5]:
  print(item[0], item[1])