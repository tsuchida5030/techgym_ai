#AI-TECHGYM-1-12-Q-1
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

#PCA
from sklearn.decomposition import PCA

# k-means法を使うためのインポート
from sklearn.cluster import KMeans
import pandas as pd

#フォントの指定
FONTPATH='./Osaka.ttc'
prop = font_manager.FontProperties(fname=FONTPATH)

#モデルの読み込み
model_path = './words.model'
model = word2vec.Word2Vec.load(model_path)

#単語ベクトルの可視化
def draw_2d_2groups(vectors, target1, target2, topn=100):
    similars1 = [w[0] for w in vectors.wv.most_similar(target1, topn=topn)]
    similars1.insert(0, target1)
    similars2 = [w[0] for w in vectors.wv.most_similar(target2, topn=topn)]
    similars2.insert(0, target2)
    similars = similars1 + similars2
    # colors = ['b']+['g']*(topn)+ ['r']+['orangered']*(topn)
    X = [vectors.wv[w] for w in similars]
    pca = PCA(n_components=2)
    Y = pca.fit_transform(X)
    df_Y = pd.DataFrame(Y, columns=['x', 'y'])
    # display(df_Y)

    # KMeansクラスの初期化
    kmeans = KMeans(init='random', n_clusters=3, random_state=0)
    # クラスターの重心を計算
    kmeans.fit(df_Y)
    # クラスター番号をpandasのSeriesオブジェクトに変換
    labels = pd.Series(kmeans.labels_, name='cluster_number')
    # クラスター番号をdf_Yに追加する
    df_Y = pd.concat([df_Y, labels], axis=1)
    # display(df_Y)
    colors = []
    for number in df_Y['cluster_number']:
        if number == 0:
            colors.append('g')
        elif number == 1:
            colors.append('orangered')
        else:
            colors.append('c')
    colors[0] = 'b'
    colors[101] = 'r'
    # print(similars)

    # グラフの縦軸・横軸の目盛間隔を揃える
    plt.figure(figsize = (20, 20))
    plt.gca().set_xlim(-6, 6)
    plt.gca().set_ylim(-6, 6)
    plt.scatter(df_Y.iloc[:,0], df_Y.iloc[:,1], color=colors)

    # y=0に水平線を引く
    plt.axhline(0, ls = "-.", color = "m")
    # x=0に垂直線を引く
    plt.axvline(0, ls = "--", color = "b")

    for w, x, y, c in zip(similars[:], Y[:,0], Y[:,1], colors[:]):
        plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=15, color=c)
    plt.show()

draw_2d_2groups(model, '老人', '海')