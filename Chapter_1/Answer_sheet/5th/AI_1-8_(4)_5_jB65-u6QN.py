#AI-TECHGYM-1-8-A-3
#自然言語処理

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer

#形態素解析のオブジェクト
text = Tokenizer()

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()

lists_c = []
#読み込んだデータを形態素解析
lines = txt.split("\n")
for i in lines:
  # print(i)
  # print("\n")
  list_c = text.tokenize(i, wakati=True)
  lists_c.extend(list_c)
  # print("\n")

print(lists_c)