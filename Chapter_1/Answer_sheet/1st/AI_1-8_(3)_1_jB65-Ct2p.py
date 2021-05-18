#AI-TECHGYM-1-8-Q
#自然言語処理

from janome.tokenizer import Tokenizer

import os
os.chdir("C:/Users/tsuchida/Documents/techgym_セミナー/TortoiseGit_resorce/techgym_ai/Chapter_1/Answer_sheet/AI_Chapter1_saved_files")

f = open('techgym-AI.txt')
s = f.read()
print(s)
print()
print('以下、形態素解析の結果')
print('**************************************')

t = Tokenizer()
tokens = t.tokenize(s)

for token in tokens:
  print(token)

f.close()