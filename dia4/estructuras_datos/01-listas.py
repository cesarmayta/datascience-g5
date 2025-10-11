# LISTAS
# Una lista es una colección ordenada y mutable de elementos.
# Se definen utilizando corchetes [] y los elementos están separados por comas.
dias = ["lunes", "martes", "miércoles", "jueves","viernes"]

#imprimir uno o varios dias
print(dias[0])
print(dias[4])
print(dias[1:4])

#agregar valores a la lista
dias.append("Sábado")
dias.append("Domingo")
print(dias)

#eliminar valores de la lista
dias.pop() #elimina el último elemento
dias.pop(3) #elimina el elemento en la posición 0
print(dias)
#modificar un dato
dias[3] = "jueves"
dias[4] = "viernes"
print(dias)

#recorrer una lista
for dia in dias:
    print(f"Hoy es {dia}")
    
for contador in range(len(dias)):
    print(f"Hoy es {dias[contador]}")