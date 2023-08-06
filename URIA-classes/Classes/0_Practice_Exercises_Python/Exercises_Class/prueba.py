from nltk.corpus import gutenberg,machado,movie_reviews

# print( gutenberg.fileids() )
# print( machado.fileids() )
# print( movie_reviews.fileids() )

 
contenido = machado.words("teatro/matt02.txt")
emma = gutenberg.words('austen-emma.txt')
print(emma.words)


