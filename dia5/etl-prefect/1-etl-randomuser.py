import requests
import mysql.connector
from datetime import datetime
from tabulate import tabulate
from prefect import flow,task

@task
def extract():
    """
    extrae data de randomuser
    """
    URL = "https://randomuser.me/api/?results=10"
    response = requests.get(URL)
    data = []
    if response.status_code == 200:
        data = response.json()['results']
        
    return data

@task
def transform(data_users):
    """
    transformamos la data de randomuser
    """
    data_transformed = []
    for user in data_users:
        nombre = f"{user['name']['first']} {user['name']['last']}"
        sexo = user['gender']
        pais = user['location']['country']
        fecha_nac = user['dob']['date']
        fecha_nac = datetime.fromisoformat(fecha_nac.rstrip("Z")).date()
        data_transformed.append((nombre,sexo,pais,fecha_nac))
        
    return data_transformed

@task
def load(data_to_load):
    resultado = 0
    conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="db_g5"
    )
    cursor = conn.cursor()
    cursor.execute("""
               CREATE TABLE IF NOT EXISTS random_users (
               id INT AUTO_INCREMENT PRIMARY KEY,
               nombre VARCHAR(255),
               sexo VARCHAR(10),
               pais VARCHAR(100),
               fecha_nac DATE)
               """)
    conn.commit()
    insert_query = "INSERT INTO  random_users(nombre,sexo,pais,fecha_nac) VALUES(%s,%s,%s,%s)"
    cursor.executemany(insert_query,data_to_load)
    conn.commit()
    resultado = cursor.rowcount
    cursor.close()
    conn.close()
    return resultado

@flow(name='ETL Random User')
def main():
    data = extract()
    data_transformed = transform(data)
    cabeceras = ['nombre','sexo','pais','fecha_nac']
    print(tabulate(data_transformed,headers=cabeceras,tablefmt='grid'))
    resultado = load(data_transformed)
    print(f'se insertaron {resultado} registros en la bd')

if __name__ == "__main__":
    main()