import mysql.connector 
from mysql.connector import Error

conexion = None
cursor = None

try :
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="practica_tienda"
    )
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM clientes WHERE edad > 30")
    filas = cursor.fetchall()

    print("--- LISTAS DE CLIENTES ---")

    for fila in filas:
        print(f"{fila[0]} - {fila[1]} - {fila[2]} - {fila[3]} años")

    print(f"Total: {len(filas)} clientes")

except Error as error:
    print(f"Se ha producido un error: {error}")

finally:
    if cursor is not None:
        cursor.close()
    if conexion is not None and conexion.is_connected():
        conexion.close()