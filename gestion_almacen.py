import pickle

FICHERO = "almacen.pckl"


def guardar_almacen():
    with open(FICHERO, "wb") as fichero:
        pickle.dump(productos, fichero)


def cargar_almacen():
    try:
        with open(FICHERO, "rb") as fichero:
            return pickle.load(fichero)
    except FileNotFoundError:
        return {}


def mostrar_datos(codigo):
    producto = productos[codigo]
    print("Código:", codigo)
    print("Nombre:", producto["nombre"])
    print(f"Precio: {producto['precio']:.2f} €")
    print("Unidades:", producto["unidades"])
    print("Descripción:", producto["descripcion"])


def mostrar_todos():
    if not productos:
        print("No hay productos en el almacén.")
    else:
        for codigo in productos:
            mostrar_datos(codigo)
            print("-" * 30)


def alta_producto():
    codigo = input("Código: ").strip().upper()

    if codigo in productos:
        print("Ya existe un producto con ese código.")
        return

    nombre = input("Nombre: ")

    try:
        precio = float(input("Precio: "))
        unidades = int(input("Unidades: "))
    except ValueError:
        print("El precio y las unidades deben ser números. No se ha añadido el producto.")
        return

    descripcion = input("Descripción: ")

    productos[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "unidades": unidades,
        "descripcion": descripcion
    }

    guardar_almacen()
    print("Producto añadido correctamente.")


def baja_producto():
    codigo = input("Código del producto: ").strip().upper()

    if codigo not in productos:
        print("No existe ningún producto con ese código.")
        return

    del productos[codigo]
    guardar_almacen()
    print("Producto eliminado correctamente.")


def modificar_producto():
    codigo = input("Código del producto: ").strip().upper()

    if codigo not in productos:
        print("No existe ningún producto con ese código.")
        return

    print("\n1. Modificar nombre")
    print("2. Modificar precio")
    print("3. Modificar unidades")
    print("4. Modificar descripción")
    print("5. Cancelar\n")

    eleccion = input("Elige una opción: ")

    if eleccion == "1":
        productos[codigo]["nombre"] = input("Nuevo nombre: ")
    elif eleccion == "2":
        try:
            productos[codigo]["precio"] = float(input("Nuevo precio: "))
        except ValueError:
            print("El precio debe ser un número. No se ha modificado nada.")
            return
    elif eleccion == "3":
        try:
            productos[codigo]["unidades"] = int(input("Nuevas unidades: "))
        except ValueError:
            print("Las unidades deben ser un número entero. No se ha modificado nada.")
            return
    elif eleccion == "4":
        productos[codigo]["descripcion"] = input("Nueva descripción: ")
    elif eleccion == "5":
        print("Modificación cancelada.")
        return
    else:
        print("Opción no válida.")
        return

    guardar_almacen()
    print("Producto modificado correctamente.")


def mostrar_producto():
    codigo = input("Código del producto: ").strip().upper()

    if codigo not in productos:
        print("No existe ningún producto con ese código.")
        return

    mostrar_datos(codigo)


def buscar_productos():
    texto = input("Texto a buscar en el nombre: ").strip().lower()
    encontrados = False

    for codigo, producto in productos.items():
        if texto in producto["nombre"].lower():
            mostrar_datos(codigo)
            print("-" * 30)
            encontrados = True

    if not encontrados:
        print("No se encontraron productos con ese nombre.")


# Al iniciar: cargar el almacén
print("Cargando almacén...")
productos = cargar_almacen()
print("Almacén cargado correctamente.")

opcion = ""

while opcion != "9":
    print("\n====== GESTIÓN DE ALMACÉN ======\n")
    print("1. Alta de producto")
    print("2. Baja de producto")
    print("3. Modificar producto")
    print("4. Mostrar producto")
    print("5. Mostrar todos los productos")
    print("6. Buscar productos")
    print("7. Guardar almacén")
    print("8. Cargar almacén")
    print("9. Salir\n")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        alta_producto()
    elif opcion == "2":
        baja_producto()
    elif opcion == "3":
        modificar_producto()
    elif opcion == "4":
        mostrar_producto()
    elif opcion == "5":
        mostrar_todos()
    elif opcion == "6":
        buscar_productos()
    elif opcion == "7":
        guardar_almacen()
        print("Almacén guardado correctamente.")
    elif opcion == "8":
        productos = cargar_almacen()
        print("Almacén cargado correctamente.")
    elif opcion == "9":
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Elige un número del 1 al 9.")