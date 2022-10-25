#AI-TECHGYM-1-12-A-1
#自然言語処理

#インポート
from gensim.models import word2vec
import numpy as np

#PCA
from sklearn.decomposition import PCA

#モデルの読み込み
model_path = './words.model'
model = word2vec.Word2Vec.load(model_path)

#対象の単語
words = []
words.append("老人")
words.append("海")
words.append("ヘミングウェイ")
words.append("魚")
words.append("彼")

vectors = []

for w in words:
  vectors.append(model.wv[w])

#単語のベクトル表現を2次元に圧縮する
pca = PCA(n_components=2)
pca.fit(vectors)
vectors_pca= pca.transform(vectors)

for w in vectors_pca:
  #配列形式に整形
  print(np.array2string(w, separator=', ', formatter={'float_kind': lambda x: '{: .4f}'.format(x)}))

colors = ['blue', 'orange', 'cyan', 'red', 'gray']
plt.figure(figsize=(12,12))
for v, c, w in zip(vectors_pca, colors, words):
  plt.scatter(v[0], v[1], color=c, label=w)
for w, x, y in zip(words, vectors_pca[:,0], vectors_pca[:,1]):
  plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=15)
plt.show()