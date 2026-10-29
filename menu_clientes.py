import mysql.connector                 # Librería para conectar Python con MySQL
from mysql.connector import Error      # Para capturar errores de MySQL


def conectar():                        # Crea y devuelve una conexión a practica_tienda
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="practica_tienda"
    )


def insertar():                        # INSERT: añade un cliente nuevo
    nombre = input("Nombre: ")         # input() pide el dato por teclado (siempre llega como texto)
    ciudad = input("Ciudad: ")
    edad = int(input("Edad: "))        # int() convierte el texto a número entero
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO clientes (nombre, ciudad, edad) VALUES (%s, %s, %s)",
        (nombre, ciudad, edad)
    )
    conexion.commit()                  # Guarda el cambio
    print("Cliente insertado correctamente")
    cursor.close()
    conexion.close()


def listar():                          # SELECT: muestra todos los clientes
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    filas = cursor.fetchall()          # Lista de tuplas con todas las filas
    print("--- LISTA DE CLIENTES ---")
    for fila in filas:
        print(f"{fila[0]} - {fila[1]} - {fila[2]} - {fila[3]} años")
    print(f"Total: {len(filas)} clientes")
    cursor.close()
    conexion.close()


def actualizar():                      # UPDATE: cambia la ciudad de un cliente
    id_cliente = int(input("ID del cliente a actualizar: "))
    ciudad = input("Nueva ciudad: ")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE clientes SET ciudad = %s WHERE id = %s",
        (ciudad, id_cliente)
    )
    conexion.commit()
    print(f"{cursor.rowcount} fila(s) actualizada(s)")   # 0 = no existe ese ID
    cursor.close()
    conexion.close()


def borrar():                          # DELETE: borra un cliente por su ID
    id_cliente = int(input("ID del cliente a borrar: "))
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
    conexion.commit()
    print(f"{cursor.rowcount} fila(s) borrada(s)")
    cursor.close()
    conexion.close()


# ---------- PROGRAMA PRINCIPAL ----------
while True:                            # Bucle infinito: el menú se repite hasta elegir salir
    print("\n===== MENÚ CLIENTES =====")
    print("1. Insertar cliente")
    print("2. Listar clientes")
    print("3. Actualizar ciudad")
    print("4. Borrar cliente")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    try:                               # Captura cualquier fallo sin cerrar el programa
        if opcion == "1":
            insertar()
        elif opcion == "2":
            listar()
        elif opcion == "3":
            actualizar()
        elif opcion == "4":
            borrar()
        elif opcion == "5":
            print("¡Hasta luego!")
            break                      # break sale del bucle y termina el programa
        else:
            print("Opción no válida")
    except Error as error:             # Errores de MySQL
        print(f"Error de base de datos: {error}")
    except ValueError:                 # Si escribes letras donde va un número
        print("Error: escribe un número válido")