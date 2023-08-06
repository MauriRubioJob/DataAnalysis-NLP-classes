# Lematizing I
# Write a python function that receives a word and its gramatical purpose in the context of the text from which it comes and returns you the lematized word.

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lematizador = WordNetLemmatizer()

tokens = ['Here', 'you', 'can', 'find', 'activities', 'to', 'practise', 'your', 'reading', 'skills','.', 'Reading', 'will', 'help', 'you', 'to', 'improve', 'your', 'understanding', 'of', 'the', 'language', 'and', 'build', 'your', 'vocabulary', '.']
gramatical_purpose = ['RB', 'PRP', 'MD', 'VB', 'NNS', 'TO', 'VB', 'PRP$', 'NN', 'NNS', '.', 'NNP','MD', 'VB', 'PRP', 'TO', 'VB', 'PRP$', 'NN', 'IN', 'DT', 'NN', 'CC', 'VB', 'PRP$', 'NN', '.']

print( len(tokens) )
print(len(gramatical_purpose))

raices_tokens = []
for i in range( len(tokens) ):
    # print(tokens[i])
    # print(gramatical_purpose[i])

    # Si empiza por "NN" es un sustantivo -> lo lematizamos como wordnet.NOUN
    if gramatical_purpose[i].startswith("NN"):
        token_lematizado = lematizador.lemmatize(tokens[i] , wordnet.NOUN)
    elif gramatical_purpose[i].startswith("VB"):
        token_lematizado = lematizador.lemmatize(tokens[i] , wordnet.VERB)
    elif gramatical_purpose[i].startswith("RB"):
        token_lematizado = lematizador.lemmatize(tokens[i] , wordnet.ADV)
    else:
        token_lematizado = lematizador.lemmatize(tokens[i] , wordnet.ADJ)
    
    raices_tokens.append(token_lematizado)

print(raices_tokens)
