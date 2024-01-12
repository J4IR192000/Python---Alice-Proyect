import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x300")
ventana.title("ESTE ES EL TITULO")
ventana.resizable(0,0)

cabezera = tk.Label(ventana,text =" Esta es la cabezera ").pack()
text = tk.Label(ventana, 
text="HOLA \n MUNDO",
font=("COMIC Sans MS",20)
)
text.place(relx=0.5, rely=0.5, 
anchor='center')

ventana.mainloop()