#AI-TECHGYM-1-10-Q-1
#自然言語処理

import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#txtファイルからデータの読み込み
with open("./techgym-AI.txt") as f:
  txt = f.read()

#読み込んだデータを表示
lines = txt.split("\n")
for i in lines:
   print(i)