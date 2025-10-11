import os
from time import sleep

# EJERCIO FINAL MODULO 1 - CRUD EMPRESAS
# NOMBRE : CESAR MAYTA

dic_empresas = {
    '20454545':{
        'razon_social': 'EMPRESA SAC',
        'direccion':'CALLE EL SOL 123',
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")