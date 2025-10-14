# PARAMETROS EN FUNCIONES
# Una función puede recibir parámetros para trabajar con datos externos.
# Los parámetros se definen entre los paréntesis de la definición de la función.

# Ejemplo sin parámetros
def saludar():
    print("Hola, ¿cómo estás?")
    
# Función con parametros por defecto
def potencia(base, exponente=2):
    return base ** exponente

# Función con múltiples retornos
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta
    
saludar()  # Llamada a la función sin parámetros
print(potencia(3))      # Llamada a la función con un parámetro (exponente por defecto)
print(potencia(3, 4))   # Llamada a la función con ambos parámetros
suma, resta = operaciones(5, 3)  # Llamada a la función con múltiples retornos
print(f"Suma: {suma}, Resta: {resta}")