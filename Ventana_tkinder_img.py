import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("ESTE ES EL TITULO")

img = tk.PhotoImage(file="Alice2.png")
lbl_img= tk.Label(ventana,image=img).pack()

ventana.mainloop()