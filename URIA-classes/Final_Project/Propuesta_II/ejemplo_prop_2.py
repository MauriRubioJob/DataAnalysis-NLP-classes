'''
Planteamiento del proyecto:

Solciitar al usuario si quiere buscar info de una empresa o persona.

    Camino 1: Empresa

    Solicitar al usuario la palabra(s) clave.

    Conformar la URL para obtener info de TODAS las empresas con ese nombre

    Si hay empresas con ese nombre

        Listar todas esas empresas de la página 1, o todas las páginas

        Solicitar al usuario qué empresa quiere consultar

        Obtener el slug de esa empresa

        Conforma la URL para obtener la info de esa empresa concreta

        Extraer la información en base a lo recibido tras la comunicación web.
    
    Camino 1: Empresa

    Solicitar al usuario la palabra(s) clave.

    Conformar la URL para obtener info de TODAS las empresas con ese nombre

    Si hay empresas con ese nombre

        Listar todas esas empresas de la página 1, o todas las páginas

        Solicitar al usuario qué empresa quiere consultar

        Obtener el slug de esa empresa

        Conforma la URL para obtener la info de esa empresa concreta

        Extraer la información en base a lo recibido tras la comunicación web.

    Camino 2: persona

    Solicitar al usuario la palabra(s) clave.

    Conformar la URL para obtener info de TODAS las personas con ese nombre

    Si hay personas con ese nombre

        Listar todas esas personas de la página 1, o todas las páginas

        Solicitar al usuario qué persona quiere consultar

        Obtener el slug de esa persona

        Conforma la URL para obtener la info de esa persona concreta

        Extraer la información en base a lo recibido tras la comunicación web.

'''
# .......

# Buscando una empresa...

import requests
import json

palabra_buscar = "pantalla"

url = "https://libreborme.net/borme/api/v1/empresa/search/?q=xxx&page=1"


url = url.replace( "xxx" , palabra_buscar )

respuesta = requests.get ( url )

if respuesta.status_code == 200:
    conversion = json.loads(respuesta.text)


# print(type(conversion["objects"]))

empresa_de_interes = conversion["objects"][6]

# print(type(empresa_de_interes))

# print("El slug de la empresa" , empresa_de_interes["name"], "es" , empresa_de_interes["slug"])


url = "https://libreborme.net/borme/api/v1/empresa/xxx-xxx-xxx"

url = url.replace("xxx-xxx-xxx" , empresa_de_interes["slug"])

respuesta = requests.get ( url )

if respuesta.status_code == 200:
    info_empresa_interes = json.loads(respuesta.text)

print(type(info_empresa_interes))

lista_cargos_historial = info_empresa_interes["cargos_historial_p"]

archivo = open( "informacion.txt", "w" )
archivo.write ("cargo,empresa\n")
for cargo in lista_cargos_historial:
    archivo.write(cargo["name"]+","+info_empresa_interes["name"]+"\n")


archivo.close()
