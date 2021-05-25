#AI-TECHGYM-1-8-A-3
#自然言語処理

from janome.tokenizer import Tokenizer

import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

t = Tokenizer()
tokens = t.tokenize('すもももももももものうち', wakati=True)

print(tokens)

#形態素解析のオブジェクト
text = Tokenizer()

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()

# 読み込んだデータを形態素解析
lines = txt.split("\n")
p_list = []
for i in lines:
  text_c = text.tokenize(i, wakati=True)
  p_list.extend(text_c)

print(p_list)