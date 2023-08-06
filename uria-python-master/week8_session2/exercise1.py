# Write a Python NLTK program to tokenize sentences in languages other than English.
# TIP: word_tokenize accepts 2 arguments, the text to tokenize and the language.

from nltk.tokenize import word_tokenize, sent_tokenize


text1 = '''
NLTK ist Open Source Software. Der Quellcode wird unter den Bedingungen der Apache License Version 2.0 vertrieben.  
Die Dokumentation wird unter den Bedingungen der Creative Commons-Lizenz Namensnennung - Nicht kommerziell - Keine 
abgeleiteten Werke 3.0 in den Vereinigten Staaten verteilt.
'''

de_tokens = word_tokenize(text1, language="german")
de_sent_tokens = sent_tokenize(text1, language="german")
print(de_tokens)
print(de_sent_tokens)

text2 = '''
Durante su estancia en CNRI, van Rossum lanzó la iniciativa Computer Programming for 
Everybody (CP4E), con el fin de hacer la programación más accesible a más gente, 
con un nivel de 'alfabetización' básico en lenguajes de programación, similar a la 
alfabetización básica en inglés y habilidades matemáticas necesarias por muchos trabajadores. 
Python tuvo un papel crucial en este proceso: debido a su orientación hacia una sintaxis 
limpia, ya era idóneo, y las metas de CP4E presentaban similitudes con su predecesor, ABC.
'''

es_tokens = sent_tokenize(text2, language="spanish")
print(es_tokens)
