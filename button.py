from tkinter import *
root =Tk()
root.title("Boton")
root.resizable(1,1)
root.geometry("500x400")
def saludo():
    print("¡Hola, mundo!")


boton=Button(root,text="Pulsar" ,command=saludo)
boton.pack()


root.mainloop()