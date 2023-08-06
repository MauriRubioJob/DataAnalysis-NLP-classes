'''

1) Installing spaCy:   https://github.com/tt-n-walters/uria-python/tree/master/week8_session1

2) import spacy. Todas las funciones están ahí metidas, más cómmodas

3) es_paser. Spacy te hace los 4 primeros pasos todos del tirón.  
            es_parser = spacy.load("es_core_news_md")

4) Poner oración en español para añalizarla:  
"Python es un lenguaje de programación multiparadigma. 
Esto significa que más que forzar a los programadores a 
adoptar un estilo particular de programación, permite varios
estilos: programación orientada a objetos, programación imperativa y 
programación funcional. Otros paradigmas están soportados mediante el uso de extensiones. "

5) parsed = es_parser(oracion)

6) for loop, and print tpken and token's parto of speech

7) lematizador no funciona muy muy muy bien. Solo hay lematizador y no stemmer

8) El objetivo final es juntar spacy y nltk. stopwords de nltk para limpiar.

9) from nltk.corpus import stopword ;   es_stopwords = stopwords.words("spanish")

10) dentro del for loop:    if not token.text in es_stopwords:
                                clean.append(token.text)


/Applications/Python\ 3.8/Install\ Certificates.command
cd /Applications
./"Install Certificates.command"

'''


# import spacy

# es_parser = spacy.load("es_core_news_md")

# oracion = "Python es un lenguaje de programación multiparadigma. Esto significa que más que forzar a los programadores a adoptar un estilo particular de programación, permite variosestilos: programación orientada a objetos, programación imperativa y programación funcional. Otros paradigmas están soportados mediante el uso de extensiones. "

# parsed = es_parser(oracion)

# print(parsed)

# for token in parsed:
#     print(token , token.pos_) 


# import os
# arr = os.listdir('.')
# print(arr)

