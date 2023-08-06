# La idea de hoy es comenzar a trabajar con el módulo SPACY.
# Este módulo nos va a permitir procesar un texto/oración en español.

# Spacy es un módulo que a diferencia de nltk, no tiene submódulos y todas sus funciones están
# en la raíz del módulo
import spacy
from nltk.corpus import stopwords

oracion = "pequeñito Python es un lenguaje de malísimo programación multiparadigma. Esto significa que más que forzar a los programadores a adoptar un estilo particular de programación, permite variosestilos: programación orientada a objetos, programación imperativa y programación funcional. Otros paradigmas están soportados mediante el uso de extensiones."
es_stopwords = stopwords.words("spanish")

# print(es_stopwords)

es_parser = spacy.load("es_core_news_md")

# El es_parser es la función que se encarga de procesar la oración, sabiendo
# que el lenguaje es el español. Spacy los 4 pasos (cleaning, tokenization, tagging, normaliz)
# me loos hace todos a la vez, del tirón, con sólo 1 función
procesado = es_parser ( oracion )

# Dentro de procesado, ya están los tokens, palabras tageadas, palabras lematizadas...
print(procesado)

# elementos_filtrados = []

# for elemento in procesado:
#     palabra = elemento.text
#     if palabra.lower() not in es_stopwords:
#         elementos_filtrados.append( elemento )

#     # print("El texto del token es: ", elemento.text)
#     # print("La etiqueta gramatical del token es: ", elemento.pos_)
#     # print("El lemma del token es:",elemento. )
#     # input()

# for elemento in elementos_filtrados:
#     print(elemento.text)
    


