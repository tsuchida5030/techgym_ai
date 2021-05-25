#AI-TECHGYM-1-9-A-2
#自然言語処理

#インポート
import numpy as np
from gensim.models import Word2Vec

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, min_count=1)

vector_cat = model.wv['猫']
vector_dog = model.wv['犬']

inner_proc = np.dot(vector_cat, vector_dog)
norm_cat = np.linalg.norm(vector_cat)
norm_dog = np.linalg.norm(vector_dog)
cos_similarity = inner_proc / (norm_cat * norm_dog)
print(cos_similarity)
print(model.wv.n_similarity('猫', '犬'))