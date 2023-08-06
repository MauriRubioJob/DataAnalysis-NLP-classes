# tag the following text in spanish both using nltk pos_tag universal language and spacy module, and spot the differences.

import spacy

from nltk.tag import pos_tag
from nltk import word_tokenize

texto = '''Python tuvo un papel crucial en este proceso: debido a su orientación hacia una sintaxis 
limpia, ya era idóneo, y las metas de CP4E presentaban similitudes con su predecesor.'''

# Obtención de las TAGS con spacy

es_parser = spacy.load("es_core_news_md")

parsed = es_parser( texto )

tags_spacy = []

for elemento in parsed:
    token = elemento.text
    tag = elemento.pos_
    tags_spacy.append([token,tag])


print("Tag con spacy: ")
print(tags_spacy)

# Obteción de las TAGS con NLTK pos_tag tagset = "universal"

tokens = word_tokenize(texto,"spanish")
tags_nltk = pos_tag( tokens, tagset = "universal")

print("Tags con universal: ")
print(tags_nltk)
