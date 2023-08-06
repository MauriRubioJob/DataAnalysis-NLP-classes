# Tagging I
# Tag the following text in english.
# Also, the function pos_tag can receive 2 arguments: the text and the language. Set the language to "universal" an spot the differences from english

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

text = '''
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.
'''

tokens = word_tokenize(text)
tags1 = pos_tag(tokens)
tags2 = pos_tag(tokens, tagset="universal")

print(tags1)
print(tags2)