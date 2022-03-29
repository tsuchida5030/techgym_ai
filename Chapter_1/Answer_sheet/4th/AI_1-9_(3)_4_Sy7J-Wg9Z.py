#AI-TECHGYM-1-9-A-2
#自然言語処理

#インポート
from gensim.models import Word2Vec
import numpy as np

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, min_count=1)

#類似している単語を出力する
cat = model.wv.most_similar(positive=['猫']) 
#cat = model.wv.similar_by_vector('猫') 
#cat = model.wv.similar_by_word('猫') 

vec_cat = model.wv['猫']
vec_dog = model.wv['犬']

# 計算した「猫」と「犬」のコサイン類似度
naiseki = np.dot(vec_cat,vec_dog)
norm1 = np.linalg.norm(vec_cat)
norm2 = np.linalg.norm(vec_dog)
print(naiseki / (norm1 * norm2))

# メソッドによるコサイン類似度
print(model.wv.n_similarity('猫', '犬'))