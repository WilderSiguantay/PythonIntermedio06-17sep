#09/09/2021
import os

'''
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing.  The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
'''
#LECTURA
# \\ Windows
# / Linux
# / Mac OS


ruta = 'Lectura.txt'

archivo = open(ruta)
'''
primeraLinea = archivo.readline()
segundaLinea = archivo.readline()

print(primeraLinea)
print(segundaLinea)
print('-----------------')

terceraLinea = archivo.readline(5)
print(terceraLinea)

archivo.close()
print('Fin de lectura')

#LEER EL ARCHIVO COMPLETO
linea = archivo.readline()

while linea !="":
    print(linea)
    linea = archivo.readline()


'''
#UNIX fin de linea = \n
#WINDOWS \r \n
#Mac \r

#print(archivo.readlines())  


#-------------ESCRITURA DE ARCHIVOS----------
'''
saludo = open('saludo.py', 'w')
saludo.write("""print("Hola Mundo") \n""")
saludo.close()

contenidoNuevo = """print("NuevaLinea")"""


archivo = open('saludo.py', 'a')
archivo.write(contenidoNuevo)
print("Escritura de archivo exitosa")
archivo.close()

'''




#os.remove('saludo.py')


#Funciones 

def get_File(ruta, permiso):
    archivo = open(ruta,permiso)
    return archivo

archivo = get_File('Lectura.txt', 'r+')
print(archivo.readline())