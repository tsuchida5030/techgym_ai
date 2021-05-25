#AI-TECHGYM-1-10-A-2
#自然言語処理

#インポート
from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec

#形態素解析のオブジェクト
text = Tokenizer()

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()
 
#読み込んだデータを形態素解析
results = []
lines = txt.split("\n")
for i in lines:
    text_c = text.tokenize(i,wakati=True)
    results.append(text_c)

model = Word2Vec(results, min_count=1)

print(model.wv['プログラミング'])

programing = model.wv.most_similar(positive='プログラミング')

for item in programing[:5]:
  print(item[0], item[1])