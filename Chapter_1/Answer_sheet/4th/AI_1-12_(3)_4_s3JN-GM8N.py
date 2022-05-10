#AI-TECHGYM-1-12-A-2
#自然言語処理

#インポート
from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

#PCA
from sklearn.decomposition import PCA

#フォントの準備
import urllib.request as req
url = "https://github.com/hokuto-HIRANO/Word2Vec/raw/master/font/Osaka.ttc"
req.urlretrieve(url, "./Osaka.ttc")

#フォントの指定
FONTPATH='./Osaka.ttc'
prop = font_manager.FontProperties(fname=FONTPATH)

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

#単語ベクトルの可視化
def draw_2d_2groups(vectors, target1, target2, topn=100):
    similars1 = [w[0] for w in vectors.wv.most_similar(target1, topn=topn)]
    similars1.insert(0, target1)
    similars2 = [w[0] for w in vectors.wv.most_similar(target2, topn=topn)]
    similars2.insert(0, target2)
    similars = similars1 + similars2
    colors = ['b']+['g']*(topn)+ ['r']+['orangered']*(topn)
    X = [vectors.wv[w] for w in similars]
    pca = PCA(n_components=2)
    Y = pca.fit_transform(X)
    plt.figure(figsize=(20,20))
    plt.scatter(Y[:,0], Y[:,1], color=colors)
    for w, x, y, c in zip(similars[:], Y[:,0], Y[:,1], colors):
        plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=15, color=c)
    plt.show()

vectors = []

for w in words:
    vectors.append(model.wv[w])

#単語のベクトル表現を2次元に圧縮する
pca = PCA(n_components=2)
pca.fit(vectors)
vectors_pca = pca.transform(vectors)

for w in vectors_pca:
    #配列形式に整形
    print(np.array2string(w, separator=', ', formatter={'float_kind': lambda x: '{: .4f}'.format(x)}))

# グラフの縦軸・横軸の目盛間隔を揃える
plt.figure(figsize = (8, 8))
plt.gca().set_xlim(-16, 16)
plt.gca().set_ylim(-16, 16)

#ブロットする
k = 0
while k < len(vectors_pca):
    #点プロット
    plt.plot(vectors_pca[k][0], vectors_pca[k][1], ms=5.0, zorder=2, marker="o")
 
    #文字プロット
    plt.annotate(words[k], (vectors_pca[k][0], vectors_pca[k][1]), fontproperties=prop, fontsize=15)
    # 引数に'xy=()'が省略されて'()'と書かれている
    
    k += 1

# plt.grid(color='k', linestyle='--', linewidth=0.5)

# y=0に水平線を引く
# plt.axhline(0, ls = "-.", color = "magenta")
plt.axhline(0, ls = "-.", color = "m")

# x=0に垂直線を引く
# plt.axvline(0, ls = "--", color = "navy")
plt.axvline(0, ls = "--", color = "b")

#グラフ表示
plt.show()

