'''
Proyecto consulta de las API del BORME.

Tenemos 1 dirección web en la que podemos incluir el nombre de la empresas que buscamos y que tenga dicha palabra
en su denominación

Tenemos otra dirección web en la que vamos a poner el "slug" de la empresa de la que queremos obtener su información.

PLANTEAMIENTO en python:

1) Necesitamos hacer consultas web -> requests

2) Necesitamos pedir al usuario la palabra que busca, y con esa palabra conformar la URL

3) La información en la web está en formato JSON, hay que convertirla -> import json

4) Permitir al usuario elegir de qué empresa consultar los datos

5) con el slug de la empresa elegida, conformar la 2ª URL y obtener la información de la empresa.

6) Consultamos la información que queramos de la empresa en cuestión

'''

# SECCIÓN IMPORTACIÓN DE MÓDULOS
import requests 
import json


# SECCIÓN DE FUNCIONES:

# Función 1: Obtener información de empresas cuyo nombre tenga la palabra que pida el usuario
def obtenerEmpresas ( busqueda ):
    urlEmpresas = "https://librebor.me/borme/api/v1/empresa/search/?q=xxx&page=1"
    urlEmpresas = urlEmpresas.replace( "xxx" , busqueda )

    respuesta = requests.get(urlEmpresas)

    if respuesta.status_code == 200:
        print("conexión satisfactoria")
        empresasListadas = json.loads( respuesta.text )
        return empresasListadas
    else:
        print("La conexión no ha salido bien :( ")


# Función 2: Listar todas las empresas que incluyan esa palabra en su nombre:
def mostrarEmpresas ( empresasListadas ):
    for i in range( len(empresasListadas["objects"]) ):
        print ( i, ": ", empresasListadas["objects"][i]["name"] )


# Función 3: En base a la elección del usuario, buscar información de la empresa concreta.
def obtenerInformacion ( slugEmpresa ):

    urlInfoEmpresa =  "https://librebor.me/borme/api/v1/empresa/xxx-xxx-xxx/"
    urlInfoEmpresa = urlInfoEmpresa.replace("xxx-xxx-xxx" , slugEmpresa)

    # print(urlInfoEmpresa)
    respuesta = requests.get(urlInfoEmpresa)

    if respuesta.status_code == 200:
        print("conexión satisfactoria")
        informacionEmpresa = json.loads( respuesta.text )
        return informacionEmpresa
    else:
        print("La conexión no ha salido bien :( ")


# Función 4: A partir de la información de la empresa, obtener datos:
def imprimirTipoEmpresa ( informacionEmpresa ):
    print( "La empresa "+informacionEmpresa["name"]+" es del tipo "+informacionEmpresa["type"] )



# PROGRAMA PRINCIPAL:

# Solicitar al usuario la palabra a buscar. Listar todas las empresas cuyo nombre contienen esa palabra:

solicitud = input("Por favor introduce la palabra que quieras buscar: ") 
listaDeEmpresas = obtenerEmpresas ( solicitud )

if ( len ( listaDeEmpresas["objects"] ) == 0 ):
    print("Lo siento, ninguna empresa contiene la palabra "+solicitud+" en su nombre")

else:
    mostrarEmpresas ( listaDeEmpresas )

    eleccion = int ( input("Introduce el número de la empresa de la cual desees información: ") )

    slugEmpresa = listaDeEmpresas["objects"][eleccion]["slug"]
    infoEmpresa = obtenerInformacion ( slugEmpresa )

    imprimirTipoEmpresa ( infoEmpresa )


