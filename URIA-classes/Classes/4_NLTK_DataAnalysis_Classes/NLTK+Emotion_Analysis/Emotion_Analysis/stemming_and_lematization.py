# Paso 4 NORMALIZACIÓN.
'''
Este paso se encarga de obtener la raíz de una palabra, que es lo que a python le importa.
Para obtener la raíz de una palabra tenemos 2 herramientas:

    - stemming: Más brusco, tiene menos finura, pero es menos costoso computacionalmente de ejecutar.
        El proceso de ejecutar stemming gasta menos ennergia, porque hace menos procesos
    
    - Lematización: Te da la raíz de la palabra en función de cómo esa palabra se comporta gramaticalmente 
        en el contexto de mi oración/texto

'''

# Importar los stemmers para obtener la raíz de la palabra con la herramienta stem
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
# 

# stemmer = PorterStemmer()
# stemmer = LancasterStemmer()
stemmer = SnowballStemmer(language="english")

print("Utilizando el proceso de stemming")
print( stemmer.stem("having") )
print( stemmer.stem("had") )
print( stemmer.stem("giving") )
print( stemmer.stem("gave") )

print("\n")

lematizador = WordNetLemmatizer()

# Para lematizar cuando trabajemos con palabras contextualizadas gramaticalmente:
# Verbos -> wordnet.VERB
# Sustantivos (NOUN) -> wordnet.NOUN
# Adverbios -> wordnet.ADV
# Adjetivos -> wordnet.ADJ

print("Utilizando el proceso de lematización")
print( lematizador.lemmatize("having" , wordnet.VERB ) )
print( lematizador.lemmatize("bad" , wordnet.ADJ ) )
print( lematizador.lemmatize("worse" , wordnet.ADJ ) )

