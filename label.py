from tkinter import *
root=Tk()
root.title("Labels")
root.resizable(1,1)
root.geometry("500x400")

"""
frame=Frame(root,width=480,height=320)
frame.pack()

label=Label(frame,text="Hoy es Martes")
#label.pack()
# por defecto la ventana se ajusta al tamaño de el label 
label.place(x=100, y=100)
"""



Label(root,text="Hola mundo").pack(anchor='nw')

label=Label(root,text="Otra etiqueta")
label.pack(anchor='center')

Label(root,text="Ultima etiqueta").pack(anchor='se')
label.config(bg='green',fg='yellow',font=('Arial',24))



root.mainloop()