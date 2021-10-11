materias = {}
materias["Lunes"] = [6103,7540]
materias["Martes"] = [6201]
materias["Miercoles"] = [6103,7540]
materias["Jueves"] = []
materias["Viernes"] = [6201]


#print(materias['Domingo'])
#print(materias.get('Domingo', 'No existe'))

#Declarar diccinoario capitales

capitales = {'Chile': 'Santiago',
             'España':'Madrid',
             'Francia':'Paris',
             'Guatemala':'Guatemala'}

#print('La capital de Chile es:' , capitales['Chile'])

#ELIMINAR UN REGISTRO
#del capitales['Guatemala']

#print('\n Hay {0} paises \n'.format(len(capitales))) #tres paises


#AGREGAR A DICCIONARIO
capitales['Portugal'] = 'Lisboa' 

#for pais, capital in capitales.items():
 #   print('La capital de {0} es {1}'.format(pais, capital))


#VERIFICAR VALORES
d = {'x': 12, 'y':7}
#verificar si existe clave
#if 'x' in d:
 #   print(d['x'])
print(d.setdefault('x'))

#DECLARAR DICCIONARIOS
#a partir de una tupla
dic2 = dict((('mesa',5),('silla',10)))
#print(dic2['mesa'])
#a partir de cadenas
dic3 = dict(ALM=5, CAD=10)
#print(dic3['CAD'])

#print(dic2.items()) #obtiene una lista de tuplas clave:valor
#print(dic2.keys()) #obtiene una lista de las claves
#print(dic2.values()) #obtiene una lista de los valores





