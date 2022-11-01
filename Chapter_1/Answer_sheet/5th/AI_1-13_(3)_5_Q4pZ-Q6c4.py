#AI-TECHGYM-1-13-Q-1
#自然言語処理

# word2vec データ読み込み
from gensim.models import KeyedVectors

# 実行場所
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#ファイルの準備
import os
import urllib.request
import csv

with open('words.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      print(row)

# word_set = []
# for 

#コサイン類似度
# print("「Java」と「PHP」のコサイン類似度")
# ret_s = w2v.n_similarity(['Java'],['PHP']) 
# print(ret_s)