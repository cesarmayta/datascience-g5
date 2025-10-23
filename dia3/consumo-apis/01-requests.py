# pip install requests
# pip install tabulate
# pip install mysql-connector-python
import requests
from tabulate import tabulate
import mysql.connector

URL = 'https://randomuser.me/api/?results=10'

response = requests.get(URL)

#print(f'codigo de respuesta : {response.status_code}')
#print(f' contenido : {response.json()}')
if response.status_code == 200:
    data = response.json()
    rows = []
    for u in data['results']:
        nombre = u['name']['first'] + ' ' + u['name']['last']
        pais = u['location']['country']
        correo = u['email']
        telefono = u['phone']
        foto = u['picture']['large']
        rows.append([nombre, pais, correo, telefono, foto])

    headers = ['Nombre', 'País', 'Correo', 'Teléfono', 'Foto']
    print(tabulate(rows, headers=headers, tablefmt='grid'))

    # Conexión a la base de datos MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root2025',
        database='db_g5'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuario(
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(255) NOT NULL,
            pais VARCHAR(255) NOT NULL,
            correo VARCHAR(255),
            telefono VARCHAR(100),
            foto TEXT
            );
            """
        )
        # registramos usuarios en la bd
        for usuario in rows:
            cursor.execute(
                """
                    insert into usuario(nombre,pais,correo,telefono,foto)
                    values(%s,%s,%s,%s,%s)
                """,
                usuario
            )

        connection.commit()
        print(f' registros importados a la base de datos!!!')
    else:
        print(f'no esta conectado a la BD')

else:
    print(f'algo salio mal : {response.status_code}')