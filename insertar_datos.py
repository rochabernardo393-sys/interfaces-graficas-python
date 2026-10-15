from tkinter import *
from tkinter import messagebox
import sqlite3

ventana = Tk()
ventana.title("Academia - Cursos")
ventana.geometry("400x520")

# NOMBRE
Label(ventana, text="Nombre del curso:").pack()

caja_nombre = Entry(ventana, width=35)
caja_nombre.pack(pady=5)

# DESCRIPCIÓN
Label(ventana, text="Descripción:").pack()

caja_descripcion = Text(ventana, width=30, height=5, font=("Consolas", 12),
                        padx=15, pady=15, selectbackground="red")
caja_descripcion.pack(pady=5)

# PRECIO
Label(ventana, text="Precio (€):").pack()

caja_precio = Entry(ventana, width=35)
caja_precio.pack(pady=5)

# CERTIFICACIÓN: CHECKBUTTON
Label(ventana, text="¿Tiene certificación?").pack()

certificado = IntVar()
Checkbutton(ventana, text="Sí, tiene certificación", variable=certificado).pack()

# HORARIO: RADIOBUTTON
Label(ventana, text="Horario:").pack()

horario = StringVar(value="Mañanas")
Radiobutton(ventana, text="Mañanas", variable=horario, value="Mañanas").pack()
Radiobutton(ventana, text="Tardes", variable=horario, value="Tardes").pack()

# BOTÓN
Button(ventana, text="INSERTAR CURSO").pack(pady=15)

ventana.mainloop()