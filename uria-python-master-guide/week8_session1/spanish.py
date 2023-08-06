import spacy
from nltk.corpus import stopwords


es_parser = spacy.load("es_core_news_md")
es_stopwords = stopwords.words("spanish")


oracion = "Python es un lenguaje de programación multiparadigma. Esto significa que más que forzar a los programadores a adoptar un estilo particular de programación, permite varios estilos: programación orientada a objetos, programación imperativa y programación funcional. Otros paradigmas están soportados mediante el uso de extensiones."

parsed = es_parser(oracion)

cleaned_words = []
for token in parsed:
    if not token.text in es_stopwords:
        cleaned_words.append(token.text)
