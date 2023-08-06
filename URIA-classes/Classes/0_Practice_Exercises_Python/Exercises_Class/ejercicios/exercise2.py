# Cleaning I:
# Using punctuation from string... do the cleaning proccess of taking out all the punctuation in the 
# text given after tokenizing it:


from string import punctuation
from nltk import word_tokenize


text = "Critics of zoos would argue that animals often suffer physically and mentally by being enclosed. Even the best artificial environments can't come close to matching the space, diversity, and freedom that animals have in their natural habitats. This deprivation causes many zoo animals to become stressed or mentally ill. Capturing animals in the wild also causes much suffering by splitting up families. How could we mend this terrible situation? We have to help!"

# print( list( punctuation ) )

# Forma 1: guardando en una nueva lista los caratceres que pasen nuestro filtro:
# 1) Tokenizo mi texto y elimino los tokens que sean signos de puntuación

tokens = word_tokenize(text)
print(tokens)
input()
cleaned = []
for token in tokens:
    if token not in punctuation:
        
        cleaned.append(token)
print(cleaned)

# Froma 2: Utilizando replace.
# for char in text:
#     if char in punctuation:
#         text = text.replace(char,"")
# print(text)