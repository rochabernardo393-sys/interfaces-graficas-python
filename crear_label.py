from tkinter import *
root =Tk()
root.title("Boton")
root.resizable(1,1)
root.geometry("500x400")
def crearLabel():
    Label(root,text="Label creado").pack()


boton=Button(root,text="Pulsar" ,command=crearLabel)
boton.pack()


root.mainloop()