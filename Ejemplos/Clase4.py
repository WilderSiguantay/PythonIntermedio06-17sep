#Conexion a base de datos
#python.exe -m pip install --upgrade pip

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "pythondb"
)

mycursor = mydb.cursor()

#CREAR BASE DE DATOS
#mycursor.execute('CREATE DATABASE pythondb')

#mycursor.execute('SHOW DATABASES')

#for x in mycursor:
 #   print(x)

#CREAR TABLA 

#mycursor.execute('CREATE TABLE cliente (nombre varchar(255), direccion varchar(255))')

mycursor.execute('SHOW TABLES')

for x in mycursor:
    print(x)

#INSERTAR DATOS EN TABLA

#sql = "Insert into clientes (nombre , direccion) values (%s , %s)"
#val = ("Ruben Urizar", "Universidad de San Carlos de Guatemala")

#mycursor.execute(sql , val)

#mydb.commit()

#print(mycursor.rowcount, "DATOS INSERTADOS")

#INSERTAR MUCHOS

'''
sql = "Insert into clientes(nombre, direccion) values (%s,%s)"
val = [
    ('Nombre1','Direccion 1'),
    ('Nombre2','Direccion 2'),
    ('Nombre3','Direccion 3'),
    ('Nombre4','Direccion 4'),
    ('Nombre5','Direccion 5'),
    ('Nombre6','Direccion 6'),
    ('Nombre7','Direccion 7'),
    ('Nombre8','Direccion 8'),
    ('Nombre9','Direccion 9'),
    ('Nombre10','Direccion 10')
]

mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount, " Datos insertados exitosamente")


'''

mycursor.execute('SELECT * FROM Clientes')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)