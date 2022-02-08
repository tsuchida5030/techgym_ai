#AI-TECHGYM-1-15-Q-1
#自然言語処理

#インポート
from gensim.models import KeyedVectors
import os
import numpy as np
import pandas as pd
from gensim.models import word2vec

os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

print("単語を入力してください。\n")
word = input()

try:
  sim_word = w2v.most_similar(word)[0][0]
  print('{0}といったら{1}です。'.format(word, sim_word) + '\n')
  print('{}と言ったら？'.format(sim_word))
except:
  print('モデルにない単語なのでもう一度入力してください。')