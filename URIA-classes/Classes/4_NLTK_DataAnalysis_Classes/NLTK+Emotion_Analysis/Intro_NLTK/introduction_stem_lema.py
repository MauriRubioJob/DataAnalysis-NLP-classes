# stemming es una herramienta que me permite cortar la temrinación de una palabra
# para quedarme unicamente con la raíz de la palabra, que es la que tiene valor para python

# nltk -> stem -> PorteStemmer para coger las funciones que yo necesito
from nltk.stem import PorterStemmer 

from nltk.stem import LancasterStemmer


lista_verbos = [ "give" , "gave" , "giving" , "given" ]

for palabra in lista_verbos:

    # raiz = PorterStemmer().stem( palabra )
    raiz = LancasterStemmer().stem( palabra )

    print( "La raiz de la palabra" , palabra, "es", raiz )

# Lematization es básicamente lo mismo, pero me da la raíz de la palabra en función del contexto
# de la oración.

