'''
Uno de los métodos de string que es clave y esencial a la hora de adentrarnos en los proyectos
personales es el siguiente:

Método:   startswith()  -> Este método nos ayuda a identificar aquellos string / cadenas de caracteres 
que comienzan por la palabra/carácter que indiquemos.

Por ejemplo, en la propuestas de los artículos, será esencial saber utilizarlo para determinar cuando empieza un artículo
    y acaba otro.

En la propuesta 3, la de los csv, sí va a ser muy importante wutilizar también el startswith.


'''


linea =    "Artículo 2:   El texto delimitado por.... "
linea2 = "TÍTULO: iifdwrlvò"
contenido = ""

if (linea.startswith("Artículo"):
    print("Esa línea es parte de un artículo")

