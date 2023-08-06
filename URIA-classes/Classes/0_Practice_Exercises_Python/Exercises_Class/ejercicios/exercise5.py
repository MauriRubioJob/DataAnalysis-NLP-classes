# Tagging I 
# Tag the following text in english.
# Also, the function pos_tag can receive 2 arguments: the text and the language. Set the language to "universal" an spot the differences from english

from nltk.tag import pos_tag
from nltk import word_tokenize

text = '''Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.'''

tokens = word_tokenize ( text )

print("Tagging normal")
tags_eng = pos_tag(tokens)
print(tags_eng)

print("\n")

print("Tagging con tagset universal")
tags_universal = pos_tag ( tokens, tagset = "universal" )
print(tags_universal)


