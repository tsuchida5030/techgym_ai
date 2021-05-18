#AI-TECHGYM-1-8-Q
#自然言語処理

from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()

sentence = 'すもももももももものうち'

print(sentence)

for token in tokenizer.tokenize(sentence):
  print("    " + str(token))