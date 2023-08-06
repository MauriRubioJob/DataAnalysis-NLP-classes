# Cleaning II:

# Create a function that removes the stopwords of a text. The function must receive as arguments the text and the language, and return the cleaned text.



text1 = '''Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.'''

text2 = '''Python tuvo un papel crucial en este proceso: debido a su orientación hacia una sintaxis 
limpia, ya era idóneo, y las metas de CP4E presentaban similitudes con su predecesor.'''

from nltk.corpus import stopwords
from nltk import word_tokenize

eng_stopwords = stopwords.words("english")
es_stopwords = stopwords.words("spanish")

def eliminar_stopwords ( texto , sw , lg ):
    # 1) tokenizar el texto
    tokens = word_tokenize ( texto , language = lg )

    # 2) limpiar los tokens de stopwords
    cleaned = []
    for token in tokens:
        if token.lower() not in sw:
            cleaned.append(token)
    
    return cleaned

# Para el texto 1 que está en inglés:
cleaned_tokens1 = eliminar_stopwords ( text1 , eng_stopwords , "english")

# PAra el texto 2 que está en español:
cleaned_tokens2 = eliminar_stopwords (text2 , es_stopwords , "spanish")

print("Texto en inglés sin stopwords: ")
print(cleaned_tokens1)

print("Texto en español sin stopwords: ")
print(cleaned_tokens2)


