#CONEXION Y CREACION DE LA BD

import sqlite3
try:
    conexion = sqlite3.connect("users.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            user VARCHAR(50) PRIMARY KEY,
            password VARCHAR(6) NOT NULL
        )
    """)

    #DATOS INICIALES
    cursor.execute(
        "INSERT OR IGNORE INTO usuarios VALUES (?, ?)",
        ("luismiguel.b@gmail.com", '123456')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO usuarios VALUES (?, ?)",
        ("alex.d@gmail.com", '333www')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO usuarios VALUES (?, ?)",
        ("marta.h@gmail.com", '565656')
    )
    conexion.commit()

    print("Base de datos creada correctamente.")

except sqlite3.Error as error:
    print("Se ha producido un error con la base de datos:", error)

finally:
    try:
        conexion.close()
    except NameError:
        pass