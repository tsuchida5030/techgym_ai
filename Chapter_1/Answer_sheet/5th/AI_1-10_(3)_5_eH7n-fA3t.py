#AI-TECHGYM-1-10-Q-1
#自然言語処理

#ファイル格納場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
from gensim.models import Word2Vec
from janome.tokenizer import Tokenizer


#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()

#読み込んだデータを表示
# display(txt)
lines = txt.split("\n")
# print(lines)

#読み込んだデータを形態素解析
lists_c = []
t = Tokenizer()
for i in lines:
  list_c = t.tokenize(i, wakati=True)
  lists_c.append(list_c)

model = Word2Vec(lists_c, window=5, min_count=1, epochs=5)
pro = model.wv.most_similar(positive=['プログラミング'])

for item in pro[:5]:
  print(item[0]+'　'*(10-len(item[0])), item[1])