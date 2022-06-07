#AI-TECHGYM-1-15-Q-1
#自然言語処理

#インポート
from gensim.models import KeyedVectors
import os

# 実行フォルダ
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

print("単語を入力してください。\n")
word = input()

try:
  print(w2v.most_similar(word, topn=5))
except Exception as e:
  print('モデルに含まれていません。')