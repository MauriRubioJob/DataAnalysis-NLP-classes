import requests
import csv

url = 'https://python.techtalents.cloud/imdb.csv'

respuesta = requests.get(url)

if respuesta.status_code == 200:
	contenido = respuesta.text
else:
	print("Ha habido un problema conectando")

# print(contenido)

lineas = contenido.splitlines()

lista_csv = list(csv.reader(lineas))
print(type(lista_csv))

for elemento in lista_csv:
	print(elemento)
	input()

