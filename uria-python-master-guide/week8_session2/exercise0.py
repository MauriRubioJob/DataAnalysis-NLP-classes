# Write a Python NLTK program to split the text sentence/paragraph into a list of words.

from nltk.tokenize import word_tokenize


text = """
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.
"""

tokens = word_tokenize(text)
print(tokens)
