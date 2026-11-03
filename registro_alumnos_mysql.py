from tkinter import *                      
import mysql.connector                     
from mysql.connector import Error          


def conectar():                            
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="practica_tienda"
    )


def crear_tabla():                         
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellidos VARCHAR(100) NOT NULL
        )
    """)
    conexion.commit()
    cursor.close()
    conexion.close()


def registrar():                      
    nombre = entry_nombre.get().strip()            
    apellidos = entry_apellidos.get().strip()

    if nombre == "" or apellidos == "":            
        label_resultado.config(
            text="Error: debes introducir el nombre y los apellidos.",
            fg="red"
        )
        return                                     

    conexion = None                                
    cursor = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO alumnos (nombre, apellidos) VALUES (%s, %s)",
            (nombre, apellidos)
        )
        conexion.commit()                          

        label_resultado.config(
            text=f"Alumno registrado y guardado: {nombre} {apellidos}",
            fg="green"
        )
        entry_nombre.delete(0, END)                
        entry_apellidos.delete(0, END)

    except Error as error:                         
        label_resultado.config(text=f"Error de base de datos: {error}", fg="red")

    finally:                                       
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()


def ver_alumnos():                         
    conexion = None
    cursor = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, apellidos FROM alumnos")   
        filas = cursor.fetchall()                 

        if len(filas) == 0:                        
            label_lista.config(text="No hay alumnos guardados todavía.")
        else:
            texto = ""                            
            for fila in filas:                     
                texto = texto + f"{fila[0]} - {fila[1]} {fila[2]}\n"   
            label_lista.config(text=texto)         

    except Error as error:
        label_lista.config(text=f"Error de base de datos: {error}")

    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()




root = Tk()                                
root.title("Registro de alumnos")

frame = Frame(root)                       
frame.pack(padx=20, pady=20)

Label(frame, text="REGISTRO DE ALUMNOS", font=("Arial", 14, "bold")).pack(pady=10)

Label(frame, text="Nombre:").pack()
entry_nombre = Entry(frame, width=30)
entry_nombre.pack(pady=5)

Label(frame, text="Apellidos:").pack()
entry_apellidos = Entry(frame, width=30)
entry_apellidos.pack(pady=5)

Button(frame, text="Registrar alumno", command=registrar).pack(pady=10)

label_resultado = Label(frame, text="")    
label_resultado.pack(pady=5)

Button(frame, text="Ver alumnos guardados", command=ver_alumnos).pack(pady=10)

label_lista = Label(frame, text="", justify=LEFT)   
label_lista.pack(pady=5)

try:                                       
    crear_tabla()
except Error as error:                     
    label_resultado.config(text=f"No se pudo conectar con MySQL: {error}", fg="red")

root.mainloop()                            