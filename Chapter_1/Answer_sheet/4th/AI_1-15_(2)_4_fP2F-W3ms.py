#AI-TECHGYM-1-15-A-1
#自然言語処理

# 実行フォルダ
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
from gensim.models import KeyedVectors

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

print("単語を入力してください。\n")
word = input()

while word != 'Q':
  try:
    job = w2v.most_similar(word,topn=1)
  except Exception as e:
    print("モデルにない単語なのでもう一度入力してください。\n")
    word = input()
    continue
  #連想した単語
  word_sim = job[0][0]

  #類似
  print("'" + word + "'と言ったら'" + word_sim + "'です。\n")
  print("'" + word_sim + "'と言ったら？")

  word = input()