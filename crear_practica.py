import mysql.connector
from mysql.connector import Error

conexion = None
cursor = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306
    )
    cursor = conexion.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS practica_tienda")
    cursor.execute("USE practica_tienda")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            ciudad VARCHAR(50),
            edad INT
            )
    """)

    print("¡Base practica_tioenda y tabla clientes listas!")

except Error as error:
    print(f"Se ha producido un error: {error}")

finally:
    if cursor is not None:
        cursor.close()
    if conexion is not None and conexion.is_connected():
        conexion.close()