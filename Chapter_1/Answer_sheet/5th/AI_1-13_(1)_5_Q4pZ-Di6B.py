#AI-TECHGYM-1-13-Q-1
#自然言語処理

# word2vec データ読み込み
from gensim.models import KeyedVectors

# 実行場所
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#ファイルの準備
import os
import urllib.request

title = "stanby-jobs-200d-word2vector.bin"
if not os.path.exists(title):
    print(title + " DOWNLOAD.")
    url = "https://github.com/bizreach/ai/releases/download/2018-03-13/stanby-jobs-200d-word2vector.bin"
    urllib.request.urlretrieve(url,"{0}".format(title))
else :
    print(title + " EXIST.")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

#計算した結果近い単語が出てくる
print("「テクノロジー」")
words = w2v.most_similar('テクノロジー', topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」+「金融」")
words = w2v.most_similar(positive=['テクノロジー','金融'], topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」+「金融」-「IT」")
words = w2v.most_similar(positive=['テクノロジー','金融'],negative=['IT'], topn=5)
for word in words:print(word)
print('\n')


#similar_by_vector()メソッド
print("「テクノロジー」")
words = w2v.similar_by_vector('テクノロジー', topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」+「金融」")
words = w2v.similar_by_vector(positive=['テクノロジー','金融'], topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」+「金融」-「IT」")
words = w2v.similar_by_vector(positive=['テクノロジー','金融'],negative=['IT'], topn=5)
for word in words:print(word)
print('\n')