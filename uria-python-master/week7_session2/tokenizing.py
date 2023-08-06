from nltk import tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag


my_string = "Welcome to the program! Hope you enjoy your stay Mr. Bob! Do you need anything, can I get you anything?"


tokenized = tokenize.word_tokenize(my_string)

eng_stopwords = stopwords.words("english")


important_tokens = []
for word in tokenized:
    if not word in eng_stopwords:
        important_tokens.append(word)

tagged = pos_tag(important_tokens)

print(tagged)
