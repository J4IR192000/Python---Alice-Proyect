from cProfile import label
import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x600")
ventana.title("Alice")

def TextodeCaja():
    texto1 = Caja1.get() 
    Label2["text"] = texto1

Label1 = tkinter.Label(ventana,text =" ALICE ",font=("COMIC Sans MS",15))
Label2 = tkinter.Label(ventana,text= "Hola", font=("COMIC Sans MS",10))
Caja1 = tkinter.Entry(ventana)
boton1 = tkinter.Button(ventana, text="Aceptar", command=TextodeCaja)

Label1.pack()
Label2.pack()
Caja1.pack()
boton1.pack()

ventana.mainloop()
