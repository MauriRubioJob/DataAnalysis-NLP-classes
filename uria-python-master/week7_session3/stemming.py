from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer


stemmer = LancasterStemmer()

print(stemmer.stem("run"))
print(stemmer.stem("running"))

print(stemmer.stem("wolf"))
print(stemmer.stem("wolves"))

print(stemmer.stem("knife"))
print(stemmer.stem("knives"))

print(stemmer.stem("pony"))
print(stemmer.stem("ponies"))
