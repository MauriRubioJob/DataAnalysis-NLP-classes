# Over the internet you must get the text associate to the proccess of consulting the following page:
# url = 'https://en.wikipedia.org/robots.txt'
# After that, the text received must be splitted into lines and print the 36th line:

import requests

url ='https://en.wikipedia.org/robots.txt'

respuesta = requests.get(url)

texto = respuesta.text
lineas = texto.split("\n")
print(lineas[35])