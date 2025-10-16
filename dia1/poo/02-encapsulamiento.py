#ENCAPSULAMIENTO EN POO CON PYTHON
class Usuario:
    __email = 'cesar'
    __password = '123'
    
    def __init__(self):
        pass
    
    def login(self,email,password):
        if email == self.__email and password == self.__password:
            print('Login exitoso')
        else:
            print('Login fallido')
            
print("LOGIN DE USUARIOS")
email = input('Ingrese su email: ')
password = input('Ingrese su password: ')

usuario = Usuario()
usuario.login(email,password)
