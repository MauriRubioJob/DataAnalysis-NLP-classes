# Execute the basic cleaning, tokenization, tagging and lematization of all the words in 
# the jane auston's emma text that's located in the nltk corpus, and extract the informations 
# of the emotions expressed in the text as it's been done with the tweets in class.

from nltk.corpus import gutenberg, stopwords, wordnet
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist

import json


emmaAusten = gutenberg.words("austen-emma.txt")
eng_stopwords = stopwords.words("english")
lematizador = WordNetLemmatizer()

# Texto ya tokenizado

# for element in emmaAusten:
#     print(element)
#     input()

# 1) limpiamos el texto de emmaAusten quitando las stopwords
tokens_limpios = []
for token in emmaAusten:
    if token.lower() not in eng_stopwords:
        tokens_limpios.append(token)

# 2) Etiquetamos los tokens limpios:
etiquetas = pos_tag(tokens_limpios)

# 3) lematizamos los tokens que ya están etiquetados
palabras_lematizadas = []

for etiqueta in etiquetas:
    if etiqueta[1].startswith("NN"):
        raiz_token = lematizador.lemmatize( etiqueta[0] , wordnet.NOUN )
    elif etiqueta[1].startswith("VB"):
        raiz_token = lematizador.lemmatize( etiqueta[0] , wordnet.VERB )
    elif etiqueta[1].startswith("RB"):
        raiz_token = lematizador.lemmatize( etiqueta[0] , wordnet.ADV )
    else:
        raiz_token = lematizador.lemmatize( etiqueta[0] , wordnet.ADJ )
    
    palabras_lematizadas.append(raiz_token)

# 4) Con las palabras ya normalizadas, recorremos

archivo = open("emotions.json","r")
contenido = archivo.read()
archivo.close()

dic_emociones = json.loads(contenido)

lista_emociones = []
for palabra in palabras_lematizadas:
    if palabra.lower() in dic_emociones:
        lista_emociones.append(dic_emociones[palabra.lower()])


frequencies = FreqDist ( lista_emociones )
frequencies.plot(cumulative=False)