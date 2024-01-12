from tkinter import *
import tkinter 
from PIL import ImageTk, Image #Necesitamos instalarlo con 'pip install pillow' en cmd

ventana = tkinter.Tk()
ventana.geometry("500x500")
ventana.title("ESTE ES EL TITULO")

image = Image.open("Hilda.png")
image = Image.resize((200,200), image.ANTIALIAS) #NO FUNCIONO XD

img = ImageTk.PhotoImage(image)
lbl_img = Label(ventana, image= img)
lbl_img.pack()

ventana.mainloop()