# The corpus of nltk offers us a huge collection of data. Some of that data are famous writers text. the following program imports different collections and shows you how to consult the file you want.

from nltk.corpus import gutenberg, machado, movie_reviews

print(gutenberg.fileids())
# print(machado.fileids())
# print( movie_reviews.fileids() )


# machado_teatro2 = machado.words("teatro/matt02.txt")
# print(len(machado_teatro2))


# Check the length of austen-emma text that's inside gutenberg's corpora.
emma = gutenberg.raw("austen-emma.txt")
print(len(emma))

emma_words = gutenberg.words("austen-emma.txt")
print(len(emma_words))

emma_sents = gutenberg.sents("austen-emma.txt")
print(len(emma_sents))
