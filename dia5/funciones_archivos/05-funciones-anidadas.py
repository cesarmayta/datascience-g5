# FUNCIONES ANIDADAS
# Las funciones anidadas son funciones definidas dentro de otras funciones.

def operacion(a,b):
    def suma(a,b):
        return a + b
    def resta(a,b):
        return a - b
    def multiplicacion(a,b):
        return a * b
    def division(a,b):
        return a / b

    print("Suma:", suma(a,b))
    print("Resta:", resta(a,b))
    print("Multiplicación:", multiplicacion(a,b))
    print("División:", division(a,b))
    
operacion(10,5)

# FUNCIONES RECURSIVAS
# Una función recursiva es una función que se llama a sí misma para resolver un problema.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print("Factorial de 5:", factorial(5))

# FUNCIONES COMO PARAMETRO DE OTRA FUNCIÓN
def aplicar_funcion(func, valor):
    return func(valor)

doblar = lambda x: x * 2
resultado = aplicar_funcion(doblar, 5)
print("Resultado de aplicar función:", resultado)