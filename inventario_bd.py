import sqlite3

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventario (
        nombre TEXT PRIMARY KEY,
        stock INTEGER NOT NULL
    )
""")

conexion.commit()
opcion = ""
while opcion != "6":
    print()
    print("1. Mostrar inventario")
    print("2. Añadir videojuego")
    print("3. Vender videojuego")
    print("4. Reponer stock")
    print("5. Buscar videojuego")
    print("6. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        cursor.execute("SELECT nombre, stock FROM inventario")
        juegos = cursor.fetchall()
        if len(juegos) == 0:
            print("El inventario esta vacio.")
        else:
            for nombre, stock in juegos:
                print(nombre, "->", stock, "unidades")
    elif opcion == "2":
        nombre = input("Nombre del videojujego: ")
        cantidad = int(input("Cantidad inicial: "))
        cursor.execute("SELECT stock FROM  inventario WHERE nombre = ?",(nombre,) )
        resultado =cursor.fetchone()
        if resultado is not None:
            print("Ese video juego ya existe en el inventario.")
        else:
            cursor.execute("INSERT INTO inventario (nombre,stock) VALUES (?,?)", (nombre, cantidad))
            conexion.commit()
            print("Videojuego añadido correctamente")
    elif opcion == "3":
        nombre = input("Nombre del videojuego: ")
        cantidad = int(input("Cantidad a vender: "))
        cursor.execute("SELECT stock FROM inventario WHERE nombre = ?", (nombre,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Ese videojuego no existe en el inventario.")
        elif cantidad > resultado[0]:
            print("No hay suficientes unidades disponibles.")
        else:
            cursor.execute("UPDATE inventario SET stock = stock - ? WHERE nombre = ?", (cantidad, nombre))
            conexion.commit()
            print("Venta realizada correctamente.")
    elif opcion == "4":
        nombre = input("Nombre del videojuego: ")
        cursor.execute("SELECT stock FROM inventario WHERE nombre = ?", (nombre,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Ese videojuego no existe en el inventario.")
        else:
            cantidad = int(input("¿Cuántas unidades quieres añadir? "))
            cursor.execute("UPDATE inventario SET stock = stock + ? WHERE nombre = ?", (cantidad, nombre))
            conexion.commit()
            print("Stock actualizado correctamente.")
    elif opcion == "5":
        nombre = input("Nombre del videojuego: ")
        cursor.execute("SELECT stock FROM inventario WHERE nombre = ?", (nombre,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Ese videojuego no existe en el inventario.")
        else:
            print(nombre, "tiene", resultado[0], "unidades disponibles.")
    elif opcion == "6":
        print("Saliendo del programa.")
    else:
        print("Opcion no valida. Elige un numero del 1 al 6.")
conexion.close()
