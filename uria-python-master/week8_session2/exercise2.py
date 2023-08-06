# Cleaning I:
# Using punctuation from string... do the cleaning proccess of taking out all the punctuation in the text given after tokenizing it:


from string import punctuation
from nltk.tokenize import word_tokenize

text = "Critics;: of zoos would argue that animals often suffer physically and mentally by being enclosed. Even the best artificial environments can't come close to matching the space, diversity, and freedom that animals have in their natural habitats. This deprivation causes many zoo animals to become stressed or mentally ill. Capturing animals in the wild also causes much suffering by splitting up families. How could we mend this terrible situation? We have to help!"

tokens = word_tokenize(text)

cleaned_tokens = []
for token in tokens:
    if not token in punctuation:
        cleaned_tokens.append(token)

print(cleaned_tokens)


for token in tokens:
    if token in punctuation:
        tokens.remove(token)

print(tokens)