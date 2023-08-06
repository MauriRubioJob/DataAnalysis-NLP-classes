# import pdfminer.high_level


# Paso 2)
# archivo = open("LPI.pdf", "rb")
# # Paso 3)
# contenido = pdfminer.high_level.extract_text ( archivo )
# archivo.close()

archivo = open("prueba.txt", "r",encoding = "utf8")
contenido = archivo.read ( )
archivo.close()


lineas = contenido.splitlines()

lineas_limpias = []

# 1) Voy a limpiar las páginas y las cabeceras
for linea in lineas:
    if linea.startswith("Página") or linea.startswith("BOLETÍN OFICIAL DEL ESTADO") or linea.startswith("LEGISLACIÓN CONSOLIDADA"):
        pass
    else:
        lineas_limpias.append(linea)

    
    # if ( linea.startswith("–") and linea.endswith("–") )  or linea.startswith("BOLETÍN OFICIAL DEL ESTADO") or linea.startswith("LEGISLACIÓN CONSOLIDADA"):
    #     pass
    # else:
    #     lineas_limpias.append(linea)

# 2)

limpio=[]

continuar = False

for linea in lineas_limpias:
    if linea.startswith("Artículo ") or linea.startswith("Disposición "):
        continuar = True

    if( linea.startswith("TÍTULO") or linea.startswith("CAPÍTULO") or linea.startswith("LIBRO") or linea.startswith("Sección") ):
        continuar = False

    if (continuar):
        limpio.append(linea)

# En la variable limpio tengo guardadas todas las líneas válidad. De títulos de artículos o textos de artículos

articulos = "\n".join(limpio)

while(True):
    if ("\n\n" in articulos):
        articulos = articulos.replace("\n\n","\n")
    else:
        break


# archivo = codecs.open('texto1.txt','w', 'utf-8')  
archivo = open("limpio_automatico.txt","w",encoding="utf8")
archivo.write(articulos)
archivo.close()