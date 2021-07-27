#AI-TECHGYM-1-15-A-1
#自然言語処理

#インポート
from gensim.models import KeyedVectors
import os

os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

def show_similar():

  print("単語を入力してください。\n")
  word = input()

  try:
    job = w2v.most_similar(word,topn=20)
  except :
    print("モデルにない単語です。\n")
    show_similar()

  #連想した単語
  word_sim = job[0][0]

  #類似
  print("最も似ている単語は'" + word_sim + "'です。\n")

  return job

job = show_similar()
