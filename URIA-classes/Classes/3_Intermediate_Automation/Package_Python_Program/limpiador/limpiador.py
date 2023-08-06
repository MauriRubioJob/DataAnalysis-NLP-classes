# import codecs
# archivo = codecs.open('texto1.txt','r', 'utf-8')  

archivo = open("Codigo_penal_militar.txt","r",encoding="utf8")

contenido = archivo.read()
archivo.close()

lineas = contenido.splitlines()

limpio=[]

continuar = False

for linea in lineas:
    if linea.startswith("Artículo"):
        continuar = True

    if(linea.startswith("TÍTULO") or linea.startswith("CAPÍTULO") or linea.startswith("LIBRO") or linea.startswith("Sección") ):
        continuar = False

    if (continuar):
        limpio.append(linea)
    
    

articulos = "\n".join(limpio)


# archivo = codecs.open('texto1.txt','w', 'utf-8')  
archivo = open("Codigo_Militar_articulos.txt","w",encoding="utf8")
archivo.write(articulos)
archivo.close()