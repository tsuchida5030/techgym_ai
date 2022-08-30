#AI-TECHGYM-1-9-Q
#自然言語処理

#インポート
from gensim.models import Word2Vec
import numpy as np

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, vector_size=100,min_count=1,window=5,epochs=100)

# vector = model.wv['猫']
# print(vector.shape)
# print(vector)

vec_cat = model.wv['猫']
vec_dog = model.wv['犬']

print(np.dot(vec_cat, vec_dog)/(np.linalg.norm(vec_cat) * np.linalg.norm(vec_dog)))
print(model.wv.n_similarity('猫', '犬'))