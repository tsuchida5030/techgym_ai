﻿#AI-TECHGYM-1-10-Q-1
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer
t = Tokenizer()

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()

# ls_tokens = []
#読み込んだデータを表示
# lines = txt.split("\n")
# for i in lines:
#   tokens = t.tokenize(i)
#   ls_tokens.append(tokens)
#   print(i)

tokens = t.tokenize(txt)
print(txt)

text_file.close()