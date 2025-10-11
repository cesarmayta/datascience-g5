import os
from time import sleep
# DATOS DE ENTRADA(INPUT)
tipo_cambio = 3
monedas = ["SOLES","DOLARES"]

tipo_cambio = [
    [1,1/3],
    [3,1]
]

menu = ("[1] CONVERTIR SOLES A DOLARES",
        "[2] CONVERTIR DOLARES A SOLES",
        "[3] SALIR")

while(True):
    os.system("clear")
    print("""
            =============================================
                        CONVERTIDOR DE MONEDAS
            =============================================
            """)
    for opcion in menu:
        print(f"                     {opcion}")
    print("""           
            =============================================
                """)
    opcion = int(input("Ingrese una opcion : "))
    if(opcion == 1):
        moneda_origen = 0
        moneda_destino = 1
    elif(opcion == 2):
        moneda_origen = 1
        moneda_destino = 0
    elif(opcion == 3):
        print("Gracias por usar el convertidor de monedas")
        exit()
    else:
        print("Opcion no valida")
        continue
    monto_origen = float(input(f"Ingrese el monto en {monedas[moneda_origen]} : "))
    # PROCESO
    monto_destino = round(monto_origen * tipo_cambio[moneda_origen][moneda_destino],2)
    # DATOS DE SALIDA(OUTPUT)
    print(f"RESULTADO : {monto_origen} {monedas[moneda_origen]} son {monto_destino} {monedas[moneda_destino]}")
    sleep(2)