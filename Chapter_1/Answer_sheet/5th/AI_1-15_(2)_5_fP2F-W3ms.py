#AI-TECHGYM-1-15-Q-1
#自然言語処理

#インポート
from gensim.models import KeyedVectors
import os

os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

print("連想ゲームのはじめの単語を入力してください。\n")

i = 1
while True:
  word = input()
  if word == "Q":
    break

  try:
    job = w2v.most_similar(word,topn=1)
    hantei = True
  except :
    hantei = False

  if hantei == True:
    print('\'{1}\'といったら\'{2}\'です。\n'.format(word, job[0][0]))
    print('\'{}\'といったら？\n'.format(job[0][0]))
  else:
    print("モデルにない単語なのでもう一度入力してください。\n")
