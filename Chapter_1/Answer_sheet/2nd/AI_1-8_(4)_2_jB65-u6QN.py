#AI-TECHGYM-1-8-A-3
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

from janome.tokenizer import Tokenizer

#形態素解析のオブジェクト
text = Tokenizer()

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()

tokens = text.tokenize('すもももももももものうち', wakati=True)
print(tokens)

print("\n")

ls_wakati = []
lines = txt.split("\n")
for line in lines:
  text_w = text.tokenize(line, wakati=True)
  ls_wakati.extend(text_w)
  ls_wakati.extend('\n')

print(ls_wakati)
text_file.close()