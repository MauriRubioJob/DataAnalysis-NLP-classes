# Cleaning II:

# Create a function that removes the stopwords of a text. The function must receive as arguments the text and the language, and return the cleaned text.

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


text1 = '''
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.
'''

text2 = '''
Python tuvo un papel crucial en este proceso: debido a su orientación hacia una sintaxis 
limpia, ya era idóneo, y las metas de CP4E presentaban similitudes con su predecesor.
'''

def clean_stopwords(text, lang):
    tokens = word_tokenize(text, language=lang)
    stop_words = stopwords.words(lang)
    cleaned = []
    for token in tokens:
        if not token in stop_words:
            cleaned.append(token)
    return cleaned
    
print(clean_stopwords(text1, "english"))
print(clean_stopwords(text2, "spanish"))

