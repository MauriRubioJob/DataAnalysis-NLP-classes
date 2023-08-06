# '''
# 0) Dejamos repl, ejecutaba cosas en sus servers y ahora lo hacemos todo en local
# 1) Instalar python, VSCode, asegurarme de que todos lo tienen
# 2) Extensiones: python, temas: ponerle el mismo que el mío si quieren highlighted igual
# 3) consola comandos, controlar pc a través del teclado
# 4.0) windows: pip
# 4.1) MAC/Linux: pip3
# 4.2) windows: python -m pip
# 4.3) MAC/LINUX: python3 -m pip3

# if neither works, in VSCode, do the following:


# 5) installing nltk:  
# 5.1) windows: pip install --user nltk
# 5.2) MAC/L:  pip3 install --user nltk
# 5.3) windows: python -m pip install --user nltk
# 5.4) MAC/L:   python3 -m pip install --user nltk

# 6) In terminal: python, and now we are in python command
# 7) import nltk, and it must not give us an error
# 8) nltk.download
# 9) interfaz, clickar en "book" y download



# # MAC  ISSUES: 
# 1) temrinal -> terminal after opening a python file
# 2) run the file
# 3) arrow arriba
# 4) delete the string
# 5) python -m pip install --user nltk


# ###### COMENZANDO NLP ######

# 1) Ya tenemos todas las herramientas para poder trabajar con nlp
# 2) 2000+ -> código que hace spell checking
# 3) cosas....
# 4) Hoy en inglés en principio, y otro día en español. programación es la misma.
# 5) 13 -> las reglas van cambiando, el proceso de procesado, hoy  nos saltamos "cleaning"
#     tagging le da sentido a las palabras para que python las entienda y las pueda comprender para relacionarlas
#     GRAMÁTICA
# 6) explicar niveles de abstracción de comprensión en programación
# 7) tokenization -> splitting parecido.
# 8) la vida no es tan bonita... no recibimos las cosas tan mascaitas
# 9) 21 -> dividr en lineas. Buscar un patrón para separar entre oraciones programar esto.
# 10) NLTK pa eso está. Yahemos hecho procesados un poco por encima, no perfectos y tenemos módulos a nuestra disposición. Los usamos. COLABORATIVO.

# 11) En mi programa, escribir una oración chunga, importar tokenize y usar:
# 12) Tokenizar palabras: word_tokenize
# 13) Tokenizar oraciones: sent_tokenize
# 14) from nltk.corpus import stopwords
# 15) eng_stopwords = stopwords.words("english")
# 16) sp_stopwords = stopwords.words("spanish")

# corpora -> twiiter samples

# '''

from nltk import tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

import nltk.tag


# oracion = "Hola, me llamo sr. Mauri. Soy de Ponia! ¿Quieres algo de comer?"
oracion  = "Hello, there my name is mauri I am going to wolves in a car"

#  tokenize

tokenized = tokenize.word_tokenize(oracion, language="english")

print(tokenized)

# clean 

# sp_stopwords = stopwords.words("spanish")

# print(sp_stopwords)

# important_tokens = []

# for word in tokenized:
#     if word not in sp_stopwords:
#         important_tokens.append(word)

# tagged = pos_tag(important_tokens,tagset="universal")

words = ["give","giving","having","gave","wolf","wolves","ponies","pony"]
for word in words:

    # stemmed = LancasterStemmer().stem(word)
    lema = wordnet.WordNetLemmatizer().lemmatize(word,"n")
    print(word,":",lema)

# words = ["give","giving","having","gave"]
# for word in words:
#     stemmed = PorterStemmer().stem(word)
#     print(word,":",stemmed)

# print(stemmed)



# import es_core_news_sm
# nlp = es_core_news_sm.load()
# doc = nlp("El copal se usa principalmente para sahumar en distintas ocasiones como lo son las fiestas religiosas.")
# print([(w.text, w.pos_) for w in doc])