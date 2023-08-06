# Vamos a hacer un ejercicio que se encarga de 
# procesar un conjunto de datos del corpus de nltk.
'''
Vamos a coger de nltk.corpus un conjunto de datos que contienen
una serie de tweets, que vamos a aplicarles los pasos del procesado
para posteriormente, tras hacer el último paso de normalización,
comparar las palabras con una lista de emociones y así poder detectar
las emociones/sentimientos que hay en los tweets

'''

# SECCIÓN DE IMPORTACIÓN DE MÓDULOS
from nltk.corpus import twitter_samples, stopwords, wordnet
from nltk import word_tokenize, FreqDist

from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer

import json

from collections import Counter
import matplotlib.pyplot as plt

# Lo primero cargar la información
# print(twitter_samples.fileids())

# Cargamos contenido
tweets = twitter_samples.strings("tweets.20150430-223406.json")
eng_stopwords = stopwords.words("english")

lematizador = WordNetLemmatizer()

archivo = open("emotions.json","r")
contenido = archivo.read()
archivo.close()

dic_emociones = json.loads(contenido)


# print("Tweet feote:")
# print(tweets[315])


# SECCIÓN DE FUNCIONES:

# PASO 1) Limpieza de los tweets
# Quiero eliminar lo siguiente: "RT" , "@..." , "enlaces" , "..." , "…"
def limpieza_tweet ( tweet ):
    palabras = tweet.split()
    limpias = []
    for palabra in palabras:
        if palabra.startswith("RT"):
            # descartamos la palabra y no la introducimos en nuestra lista de "limpias"
            continue
        elif palabra.startswith("@"):
            continue
        elif palabra.startswith("#"):
            continue
        elif palabra.startswith("http"):
            continue
        elif palabra.startswith("…"):
            continue
        else:
            limpias.append(palabra)
    # Una vez acabado el bucle for, uno todos los elementos de mi lista "limpias"
    tweet_lim = " ".join(limpias)
    return tweet_lim

# PASO 2) Tokenizar el texto/oracion/tweet
def tokenizador ( tweet_lim ):
    token = word_tokenize( tweet_lim )
    return token

# PASO 2.1) Limpiar los tokens para eliminar las stopwords. Las stopwords son palabras que python no necesita
# por lo que vamos a limpiarlas
def limpiador_tokens ( tokens ):
    cleaned_tokens = []
    for token in tokens:
        if token.lower() in eng_stopwords:
            continue
        else:
            cleaned_tokens.append(token)
    
    return cleaned_tokens


# PASO 3-4 ) Vamos a crear una función que me etiquete los tokens limpios del tweet (PASO 3) TAGGING )
# Para posteriormente en base al etiquetado realizado podamos hacer el PASO 4) Lematizar las palabras

def etiquetar_lematizar( clean_tokens ):
    # PASO 3) Etiquetar estos tokens
    etiquetas = pos_tag( clean_tokens )

    tokens_lematizados = []
    # input()
    # Voy a recorrer cada token etiqueta, para poder lematizarlo.
    for etiqueta in etiquetas:
        token = etiqueta[0]
        tag = etiqueta[1]
        # Dependiendo de la tag, el token lo lematizamos de una forma u otra
        # print("El token" , token , "está etiquetado gramaticalemnte como",tag)

        # Para lematizar cuando trabajemos con palabras contextualizadas gramaticalmente:
        # Si la tag empieza por VB -> Verbos -> wordnet.VERB
        # Si la tag empieza por NN -> Sustantivos (NOUN) -> wordnet.NOUN
        # Si la tag empieza por RB -> Adverbios -> wordnet.ADV
        # Si la tag empieza por JJ -> Adjetivos -> wordnet.ADJ
        if tag.startswith("VB"):
            raiz_token = lematizador.lemmatize(token, wordnet.VERB)
        elif tag.startswith("NN"):
            raiz_token = lematizador.lemmatize(token, wordnet.NOUN)
        elif tag.startswith("RB"):
            raiz_token = lematizador.lemmatize(token, wordnet.ADV)
        else:
            raiz_token = lematizador.lemmatize(token, wordnet.ADJ)

        tokens_lematizados.append(raiz_token)
        # print("Mi token",token,"está lematizado como" , raiz_token)
    return tokens_lematizados


# SECCION PROGRAMA PRINCIPAL:

# Voy a crear una lista de las palabras que ya están completamente procesadas y lematizadas

lista_palabras = []

for tweet in tweets:

    tweet_limpio = limpieza_tweet ( tweet )

    tokens = tokenizador( tweet_limpio )

    tokens_limpios = limpiador_tokens( tokens )

    lista_palabras.extend( etiquetar_lematizar( tokens_limpios ) )


lista_emociones = []
for palabra in lista_palabras:
    # Voy a guardar la palabra demla lista palabras, únicamente si es palabra
    # se encuentra dentro de mi diccionario de emociones
    if palabra.lower() in dic_emociones:
        lista_emociones.append(palabra)

# print(lista_emociones)

lista_emociones_genericas = []

for emocion in lista_emociones:
    emocion_generica = dic_emociones[emocion.lower()]
    lista_emociones_genericas.append ( emocion_generica )

print(lista_emociones_genericas)

# frequencies = FreqDist ( lista_emociones_genericas )
# frequencies.plot(cumulative=False)

counted = Counter( lista_emociones_genericas )

figure, axis = plt.subplots()
axis.bar(counted.keys(), counted.values())
figure.autofmt_xdate()

plt.show()
