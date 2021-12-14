#AI-TECHGYM-1-10-Q-1
#自然言語処理

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#ライブラリのインポート
from janome.tokenizer import Tokenizer
import re

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()

t = Tokenizer()
lines = txt.split("\n")

ls_techgym = []
# 読み込んだデータを文ごとにリストに格納
for i in lines:
  ls_techgym.append(t.tokenize(i,wakati=True))

text_file.close()

print(ls_techgym)