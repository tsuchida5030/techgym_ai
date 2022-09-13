#AI-TECHGYM-1-11-Q-1
#自然言語処理

#実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_1\Answer_sheet\AI_Chapter1_saved_files")

#インポート
import urllib.request
import zipfile

#インポート
from gensim.models import Word2Vec
from janome.tokenizer import Tokenizer

# ファイル整形
import re

#ファイルダウンロード
url = 'https://www.aozora.gr.jp/cards/001847/files/57347_ruby_57225.zip'
zip = '57347_ruby_57225.zip'
urllib.request.urlretrieve(url, zip)

# ダウンロードしたzipの解凍
with zipfile.ZipFile(zip, 'r') as myzip:
  myzip.extractall()
  # 解凍後のファイルからデータ読み込み
  for myfile in myzip.infolist():
    # 解凍後ファイル名取得
    filename = myfile.filename
    # ファイルオープン時にencodingを指定してsjisの変換をする
    with open(filename, encoding='sjis') as file:
      text = file.read()

# 加工前の全文表示
# print(text)
# print('以下、加工後')
# print()

text = re.split('\-{5,}',text)[2]   # ヘッダ部分の除去
text = re.split('底本：',text)[0]   # フッタ部分の除去
text = text.replace('|', '')        # | の除去
text = re.sub('《.+?》', '', text)  # ルビの削除
text = re.sub('［＃.+?］', '',text) # 入力注の削除
text = re.sub('\n\n', '', text)   # 空行の削除
text = re.sub('\u3000', '', text)   # 全角スペースの削除
text = re.sub('\r', '', text)

# outnum = 50
# 頭の50文字の表示
# print(text[:outnum])
# print("…")
# 後ろの50文字の表示
# print(text[-outnum:])

t = Tokenizer()
#読み込んだデータを形態素解析
results = []
lines = text.split("\n")
for i in lines:
    text_c = t.tokenize(i,wakati=True)
    results.append(text_c)

# print(lines[0:5])
# print()
# print(results[0])

#モデル
model = Word2Vec(results, window=5, min_count=2, epochs=5)
oldman = model.wv.most_similar(positive=['老人'])
sea = model.wv.most_similar(positive=['海'])

print('「老人」に類似する単語の上位5個')
for item in oldman[:5]:
  print(item[0]+'　'*(10-len(item[0])), item[1])

print('「海」に類似する単語の上位5個')
for item in sea[:5]:
  print(item[0]+'　'*(10-len(item[0])), item[1])

print()
print('「老人」と「海」のコサイン類似度：{}'.format(model.wv.n_similarity(['老人'], ['海'])))
print()

print('「海」から「老人」を引いたものに最も類似する単語の上位5個')
sea_minus_old = model.wv.most_similar(positive=['海'], negative=['老人'])
for item in sea_minus_old[:5]:
  print(item[0]+'　'*(10-len(item[0])), item[1])

print('「海」へ「老人」を加えたものに最も類似する単語の上位5個')
sea_plus_old = model.wv.most_similar(positive=['海','老人'])
for item in sea_plus_old[:5]:
  print(item[0]+'　'*(10-len(item[0])), item[1])