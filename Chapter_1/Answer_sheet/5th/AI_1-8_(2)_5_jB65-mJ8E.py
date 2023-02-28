﻿#AI-TECHGYM-1-8-Q
#自然言語処理

from janome.tokenizer import Tokenizer

t = Tokenizer()
tokens = t.tokenize('すももももももものうち')

for token in tokens:
  print(token.part_of_speech)

for token in tokens:
  print(token.base_form)