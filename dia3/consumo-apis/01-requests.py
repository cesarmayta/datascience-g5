# pip install requests
# pip install tabulate
import requests
from tabulate import tabulate

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

else:
    print(f'algo salio mal : {response.status_code}')