import requests

url = "https://www.google.com/"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    print("conexion existosa")
else:
    print("PROBLEMA")