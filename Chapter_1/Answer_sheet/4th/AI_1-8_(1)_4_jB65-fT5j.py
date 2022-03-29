#AI-TECHGYM-1-8-Q
#自然言語処理

from janome.tokenizer import Tokenizer

sentence = 'すもももももももものうち'
tokenizer = Tokenizer()
tokens = tokenizer.tokenize(sentence)

for token in tokens:
  print(token)