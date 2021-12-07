#AI-TECHGYM-1-8-Q
#自然言語処理

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer
import re

path = './techgym-AI.txt'

with open(path) as f:
  s = f.read()
  print(type(s))
  print(s[:50])

# 改行文字を除く処理
s_line = re.sub('\n', '', s)

# 'すももも・・・」'について
t = Tokenizer()
tokens = t.tokenize('すもももももももものうち', wakati=True)
ls_sumomo = []
for token in tokens:
  ls_sumomo.append(token)
print()
print(ls_sumomo)

# テックジム紹介文について
t = Tokenizer()
tokens = t.tokenize(s_line, wakati=True)
ls_tg = []
for token in tokens:
  ls_tg.append(token)

print(ls_tg)