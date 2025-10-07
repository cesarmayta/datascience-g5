# CALCULADORA CON PYTHON
import os
from time import sleep
bandera = True
while(bandera):
    os.system("clear")
    print("================ CALCULADORA CON PYTHON ============")
    numero1 = int(input("Número 1 : "))
    numero2 = int(input("Número 2 : "))
    print("========= OPCIONES ========")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion = int(input("Ingrese la opcion que desea: "))
    if(opcion == 1):
        print("======= SUMA =======")
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado}")
    elif(opcion == 2):
        print("======= RESTA =======")
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado}")
    elif(opcion == 3):
        print("======= MULTIPLICACION =======")
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif(opcion == 4):
        print("======= DIVISION =======")
        if(numero2 != 0):
            resultado = numero1 / numero2
            print(f"El resultado de la division es: {resultado}")
        else:
            print("No se puede dividir entre 0")
    else:
        print("Opcion no valida")
        
    sleep(2)
    os.system("clear")
        
    bandera = input("¿desea continuar...?(si,no) : ")
    if(bandera == "si"):
        bandera = True
    else:
        bandera = False
        print("Gracias por usar la calculadora")
    