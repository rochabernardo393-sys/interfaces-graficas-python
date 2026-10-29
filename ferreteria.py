from tkinter import *



def abrir_ventana_insertar():
    ventana_insertar=Toplevel(root)
    ventana_insertar.title("Insertar producto")
    ventana_insertar.geometry("300x200")

    Label(
        ventana_insertar,
        text="¡Hola! esta es la ventana insertar"
    ).pack(pady=30)

root=Tk()
menubar=Menu(root)
root.config(menu=menubar)

bd=Menu(menubar,tearoff=0)
bd.add_command(label="Conectar")
bd.add_command(label="Desconectar")
bd.add_separator()
bd.add_command(label="Salir",command=root.quit)

ins=Menu(menubar,tearoff=0)
ins.add_command(label="Insertar un nuevo producto")

bus=Menu(menubar,tearoff=0)
bus.add_command(label="Buscar producto por nombre")


menubar.add_cascade(label="Base de Datos",menu=bd)
menubar.add_cascade(label="Insertar",menu=ins)
menubar.add_cascade(label="Buscar",menu=bus)

root.mainloop()