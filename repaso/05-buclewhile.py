#BUCLE WHILE
contador = 1
while(contador <= 12):
    print(contador)
    contador += 1
    
salir = False 
while(salir == False):
    # ENTRADA
    numero1 = int(input("Ingrese el primer número : "))
    numero2 = int(input("Ingrese el segundo número : "))
    operacion = input("Ingrese la operación(+,-,*,/) : ")
    # PROCESO
    if(operacion == "+"):
        resultado = numero1 + numero2
    elif(operacion == "-"):
        resultado = numero1 - numero2
    elif(operacion == "*"):
        resultado = numero1 * numero2
    elif(operacion == "/"):
        resultado = numero1 / numero2
    else:
        print("Operación no valida")
        exit()

    # SALIDA
    print(f"El resultado de {numero1} {operacion} {numero2} es {resultado}")
    bandera = input("¿Desea salir del programa?(si,no) : ")
    if (bandera == "si"):
        salir = True
        print("GRACIAS POR USAR MI PROGRAMA...")