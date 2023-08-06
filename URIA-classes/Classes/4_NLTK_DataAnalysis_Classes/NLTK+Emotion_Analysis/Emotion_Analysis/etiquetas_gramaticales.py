# Vamos a ver el proceso 3) TAGGING
'''
Tagging consiste en etiquetar, en contextualizar gramaticalmente cada palabra
del texto/oración con el que el usuario esté trabajando.

Para poder hacerle el tagging a una serie de palabras, debemos primero tokenizar (hacer el paso 2) ) 
el texto/oración con el que estemos trabajando.

'''

# 1) ejecutar el paso 2 -> Tokenizar

from nltk import word_tokenize
from nltk.tag import pos_tag

from nltk.corpus import stopwords

oracion = "Welcome to the program! Hope you enjoy your stay Mr. Bob! Do you need anything, can I get you anything?"

tokens = word_tokenize(oracion)

print(tokens)

# Una vez hemos tokenizado la oración vamos a etiquetar cada una de los tokens

etiquetado = pos_tag( tokens )

print(etiquetado)

# Pequeño vistazo a cleaning. Vamos a ver lo que son las stopwords
eng_stopwords = stopwords.words("english")
print("Palabras en inglés que a python no le sirven para nada con NLTK")
print(eng_stopwords)

sp_stopwords = stopwords.words("spanish")
print("Palabras en español que a python no le sirven para nada con NLTK")
print(sp_stopwords)


