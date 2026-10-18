inventario = {
    "Minecraft": 10,
    "FIFA 25": 5,
    "Zelda": 3
}

opcion = ""

while opcion != "6":

    print("\n1. Mostrar inventario")
    print("2. Añadir videojuego")
    print("3. Vender videojuego")
    print("4. Reponer stock")
    print("5. Buscar videojuego")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    # 1. Mostrar inventario
    if opcion == "1":
        for juego, cantidad in inventario.items():
            print(juego, "->", cantidad, "unidades")

    # 2. Añadir videojuego
    elif opcion == "2":
        nombre = input("Nombre del videojuego: ")
        if nombre in inventario:
            print("Ese videojuego ya existe en el inventario.")
        else:
            cantidad = int(input("Cantidad inicial: "))
            inventario[nombre] = cantidad
            print("Videojuego añadido correctamente.")

    # 3. Vender videojuego
    elif opcion == "3":
        nombre = input("Nombre del videojuego: ")
        if nombre not in inventario:
            print("Ese videojuego no existe en el inventario.")
        else:
            cantidad = int(input("Cantidad a vender: "))
            if cantidad > inventario[nombre]:
                print("No hay suficientes unidades disponibles.")
            else:
                inventario[nombre] -= cantidad
                print("Venta realizada.")

    # 4. Reponer stock
    elif opcion == "4":
        nombre = input("Nombre del videojuego: ")
        if nombre not in inventario:
            print("Ese videojuego no existe en el inventario.")
        else:
            cantidad = int(input("¿Cuántas unidades quieres añadir? "))
            inventario[nombre] += cantidad
            print("Stock actualizado.")

    # 5. Buscar videojuego
    elif opcion == "5":
        nombre = input("Nombre del videojuego: ")
        cantidad = inventario.get(nombre)
        if cantidad is None:
            print("Ese videojuego no existe en el inventario.")
        else:
            print(nombre, "tiene", cantidad, "unidades disponibles.")

    # 6. Salir
    elif opcion == "6":
        print("Saliendo del programa.")

    else:
        print("Opción no válida. Elige un número del 1 al 6.")