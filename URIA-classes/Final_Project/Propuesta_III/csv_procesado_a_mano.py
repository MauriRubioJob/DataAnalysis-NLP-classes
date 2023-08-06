import requests

def procesar_csv ( url_csv ):

	respuesta = requests.get( url_csv )

	if respuesta.status_code == 200:
		contenido = respuesta.text
	else:
		print("conexión fallida :(")



	filas = contenido.splitlines()
    
	separacion_propiedades = filas[0].split(",")

	longitud_permitida = len(separacion_propiedades)

	dic_csv = {}

	for prop in separacion_propiedades:
		dic_csv[prop] = []
	filas.pop(0)

	for fila in filas:
		separacion = fila.split(",")
		index = 0

		if (len(separacion) == longitud_permitida):
			for key in dic_csv:
				dic_csv[key].append(separacion[index])
				index += 1

	return dic_csv




url = "https://python.techtalents.cloud/imdb.csv"

IMDB_proc = procesar_csv( url )


for i in range( len(IMDB_proc["color"]) ):
	# Imprimir todas las películas del director "George Lucas"
	lista_generos = IMDB_proc["genres"][i].split("|")

	if "Adventure" in lista_generos and int (IMDB_proc["movie_facebook_likes"][i]) > 50000:
		print("La pelicula es: "+IMDB_proc["movie_title"][i])