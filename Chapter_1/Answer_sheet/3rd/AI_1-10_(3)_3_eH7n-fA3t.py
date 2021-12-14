#AI-TECHGYM-1-10-Q-1
#自然言語処理

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#ライブラリのインポート
from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()
text_file.close()

t = Tokenizer()
lines = txt.split("\n")

results = []
# 読み込んだデータを文ごとにリストに格納
for i in lines:
  results.append(t.tokenize(i,wakati=True))

# print(results[0])
# print(type(results[0]))

model = Word2Vec(results, min_count=1)
vec_pg = model.wv['プログラミング']
print(vec_pg)

for block in model.wv.most_similar('プログラミング')[:5]:
  print(block[0], end=' ')
  print(block[1])