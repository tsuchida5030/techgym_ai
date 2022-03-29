  #AI-TECHGYM-1-9-Q
#自然言語処理

#インポート
from gensim.models import Word2Vec
from gensim.models.word2vec import Word2Vec

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]

model = Word2Vec(sentences, min_count=1)
print(len(model.wv['猫']))
print(model.wv['猫'])