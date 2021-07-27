#AI-TECHGYM-1-15-Q-1
#自然言語処理

#インポート
from gensim.models import KeyedVectors
import os

os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

def show_most_similar():
  print("単語を入力してください。\n")
  word = input()
  try:
    result = w2v.wv.most_similar(positive=[word])
    print(result[0])
  except Exception as e:
    show_most_similar()

show_most_similar()