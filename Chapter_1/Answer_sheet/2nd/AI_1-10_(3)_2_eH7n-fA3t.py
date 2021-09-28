﻿#AI-TECHGYM-1-10-A-2
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec

#形態素解析のオブジェクト
text = Tokenizer()

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()

#読み込んだデータを形態素解析
results = []
lines = txt.split("\n")
for i in lines:
  text_c = text.tokenize(i,wakati=True)
  results.append(text_c)

#表示
# print(results)

model = Word2Vec(results, min_count=1)
vector = model.wv['プログラミング']

# ベクトル表現
print(vector)

similars = model.wv.most_similar(positive=['プログラミング'])

labels = []
values = []
for sim_term in similars:
  labels.append(sim_term[0])
  values.append(sim_term[1])
  # print('{} : {}'.format(sim_term[0], sim_term[1]))

values.sort(reverse=True)

for sim_term, value in zip(similars[0:5], values[0:5]):
  if value in sim_term:
    print('{} : {}'.format(sim_term[0], sim_term[1]))

#以下、linesからresultsへ変換する仮定で変化した点を確認するコード（それぞれ一次元、二次元配列のリスト）
# import numpy as np
# print('リスト linesの次元数、要素数 : 1, {}'.format(len(lines)))
# print('リスト resultsの次元数、要素数 : 2, {}'.format(len(results)))

# print('lines、resultsの外側の要素数は、元の文章の行数')

# print('resultsの　行数 : 内側のリストの要素数')
# for i, result in enumerate(results):
#     print('{} : {}'.format(i+1, len(result)))