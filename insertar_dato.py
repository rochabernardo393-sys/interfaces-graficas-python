"""
Formulario para insertar cursos en la tabla T_CURSOS (academia.db)

Datos a pedir:
-nombre
-descripción
-precio
-certificación
-elegir mañanas o tardes

Una vez insertado --> mensaje de estado ok, Fallo al insertar
Borrar los datos en ambos casos
"""

from tkinter import *
from tkinter import messagebox
import sqlite3


def limpiar_campos():
    caja_nombre.delete(0, END)
    caja_descripcion.delete("1.0", END)
    caja_precio.delete(0, END)
    var_certificacion.set(0)
    var_horario.set("Mañanas")


def insertar_curso():

    nombre = caja_nombre.get()
    descripcion = caja_descripcion.get("1.0", "end-1c")
    precio = caja_precio.get()
    certificacion = var_certificacion.get()
    horario = var_horario.get()

    # Campos obligatorios
    if nombre == "" or precio == "":
        messagebox.showerror(
            "Error",
            "El nombre y el precio son obligatorios."
        )
        return

    # El precio debe ser un número
    try:
        precio = float(precio)
    except ValueError:
        messagebox.showerror(
            "Error",
            "El precio debe ser un número."
        )
        return

    # Insertar en la base de datos
    try:
        conexion = sqlite3.connect("academia.db")
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO T_CURSOS
            (nombre, descripcion, precio, certificacion, horario)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, precio, certificacion, horario))

        conexion.commit()

        messagebox.showinfo("Correcto", "Curso insertado correctamente.")

    except sqlite3.Error as error:
        messagebox.showerror("Error", "Fallo al insertar: " + str(error))

    finally:
        try:
            conexion.close()
        except NameError:
            pass

    # Borrar los datos en ambos casos (OK o fallo)
    limpiar_campos()


# -------------------------------
# VENTANA
# -------------------------------

ventana = Tk()
ventana.title("Academia - Cursos")
ventana.geometry("400x540")

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
var_certificacion = IntVar()
Checkbutton(ventana, text="Sí, tiene certificación",
            variable=var_certificacion).pack()

# HORARIO: RADIOBUTTON
Label(ventana, text="Horario:").pack()
var_horario = StringVar(value="Mañanas")
Radiobutton(ventana, text="Mañanas", variable=var_horario, value="Mañanas").pack()
Radiobutton(ventana, text="Tardes", variable=var_horario, value="Tardes").pack()

# BOTÓN
Button(ventana, text="INSERTAR CURSO", command=insertar_curso).pack(pady=15)

ventana.mainloop()