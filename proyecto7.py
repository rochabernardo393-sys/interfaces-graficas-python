from tkinter import *
from tkinter import messagebox
import sqlite3 

def mostrar_cursos():
    texto.delete("1.0", END)

    conexion = None
    try:
        conexion = sqlite3.connect("academia.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM T_CURSOS")
        cursos = cursor.fetchall()

        if len(cursos) == 0:
            texto.insert(END, "No hay cursos registrados")
        else:
            for i, curso in enumerate(cursos):
                texto.insert(END, f"ID del curso: {curso[0]}\n")
                texto.insert(END, f"Nombre: {curso[1]}\n")
                texto.insert(END, f"Descripción: {curso[2]}\n")
                texto.insert(END, f"Precio: {curso[3]} €\n")
                texto.insert(END, f"Horario: {curso[5]}\n")
                texto.insert(END, f"Certificación: {curso[4]}\n")

                if i < len(cursos) - 1:
                    texto.insert(END, "\n-------------------------------\n\n")

    except sqlite3.Error as error:
        messagebox.showerror("Error", f"Error al acceder a la base de datos:\n{error}")

    finally:
        if conexion is not None:
            conexion.close()




root = Tk()
root.title("Academia - Listado de cursos")
root.geometry("550x450")

texto = Text(root, width=60, height=20)
texto.pack(padx=10, pady=10)

boton = Button(root, text="MOSTRAR CURSOS", command=mostrar_cursos)
boton.pack(pady=10)

root.mainloop()