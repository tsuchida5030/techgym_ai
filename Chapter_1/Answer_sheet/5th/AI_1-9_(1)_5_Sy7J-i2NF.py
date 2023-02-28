﻿#AI-TECHGYM-1-9-Q
#自然言語処理

#インポート
from gensim.models import Word2Vec

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]

model = Word2Vec(sentences, vector_size=100,min_count=1,window=5,epochs=100)

vector = model.wv['猫']

print(len(vector))
print(vector)