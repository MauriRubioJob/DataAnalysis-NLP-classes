from nltk.tag import pos_tag
from nltk import word_tokenize

texto = "Here you can find activities to practise your reading skills. Reading will help you to improve your understanding of the language and build your vocabulary."

tokens = word_tokenize(texto)

tags = pos_tag(tokens)

tok = []
etiq = []
for tag in tags:
    tok.append(tag[0])
    etiq.append(tag[1])

print(tok)
print(etiq)
