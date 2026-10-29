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

    sql_update = "UPDATE clientes Set ciudad = %s WHERE nombre = %s"
    cursor.execute(sql_update,("Madrid", "Carlos"))
    conexion.commit()
    print(f"{cursor.rowcount} fila(s) actualizada(s)")

    sql_delete = "DELETE FROM clientes WHERE nombre = %s"
    cursor.execute(sql_delete,("Maria",))
    conexion.commit()
    print(f"{cursor.rowcount} fila(s) borrada(s)")

except Error as error:
    print(f"Se ha producido un error: {error}")

finally:
    if cursor is not None:
        cursor.close()
    if conexion is not None and conexion.is_connected():
        conexion.close()