#AI-TECHGYM-1-15-A-1
#自然言語処理

#インポート
from gensim.models import KeyedVectors

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)


print("連想ゲームのはじめの単語を入力してください(終了:Q)\n")
word = ""
while word != "Q":
  word = input()
  if word != "Q":
    try:
        job = w2v.most_similar(word,topn=1)
    except :
        print("モデルにない単語です。\n")
    #連想した単語
    word_sim = job[0][0]
    #類似
    print("'" + word + "'といったら'" + word_sim + "'です。\n")
    print("'" + word_sim + "'といったら？")