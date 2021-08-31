#AI-TECHGYM-1-8-A-1
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer
import re

with open('./techgym-AI.txt') as f:
  text = f.read()

print(text)

t = Tokenizer()
tokens = t.tokenize(re.sub('\n', '', text))

for token in tokens:
  print(token)