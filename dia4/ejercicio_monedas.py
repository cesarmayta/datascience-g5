"""
RETO 1 : CREAR UN PROGRAMA USANDO COMO EJEMPLO EL CODIGO DE LA CALCULADORA 
QUE PERMITA CONVERTIR EL VALOR DE UNA MONEDA DE SOLES A DOLARES Y VICEVERSA,
POR EJEMPLO SI INGRESO CONVERTIR SOLES A DOLARES E INGRESO 3000 SOLES 
DEBERIA MOSTRARME SU VALOR EN DOLARES QUE SERIA 1000 DOLARES CONSIDERANDO 
QUE EL TIPO DE CAMBIO ES 3
"""
# DATOS DE ENTRADA(INPUT)
tipo_cambio = 3
moneda_origen = "SOLES"
moneda_destino = "DOLARES"

while(True):
    print("""
            =============================================
                        CONVERTIDOR DE MONEDAS
            =============================================
                    [1] CONVERTIR SOLES A DOLARES
                    [2] CONVERTIR DOLARES A SOLES
                    [3] SALIR
            =============================================
                """)
    opcion = int(input("Ingrese una opcion (1-2): "))
    if(opcion == 1):
        moneda_origen = "SOLES"
        moneda_destino = "DOLARES"
        monto_origen = float(input("Ingrese el monto a convertir: "))
        # PROCESO
        monto_destino = monto_origen / tipo_cambio
    elif(opcion == 2):
        moneda_origen = "DOLARES"
        moneda_destino = "SOLES"
        monto_origen = float(input("Ingrese el monto a convertir: "))
        # PROCESO
        monto_destino = monto_origen * tipo_cambio
    elif(opcion == 3):
        print("Gracias por usar el convertidor de monedas")
        exit()
    else:
        print("Opcion no valida")
        continue
    # DATOS DE SALIDA(OUTPUT)
    print(f"RESULTADO : {monto_origen} {moneda_origen} son {monto_destino} {moneda_destino}")