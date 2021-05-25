#AI-TECHGYM-1-9-A-1
#自然言語処理

#インポート
from gensim.models import Word2Vec

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, min_count=1)

print(model.wv.most_similar('猫'))