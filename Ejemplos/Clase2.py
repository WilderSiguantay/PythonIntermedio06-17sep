#class ClassName:  --Palabra reservada class y el nombre de la clase (ClassName)
    #declaraciones
'''
class Persona:
    pass #instruccion que puede ser utilizada cuando querramos una sentencia sintacticamente pero en realidad no hace nada

#instancia a la clase persona

wilder = Persona() #hemos creado un objeto wilder de tipo persona

print(wilder)
   
class Persona:
    nombre = ''
    apellido = ''
    universidad = ''
    carnet = ''

wilder = Persona()
wilder.nombre = 'Wilder'
wilder.apellido = 'Siguantay'
wilder.universidad = 'USAC'
wilder.carnet = '2421451454'

ruben = Persona()
ruben.nombre = 'Ruben'
ruben.apellido = 'Urizar'
ruben.universidad = 'USAC'
ruben.carnet = '2141541401'

print('Nombre Persona 1: ' , ruben.nombre , " Apellido: " + ruben.apellido)
print('Nombre de persona 2: ' + wilder.nombre)

print('Tu nombre es: %s y estudias en: %s' %(wilder.nombre,wilder.universidad))


class Person:
    name=''
    universidad =''

    def print_name(self):
        print(self.name)

jorge = Person()
jorge.name = 'Jorge'
jorge.universidad = 'Universidad de San Carlos de Guatemala'

#llamar a un metodo
jorge.print_name()

def print_datos(nombre, apellido):
    print(nombre,  ' ', apellido)

#llamada a funcion
print_datos('Wilder', 'Siguantay')



'''

class Person:
    def __init__(self, nombre,universidad ):
        self.name = nombre
        self.school = universidad

    def print_name(self):
        print(self.name)

    def print_school(self):
        print(self.school)

jorge = Person('Jorge', 'USAC')

jorge.print_name()

jorge.print_school()

''' 
SINTAXIS DE UN METODO O FUNCION
def nombreDeFuncion():
    bloque de codigo
'''

#Funcion sumar sin retorno
def sumar(numero1, numero2):
    resultado = 0
    resultado = numero1 + numero2
    print('El resultado es: ', resultado)

sumar(1,2)

#Funcion con retorno

def sumar_retorno(n1, n2):
    resultado = 0
    resultado = n1 + n2
    return resultado

respuesta = sumar_retorno(2,3)
print(respuesta)

#Parámetro arbitrarios
#Funcion espera recibir un numero arbitrario -desconocido- de argumentos, estos argumentos
#llegan a la funcion en forma de tupla, para definir argumentos arbitrarios, se antecede al parametro un *
def my_function(*kids):
    print("Funcion con argumentos Arbitrarios")
    print("El niño mas joven es: " + kids[2])

my_function("Emil", "Wilder", "Jorge", "Luis", "Julio")


#Argumentos con palabras clave

def my_function2(child3, child2, child1):
    print('---Funcion con palabra clave')
    print('A imprimir: '+ child3)

my_function2(child2='Elias', child3='Ruben', child1='Andrea')


#Argumentos arbitrarios tipo clave valor

def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrario, **kwords):
    print(parametro_fijo)
    for argumento in arbitrario:
        print(argumento)
    #[1,2,3,4,5,6,7,8]

    #Los argumentos arbitrarios tipo clave valor, se recorren como diccionarios.
    for clave in kwords:
        print('El valor de', clave,'es', kwords[clave])

recorrer_parametros_arbitrarios('ParametroFijo', 'arbitrario 1', 'arbitrario 2', 'arbitrario 3','Arbitrario 4', clave1='valor uno', clave2='valor 2')