﻿#AI-TECHGYM-1-15-A-1
#自然言語処理

#インポート
from gensim.models import KeyedVectors

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

print("連想ゲームのはじめの単語を入力してください(終了:Q)\n")
word = input()

while word != 'Q':
  try:
    job = w2v.most_similar(word,topn=1)
    #連想した単語
    word_sim = job[0][0]
    #類似
    print('{0}といったら{1}です。\n'.format(word, word_sim))
    print('{}と言ったら？\n'.format(word_sim))
  except :
    print("モデルにない単語なのでもう一度入力してください。\n")
  word = input()