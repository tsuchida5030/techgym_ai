#AI-TECHGYM-1-9-A-1
#自然言語処理

#インポート
from gensim.models.word2vec import Word2Vec

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, min_count=1)

# vector = model.wv['猫']

print(model.wv.most_similar(positive=['猫']))