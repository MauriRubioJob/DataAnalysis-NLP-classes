'''
0) Comprobar si MAC funciona ya.

1) Si no se han descargado todo -> descargar:
        Corpora/Framenet_v17
        Models/porter_test
        Models/vader_lexicon

2) Terminar los del otro día: repasar tokenization, tagging and removing shit:

2.1) Tagging: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    https://github.com/tt-n-walters/uria-python/blob/master/week7_session3/piece_of_speach_tags.md

2.2) Stopwords:
    eng_stopwords = stopwords.words("english")
    sp_stopwords = stopwords.words("spanish")

Eliminar las stopwords

2.3) Corpus es una colección de texto, discurso conjuntos de textos relacionados para poder trabajar con ellos.
Vamos a trabajar hoy con twitter samples.

3) Normalization -> stemming and lematization verlo bien en profundidad. Nos permite obtener la raíz e ignorar el tiempo 
verbal en el que está presentado, obtniendo solo la importancia de la acción.

4) Stem no siempre es perfecto pero es rápido, cómodo y ayudan internamente a NLP, aunque pa un humano no tenga sentido
el corte que hace para nosotros, para el ordenador sí tiene sentido.
    1) repasar stem con PorterStemmer, LancasterStemmer, SnowballStemmer

    2) Lematization siempre da una palabra REAL y te normaliza todo muy cómodo y muy bien, pero es más costoso.
    Debe saber si es: Noun, Verb, Adjective, Adverb. from nltk.corpus import wordnet
    verb -> wordnet.VERB
    noun -> wordnet.NOUN
    adjective -> wordnet.ADJ  ¡¡¡¡(bad, worse)!!!!
    adverb -> wordnet.ADV

    2.1) wordnet es una base de datos con un montón de palabras relacionadas entre ellas para poder realizar las relaciones
    verbales, adjetivales y obtener siempre la raíz correcta. Proceso más costoso, largo...

5) Gonna use TAGGING to our advantage para crear el contexto gramatical de la palabra y poder lematizarla

6) Con los 4 primeros pasos ya entendidos, vamos a hacer el ejemplo de twitter

7) Twitter_samples import it from corpus;   print(twitter_samples.fileids())

8) Una vez tenemos los tweets, vamos a reducir cuántos utilizamos y vamos a hacer un poquito de limpieza de cosas que no aportan
como por ejemplo los LINKS, los @, eliminar los ... … , RT, replace los hashtags. Más limpieza -> mejor resultado

9) tokenize function

10) clean tokens. -> stopwords and puntuation rmeoving.  from string import punctuation

11) Queremos lematizar para que haga bien la detección de sentimientos -> Debemos hacer los de las tags.
from nltk.tag import pos_tag

12) Queremos lematizar -> 2 import
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
palabra que no se pueda lematizar -> pasamos de ellas. o le decimos que es un adjetivo paraque no se ralle mucho.

13) import emotions and check if each token is an emotion, and count them

14) from nltk import freqDist

15) plot the graphic

'''
