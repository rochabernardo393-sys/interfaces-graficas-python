from tkinter import *
root=Tk()
root.geometry("300x100")

label=Label(root,text='Nombre:')
label.grid(row=0,column=0,sticky=W,padx=5,pady=5)

entry=Entry(root)
entry.grid(row=0,column=1,padx=5,pady=5)
entry.config(justify='center' ,state='normal')

label2=Label(root,text='Contraseña:')
label2.grid(row=1,column=0,sticky=W,padx=5,pady=5)
label2.config(bg='orange')

entry2=Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(justify='center' ,show='*')

root.mainloop()


#crear un script que cree una base d edatos que tenga 22 campos usuarios
# y contraseña qu etebnga 3 usuarios 
#usuario arriba 
#contraseña abajo
#qu tenga un boton donde diga si hay algo incorrectop o que duiiga 
#si esta coorecto