from tkinter import *
import sqlite3
def login():
    print("entra")
    conexion = sqlite3.connect('users.db')
    cursor = conexion.cursor()
    #recuperamos un registro de la tabla usuarios
    user=entry.get().strip()
    clave=entry2.get().strip()
    select=f"Select * FROM usuarios WHERE user='{user}' AND pasword='{clave}'"
    print(select)
    cursor.execute(select)
    usuario_recuperado = cursor.fetchone()
    print(usuario_recuperado)
    conexion.close()


root=Tk()
root.title("Login de usuario")
root.geometry("400x150")
root.iconbitmap("database_3_21024.ico")

#Fila 1

label=Label(root,text='Nombre')
label.grid(row=0,column=0,sticky=W,padx=5,pady=5)
entry=Entry(root,width=40)
entry.grid(row=0,column=1,padx=5,pady=5)
entry.config(justify='left' ,state='normal')

#Fila 2
label2=Label(root,text='Contraseña: ')
label2.grid(row=1,column=0,sticky=W,padx=5,pady=5)
label2.config(fg='red')

entry2=Entry(root,width=40)
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(justify='left' ,show='*')

#Fila 3
boton=Button(root,text="Entrar")
boton.grid(row=2,column=0,padx=5,pady=5)
label3=Label(root,text='Estado:    ')
label3.grid(row=2,column=1,sticky=W,padx=5,pady=5)

root.mainloop()