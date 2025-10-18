import mysql.connector
from tabulate import tabulate

# creamos una conexión
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_g5'
)

print(f'estas conectado a a la base de datos : {connection.database}')

# select 
alumno_cursor = connection.cursor()
alumno_cursor.execute('select * from alumno')
resultado = alumno_cursor.fetchall()

# for registro in resultado:
#     print('*******************')
#     print(f'dni : {registro[1]}')

columnas = ['id','dni','nombre','email','nota']

print(tabulate(resultado,headers=columnas,tablefmt='grid'))

#cerramos la conexión
connection.close()