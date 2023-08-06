'''
En este script se detalla cómo se puede realizar con python un envío de información a un correo electrónico.
Para ello primero debemos crear un servidor SMTP que se encargue de realizar el envío hacia el correo destinatario desginado.


'''


# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage



from string import punctuation

# 1) función que me abra el archivo externo y me lea el contenido
def abrir_archivo(documento):

    with open(documento,"r",encoding="utf8") as archivo:
        contenido = archivo.read()

    return contenido

# 2) función que me obtenga las líneas que tiene el documento
def obtener_lineas(contenido):
    return contenido.splitlines()

# 3) función que me obtenga las palabras del documento
def obtener_palabras(lineas):
    palabras = []
    for linea in lineas:
        palabras.extend( linea.split() )
    
    return palabras

def procesar_texto (documento):
    with open(documento,"r",encoding="utf8") as archivo:
        contenido = archivo.read()
    
    for punct in punctuation:
        contenido = contenido.replace(punct , "")
    lineas = contenido.splitlines()

    palabras = []
    for linea in lineas:
        palabras.extend( linea.split() )
    
    return contenido , lineas , palabras


# 4) función que me cuente cuántas veces aparece la palabra "whale"
def contar_palabra ( palabra_contar , palabras ):

    cuenta = palabras.count( palabra_contar )
    return cuenta

# 5) función que me dé el promedio de palabras/línea
def promedio ( long_lineas , long_palabras ):
    prom =  long_palabras / long_lineas 
    return prom

# 6) función que me dé el porcentaje de veces que aparece una cierta palabra
def porcentaje ( palabra , palabras ):
    porc = contar_palabra ( palabra , palabras ) / len(palabras) * 100

    return porc


# 7) función que  me escriba en un doc externo las líneas en las que aprece cierta 
# palabra
def extraer_info ( documento , lineas , palabra ):

    # 1) abrir el documento en modo escritura:
    # with open(documento , "w" ) as archivo:
    archivo = open(documento , "w")
    for linea in lineas:
        palabras = linea.split()
        plural = palabra+"s"

        CON1 = palabra in palabras
        CON2 = plural in palabras
        CON3 = palabra.capitalize() in palabras
        CON4 = plural.capitalize() in palabras

        if   CON1 or CON2 or CON3 or CON4:
            
            archivo.write(linea+"\n")
            
    archivo.close()
    
    print("Ya ha acabado")

    # No devolvemos nada.





contenido , lineas , palabras = procesar_texto ("Moby Dick.txt")

# Open the plain text file whose name is in textfile for reading.



# texto = ""

# cuenta_whale = contar_palabra("whale" , palabras )
# texto += f"\nwhale aparece en el texto {cuenta_whale} veces"

# cuenta_city = contar_palabra("city" , palabras )
# texto += f"\ncity aparece en el texto {cuenta_city} veces"

# texto += f"\nel promedio de pal/lin es: { promedio ( len(lineas) , len(palabras) ) }"

# palabra = "whale"
# texto += f"\nla palabra {palabra} aparece un { porcentaje(palabra, palabras)} % de veces en el texto"

# palabra = "city"
# texto += f"\nla palabra {palabra} aparece un { porcentaje(palabra, palabras)} % de veces en el texto"



archivo = open("texto.txt","r")
texto = archivo.read()
archivo.close()

msg = EmailMessage()
msg.set_content(texto)


# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'Prueba envío python'
msg['From'] = "mauricio@dominioinventadopython.com"
msg['To'] = "mauricio.rubio@techtalents.es"

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

# programaspython234@gmail.com