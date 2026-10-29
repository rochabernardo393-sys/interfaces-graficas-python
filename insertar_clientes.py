import mysql.connector
from mysql.connector import Error

conexion = None
cursor = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="practica_tienda"
    )
    cursor = conexion.cursor()

    sql = "INSERT INTO clientes (nombre, ciudad, edad) VALUES (%s, %s, %s)"
    clientes = [
        ("Lucia", "Madrid", 34),
        ("Carlos", "Lima", 28),
        ("Maria", "Caracas", 41),
    ]

    cursor.executemany(sql, clientes)
    conexion.commit()

    print(f"{cursor.rowcount} clientes insertados correctamente")

except Error as error:
    print(f"Se ha producido un error: {error}")

finally:
    if cursor is not None:
        cursor.close()
    if conexion is not None and conexion.is_connected():
        conexion.close()