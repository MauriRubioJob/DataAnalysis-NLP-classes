# Given the following text, tokenize it, clean the stopwords, tag it and lematize it.

from nltk import word_tokenize
from nltk.corpus import stopwords , wordnet
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer


text = "Critics of zoos would argue that animals often suffer physically and mentally by being enclosed. Even the best artificial environments can't come close to matching the space, diversity, and freedom that animals have in their natural habitats. This deprivation causes many zoo animals to become stressed or mentally ill. Capturing animals in the wild also causes much suffering by splitting up families. Some zoos make animals behave unnaturally: for example, marine parks often force dolphins and whales to perform tricks. These mammals may die decades earlier than their wild relatives, and some even try to commit suicide."

eng_stopword = stopwords.words("english")
lematizador = WordNetLemmatizer()

# Paso 1) Tokenizar
tokens = word_tokenize ( text )

# Paso 2) Limpiar tokens de stopwords
tokens_limpios = []

for token in tokens:
    if token.lower() not in eng_stopword:
        tokens_limpios.append(token)

    
# Paso 3) Etiquetar

tags = pos_tag ( tokens_limpios )

# Paso 4) Lematizar
palabras_lematizadas = []

for tag in tags:
    # print(tag)
    # input()
    if tag[1].startswith("NN"):
        raiz_token = lematizador.lemmatize( tag[0] , wordnet.NOUN )
    elif tag[1].startswith("VB"):
        raiz_token = lematizador.lemmatize( tag[0] , wordnet.VERB )
    elif tag[1].startswith("RB"):
        raiz_token = lematizador.lemmatize( tag[0] , wordnet.ADV )
    else:
        raiz_token = lematizador.lemmatize( tag[0] , wordnet.ADJ )
    
    palabras_lematizadas.append(raiz_token)

# Paso 5) Imprimir los tokens lematizados
print(palabras_lematizadas)


