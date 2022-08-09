#AI-TECHGYM-1-8-Q
#自然言語処理

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer
import re

texts = []
with open('techgym-AI.txt') as f:
  for i in f:
    texts.append(re.sub('\n', '', i))

Tokens = []
for text in texts:
  print(text)
  tokens = t.tokenize(text)
  for token in tokens:
    Tokens.append(token)

print()

for token in Tokens:
  print(token)