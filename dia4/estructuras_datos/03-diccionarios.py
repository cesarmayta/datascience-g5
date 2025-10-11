# DICCIONARIOS
# Son colecciones desordenadas de elementos que se almacenan en pares clave-valor. 
# Cada clave es única y se utiliza para acceder a su valor correspondiente.
# Se definen utilizando llaves {} y los pares clave-valor se separan por comas.

capitales = {
    "Perú": "Lima",
    "Ecuador": "Quito",
    "Colombia": "Bogotá",
    "Argentina": "Buenos Aires"
}

print(capitales['Ecuador'])  # Acceder al valor asociado a la clave 'Ecuador'

# Agregar o modificar un nuevo par clave-valor
capitales['Brasil'] = 'Brasilia'
nueva_capital = {
    "Chile": "Santiago"
}
capitales.update(nueva_capital)  # Agregar el nuevo par clave-valor al diccionario existente
print(capitales)

# Eliminar un par clave-valor
del capitales['Argentina']
capitales.pop('Colombia','NO EXISTE')  # Otra forma de eliminar un par clave-valor
print(capitales)

# Recorrer un diccionario
print("Recorriendo claves:")
for clave in capitales.keys():
    print(clave)
    
print("Recorriendo valores:")
for valor in capitales.values():
    print(valor)
    
print("Recorriendo pares clave-valor:")
for clave, valor in capitales.items():
    print(f"la capital de {clave} es {valor}")