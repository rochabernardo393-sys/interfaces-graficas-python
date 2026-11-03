from  tkinter import *

def registrar():
    nombre = entry_nombre.get().strip()
    apellidos = entry_apellidos.get().strip()

    if nombre == "" or apellidos == "":
        label_resultado.config(
            text="Error: debes introducir el nombre y los apelllidos.",
            fg="red"
        )


root = Tk()
root.title("Registro de alumnos")

frame = Frame(root)
frame.pack(padx=20, pady=20)

label_titulo = Label(frame, text="REGISTRO DE ALUMNOS", font=("Arial", 14,"bold"))
label_titulo.pack(pady=10)

label_nombre = Label(frame, text="Nombre:")
label_nombre.pack()

entry_nombre = Entry(frame, width=30)
entry_nombre.pack(pady=5)

label_apellidos = Label(frame, text="Apellidos:")
label_apellidos.pack()

entry_apellidos = Entry(frame, width=30)
entry_apellidos.pack(pady=5)

boton = Button(frame, text="Registrar alumno", command=registrar)
boton.pack(pady=10)

label_resultado = Label(frame,text="")
label_resultado.pack(pady=10)

root.mainloop()