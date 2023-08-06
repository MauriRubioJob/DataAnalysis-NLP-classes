# Lector PDF PyPDF2

# 1) importar el módulo
import PyPDF2

# 2) abrir archivo externo
archivo = open("Codigo_penal_militar.pdf", "rb")

# 3) Leemos el archivo
pdf = PyPDF2.PdfFileReader( archivo )


print( type(pdf) )

pag_1 = pdf.getPage(2)

num_pags = pdf.getNumPages()

print("Este pdf tiene" , num_pags , "páginas")



# print(type (pag_1 ))

# texto_1 = pag_1.

# print(type(texto_1))
# print(texto_1)