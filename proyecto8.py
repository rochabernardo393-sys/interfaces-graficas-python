from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import sqlite3

conexion = None


def conectar():
    global conexion
    try:
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                genero TEXT,
                anio INTEGER,
                disponible INTEGER DEFAULT 1
            )
        """)
        conexion.commit()
        cursor.close()
        return True
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"No se pudo conectar con la base de datos:\n{error}")
        return False


def mostrar_en_tabla(filas):
    for item in tabla.get_children():
        tabla.delete(item)
    for fila in filas:
        estado = "Disponible" if fila[5] == 1 else "Prestado"
        anio = fila[4] if fila[4] is not None else ""
        tabla.insert("", END, values=(fila[0], fila[1], fila[2], fila[3] or "", anio, estado))


def listar():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, titulo, autor, genero, anio, disponible FROM libros")
        filas = cursor.fetchall()
        cursor.close()
        mostrar_en_tabla(filas)
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"No se pudo leer la base de datos:\n{error}")


def buscar():
    titulo = simpledialog.askstring("Buscar libro", "Título (o parte del título):", parent=root)
    if titulo is None or titulo.strip() == "":
        return
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, titulo, autor, genero, anio, disponible FROM libros WHERE titulo LIKE ?",
            (f"%{titulo.strip()}%",)
        )
        filas = cursor.fetchall()
        cursor.close()
        if len(filas) == 0:
            messagebox.showinfo("Buscar", "No se encontraron libros con ese título.")
        else:
            mostrar_en_tabla(filas)
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"No se pudo realizar la búsqueda:\n{error}")


def abrir_formulario():
    ventana = Toplevel(root)
    ventana.title("Añadir libro")
    ventana.geometry("320x330")
    ventana.grab_set()

    Label(ventana, text="Título:").pack(pady=(10, 0))
    entry_titulo = Entry(ventana, width=35)
    entry_titulo.pack()

    Label(ventana, text="Autor:").pack(pady=(10, 0))
    entry_autor = Entry(ventana, width=35)
    entry_autor.pack()

    Label(ventana, text="Género:").pack(pady=(10, 0))
    entry_genero = Entry(ventana, width=35)
    entry_genero.pack()

    Label(ventana, text="Año de publicación:").pack(pady=(10, 0))
    entry_anio = Entry(ventana, width=35)
    entry_anio.pack()

    var_disponible = IntVar(value=1)
    Checkbutton(ventana, text="Disponible", variable=var_disponible).pack(pady=10)

    def guardar():
        titulo = entry_titulo.get().strip()
        autor = entry_autor.get().strip()
        genero = entry_genero.get().strip()
        anio_texto = entry_anio.get().strip()

        if titulo == "" or autor == "":
            messagebox.showwarning("Datos incompletos", "El título y el autor son obligatorios.", parent=ventana)
            return

        if anio_texto == "":
            anio = None
        elif anio_texto.isdigit():
            anio = int(anio_texto)
        else:
            messagebox.showwarning("Año no válido", "El año debe ser un número entero.", parent=ventana)
            return

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO libros (titulo, autor, genero, anio, disponible) VALUES (?, ?, ?, ?, ?)",
                (titulo, autor, genero, anio, var_disponible.get())
            )
            conexion.commit()
            cursor.close()
            messagebox.showinfo("Libro guardado", f"'{titulo}' se guardó correctamente.", parent=ventana)
            ventana.destroy()
            listar()
        except sqlite3.Error as error:
            messagebox.showerror("Error", f"No se pudo guardar el libro:\n{error}", parent=ventana)

    Button(ventana, text="Guardar", command=guardar).pack(pady=5)
    Button(ventana, text="Cancelar", command=ventana.destroy).pack()


def borrar():
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Borrar", "Selecciona primero un libro de la lista.")
        return

    valores = tabla.item(seleccion[0], "values")
    id_libro = int(valores[0])
    titulo = valores[1]

    if not messagebox.askyesno("Confirmar borrado", f"¿Seguro que quieres borrar '{titulo}'?"):
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
        conexion.commit()
        cursor.close()
        tabla.delete(seleccion[0])
        messagebox.showinfo("Borrar", "Libro eliminado correctamente.")
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"No se pudo borrar el libro:\n{error}")


def salir():
    if messagebox.askyesno("Salir", "¿Seguro que quieres salir?"):
        if conexion is not None:
            conexion.close()
        root.destroy()


root = Tk()
root.title("Biblioteca")
root.geometry("720x400")
root.protocol("WM_DELETE_WINDOW", salir)

menubar = Menu(root)
root.config(menu=menubar)

menu_archivo = Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Salir", command=salir)

menu_libros = Menu(menubar, tearoff=0)
menu_libros.add_command(label="Añadir libro", command=abrir_formulario)
menu_libros.add_command(label="Listar todos", command=listar)
menu_libros.add_command(label="Buscar por título", command=buscar)
menu_libros.add_separator()
menu_libros.add_command(label="Borrar seleccionado", command=borrar)

menubar.add_cascade(label="Archivo", menu=menu_archivo)
menubar.add_cascade(label="Libros", menu=menu_libros)

marco = Frame(root)
marco.pack(fill=BOTH, expand=True, padx=10, pady=10)

columnas = ("id", "titulo", "autor", "genero", "anio", "estado")
tabla = ttk.Treeview(marco, columns=columnas, show="headings")
tabla.heading("id", text="ID")
tabla.heading("titulo", text="Título")
tabla.heading("autor", text="Autor")
tabla.heading("genero", text="Género")
tabla.heading("anio", text="Año")
tabla.heading("estado", text="Estado")
tabla.column("id", width=40)
tabla.column("titulo", width=200)
tabla.column("autor", width=150)
tabla.column("genero", width=100)
tabla.column("anio", width=60)
tabla.column("estado", width=90)

scroll = Scrollbar(marco, command=tabla.yview)
tabla.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
tabla.pack(side=LEFT, fill=BOTH, expand=True)

if conectar():
    listar()
    root.mainloop()
else:
    root.destroy()
