#AI-TECHGYM-1-8-A-1
#自然言語処理

import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer

file_path = './techgym-AI.txt'
with open(file_path) as f:
  text = f.read()

sentences = text.split('\n')

t = Tokenizer()
for s in sentences:
  tokens = t.tokenize(s)
  for token in tokens:
    print(token)