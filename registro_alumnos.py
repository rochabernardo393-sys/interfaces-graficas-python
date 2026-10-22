from tkinter import *

def registrar():
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    label_resultado.config(text=f"Alumno registrado: {nombre} {apellidos}")
 
root = Tk()
root.title("Registro de alumnos")
root.geometry("400x300")

frame = Frame(root)
frame.pack(pady=10)

titulo = Label(frame, text="REGISTRO DE ALUMNOS")
titulo.pack(pady=5)
titulo.config(font=("Arial",16))

label_nombre = Label(frame, text="Nombre:")
label_nombre.pack()

entry_nombre = Entry(frame, width=30)
entry_nombre.pack(pady=5)

label_apellidos = Label(frame, text="Apellidos:")
label_apellidos.pack()

entry_apellidos = Entry(frame, width=30)
entry_apellidos.pack(pady=5)

boton = Button(frame, text="Registrar alumno", command=registrar)
boton.pack(pady=5)

label_resultado = Label(frame, text="")
label_resultado.pack(pady=5)

root.mainloop()