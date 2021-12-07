#AI-TECHGYM-1-8-Q
#自然言語処理

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()

sentenses = ['すもももももももものうち']

for token in tokenizer.tokenize(sentence):
  print(token)