# FUNCIONES EN PYTHON
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define utilizando la palabra clave 'def', seguida del nombre de la función y paréntesis.

def saludar(nombre):
    """Función que saluda a una persona por su nombre."""
    return f"Hola, {nombre}!"

nombre_usuario = input("Hola, ¿cómo te llamas? ")
print(saludar(nombre_usuario))

def sumar(a,b):
    """Función que suma dos números."""
    resultado = a + b
    return resultado

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
resultado_suma = sumar(num1, num2)
print(f"La suma de {num1} + {num2} es: {resultado_suma}")

#funcion con parametros por defecto
def potencia(base, exponente=2):
    """Función que calcula la potencia de un número."""
    return base ** exponente