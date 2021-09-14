#Operaciones con cadenas y listas

cadena1 = 'tengo una yama que se llama yama'
lista1= ['pero', 'manzana', 'naranja', 'uva']

#operaciones 
#Longitud
longitud = len(cadena1)
#no. de elementos
noElem = len(lista1)

print('Longitud de Cadena1: ' + str(longitud) + ' No. de elementos de lista1: ' + str(noElem))

#contar las apariciones de una palabra en particular en una cadena (Yama)
cuenta = cadena1.count('yama')
print('Veces que aparece la palabra Yama: '+str(cuenta))

#ver posicion de una palabra --nos va a devolver la posicion de la primera palabra que encuentre--
posicion = cadena1.find('yama')

print('Posicion de la palabra yama: '+ str(posicion))

#insertar cada 1 entre caracteres
cadena2 = cadena1.join('**')

print(cadena2)
#divide cadena por separador -> devuelve lista 
lista1 = cadena1.split(' ') 

#divide cadena por separador -> tupla
tupla1 = cadena1.partition(' ')

#buscar y sustituir terminos en una cadena
cadena2 = cadena1.replace('yama', 'gata', 2)

print(cadena2)

#Convertir a numero
numero = 3
cadena3 = str(numero)


#TUPLAS Y LISTAS

#Operaciones con listas y tuplas

#TUPLAS
tupla1 = (1,2,3) #declarar una tupla
tupla2 = 1,2,3 #misma declaracion pero sin parentesis
tupla3 = (1,) #Si es solo un elemento finalizar con una ","
tupla4 = tupla1,4,5,6 #anidar tuplas
tupla5 = () #declarar tupla vacia
#tupla6 =  
print(tupla4)

print(tupla4[1:3]) #accede a los valores hasta

#print(tupla2[2])

#tupla2[0] = 5 NO SE PUEDE ASIGNAR O MODIFICAR LA TUPLA

#Longitud de tupla
print('Numero de elementos: ' ,str(len(tupla1)))

#LISTAS

lista1 = ['uno',2,True, 'uno'] #lista heterogénea
lista2 = [1,2,3,4,5,6] #lista homogénea (numérica)

#Anidar listas
lista3 = ['nombre', lista1]
lista4 = [54,25,65,10,15,2,4,1]

#OPERACIONES CON LISTAS
print('Lista 1 heterogénea: ',lista1)
#Imprimir un elemento en específico
print(lista1[0])

#imprimir el ultimo elemento de una lista
print(lista4[-1])

#acceder a la lista anidad e imprimir el primer elemento
print(lista3[1][0])

#Invertir en orden de la lista
print(lista2[::-1])

#Cambiar el valor de un elemento de la lista
lista1[2] = False
print('----Cambiar un elemento---')
print(lista1)

lista2.pop(0) 
print(lista2)

#Elimina el primer elemento que coincida
lista1.remove('uno')
print(lista1)

#Otra forma de eliminar
del lista2[1]
print(lista2)

#añadir un elemento al final de la lista
lista2 =  lista2 + [7]
print(lista2)

#añadir un elemento con append
lista2.append(8)
print(lista2)

#extender listas
lista2.extend([9,10])
print(lista2)

#Eliminar elementos [desde:hasta]
del lista2[0:3]
print(lista2)

#borra todos los elementos de la lista
lista2[:] = []

print(lista2)

#numero de veces que aparece un elemento
lista6= [1,2,2,3,4,5,6,7,8,8]

print(lista6.count(2))

#Ver posicion que ocupa un elemento

print(lista6.index(7))

#ordenar una lista
lista4.sort(reverse=True)
print(lista4)
#ordenar una lista y guardarla en otra
print(lista4)
lista7 = sorted(lista4)
print(lista7)