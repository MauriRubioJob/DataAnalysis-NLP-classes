from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()

# Contexts are
# wordnet.ADJ
# wordnet.ADV
# wordnet.VERB
# wordnet.NOUN

# Lemmatize a word, with given context
print(lemmatizer.lemmatize("run", wordnet.VERB))
print(lemmatizer.lemmatize("running", wordnet.VERB))

print(lemmatizer.lemmatize("knife"))
print(lemmatizer.lemmatize("knives"))

print(lemmatizer.lemmatize("bad", wordnet.ADJ))
print(lemmatizer.lemmatize("worse", wordnet.ADJ))
