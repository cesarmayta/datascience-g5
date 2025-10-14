import os
from time import sleep
import csv

def cargar_alumnos(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            next(f)
            lineas = f.readlines()
            dic_alumnos = {}
            for linea in lineas:
                dni, nombre, email = linea.strip().split(',')
                dic_alumnos[dni] = {
                    'nombre': nombre,
                    'email': email
                }
            return dic_alumnos
    else:
        return {}
    
def cargar_alumnos_csv(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', newline='') as f:
            reader = csv.DictReader(f)
            #next(reader,None)
            dic_datos = {}
            for row in reader:
                dni = row['dni']
                dic_datos[dni] = {
                    'nombre': row['Nombre'],
                    'email': row['Email']
                }
            return dic_datos
        
def guardar_alumnos(dic_datos,nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(['dni','Nombre','Email'])
        for dni, info in dic_datos.items():
            escritor.writerow([dni, info['nombre'], info['email']])
    
        
#dic_alumnos = cargar_alumnos('alumnos.csv')
dic_alumnos = cargar_alumnos_csv('alumnos.csv')

ANCHO = 50

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR ALUMNO")
        print("=" * ANCHO)
        
        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese Nombre: ")
        email = input("Ingrese Email: ")
        dic_nuevo_alumno = {
            'nombre': nombre,
            'email': email
        }
        dic_alumnos[dni] = dic_nuevo_alumno
        print("Alumno registrado exitosamente.")
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR ALUMNOS")
        print("=" * ANCHO)
        
        for dni,info in dic_alumnos.items():
            print(f"DNI : {dni}")
            print(f"Nombre : {info['nombre']}")
            print(f"EMAIL : {info['email']}")
            print("*"*ANCHO)
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR ALUMNO")
        print("=" * ANCHO)
        dni = input("Ingrese DNI del alumno a actualizar: ")
        if dni in dic_alumnos:
            print(f"Alumno encontrado: {dic_alumnos[dni]['nombre']}")
            nuevo_nombre = input("Ingrese nuevo nombre (dejar en blanco para no cambiar): ")
            nuevo_email = input("Ingrese nuevo email (dejar en blanco para no cambiar): ")
            if nuevo_nombre:
                dic_alumnos[dni]['nombre'] = nuevo_nombre
            if nuevo_email:
                dic_alumnos[dni]['email'] = nuevo_email
            
            print("Alumno actualizado exitosamente.")
        else:
            print("Alumno no encontrado.")
    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR ALUMNO")
        print("=" * ANCHO)
        dni = input("Ingrese DNI del alumno a eliminar: ")
        if dni in dic_alumnos:
            del dic_alumnos[dni]
            print("Alumno eliminado exitosamente.")
        else:
            print("Alumno no encontrado.")
        
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        guardar_alumnos(dic_alumnos,'alumnos.csv')
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")