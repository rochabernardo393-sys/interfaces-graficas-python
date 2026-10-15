from tkinter import *
root =Tk()
root.title("Cajas de texto corto")
root.resizable(1,1)
root.geometry("500x400")
"""
entry = Entry(root)
#entry.pack()
entry.pack(side=RIGHT)
label = Label(root, text="Nombre")
label.pack(side=LEFT)

entry2 = Entry(root)
entry2.pack(side=RIGHT)

label2 = Label(root, text="Apellidos")
label2.pack(side=LEFT)
"""
""""
frame1 = Frame(root) 
frame1.pack()
entry = Entry(frame1) 
entry.pack(side=RIGHT) 
label = Label(frame1, text="Nombre") 
label.pack(side=LEFT) 
frame2 = Frame(root) 
frame2.pack() 
entry2 = Entry(frame2) 
entry2.pack(side=RIGHT) 
label2 = Label(frame2, text="Apellidos") 
label2.pack(side=LEFT)
"""
label = Label(root, text="Nombre:")
label.grid(row=0,column=0)
entry = Entry(root) 
entry.grid(row=0,column=1) 
label2 = Label(root, text="Apellidos:") 
label2.grid(row=1,column=0) 
entry2 = Entry(root) 
entry2.grid(row=1,column=1)




root.mainloop()
