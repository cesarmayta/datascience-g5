from tkinter import *
from tkinter import messagebox

def saludar():
    nombre = txt_nombre.get()
    print(f"Hola {nombre}")
    messagebox.showinfo("Saludo",f"Hola {nombre}")

#crear un objeto de clase TK
app = Tk()
app.title("Mi primera app con tkinter")
app.geometry("300x100")

#agregar un frame
frame = Frame(app)
frame.grid(row=0,column=0,columnspan=3,pady=20,padx=20)

#agregar una etiqueta
lb_nombre = Label(frame,text="Nombre:")
lb_nombre.grid(row=1,column=0)
#agregar una caja de texto
txt_nombre = Entry(frame)
txt_nombre.grid(row=1,column=1)
#agregar un boton
btn_saludar = Button(frame,text="Saludar",command=saludar)
btn_saludar.grid(row=1,column=2,padx=10)

app.mainloop()