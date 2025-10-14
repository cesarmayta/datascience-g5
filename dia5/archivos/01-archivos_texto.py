# MANEJO DE ARCHIVOS DE TEXTO
# ESCRIBIR UN ARCHIVO TXT
with open('notas.txt','w') as archivo:
    archivo.write("Hola Mundo")
    archivo.write("\n")
    archivo.write("Esta es un clase de Python")
    
# LEER UN ARCHIVO TXT
with open('notas.txt','r') as archivo:
    contenido = archivo.read()
    print(contenido)
    
print("----- linea por linea -----")
# LEER CONTENIDO LINEA POR LINEA
with open('notas.txt','r') as archivo:
    for linea in archivo:
        print(linea.strip())  # Usar strip() para eliminar saltos de línea adicionales
        
# AÑADIR CONTENIDO A UN ARCHIVO TXT
with open('notas.txt','a') as archivo:
    nueva_linea = input("Escribe una nueva linea para añadir al archivo: ")
    archivo.write("\n")
    archivo.write(nueva_linea)
    print("Linea añadida.")