import os
import math
from time import sleep

valor_salir = 7

while(True):
    os.system("clear")
    print(" ============ CALCULADORA CON PYTHON ========")
    print("========= OPCIONES DE MI CALCULADORA ========")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. potencia")
    print("6. raiz cuadrada")
    print("7. salir")
    opcion = int(input("Ingrese la opcion que desea: "))
    os.system("clear")
    if(opcion != valor_salir):
        numero1 = int(input("Número 1 : "))
        if(opcion != 6):
            numero2 = int(input("Número 2 : "))
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
    elif(opcion == 5):
        print("======= POTENCIA =======")
        resultado = math.pow(numero1,numero2)
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif(opcion == 6):
        print("======= RAIZ CUADRADA =======")
        resultado = math.sqrt(numero1)
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif(opcion == valor_salir):
        print("👋 ¡Gracias por usar la calculadora!")
        break
    else:
        print("❌ Opción no válida, intenta nuevamente.")
        
    sleep(2)