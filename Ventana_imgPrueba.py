from argparse import Namespace
from ast import Lambda
from tokenize import Name
from PIL import Image, ImageTk
import sys
import random
import os
import tkinter
from tkinter import Canvas, StringVar

try:
    img = Image.open("Alice1.png")
except:
    print("No se pudo cargar la imagen")
    sys.exit(1)

#img.show()

ventana = tkinter.Tk()
ventana.geometry("500x600")
ventana.title("Alice")

size =(300,300)
img4 = img.copy()
img4.thumbnail(size) #Mantiene el aspecto, esta es la chida pa reescalar

def TextodeCaja():
    texto1 = CajaTexto.get()
    # TextoAlice["text"] = texto1 #Recibe texto y lo manda al label TextAlice
    # INFORMACION ------------------------------------------------------------------------
    if texto1 == "hola":
        TextoAlice["text"] = "Hola"
    if texto1 == "que puedes hacer" or texto1 == "que puedes hacer?" or texto1 == "help?":
        TextoAlice["text"] = "Puedo ayudarte en tus tareas, abrir programas o puedes preguntarme cosas \n Puedes probar diciendome que abra un programa"
    if texto1 == "como te llamas" or texto1 == "como te llamas?":
        TextoAlice["text"] = "Mi nombre es alice"
    if texto1 == "cuantos años tienes" or texto1 == "cuantos años tienes?":
        TextoAlice["text"] = "No estoy segura pero yo diria que naci ayer"
    if texto1 == "adios":
        TextoAlice["text"] = "Adios"
        quit()
    # EXTRAS ----------------------------------------------------------------------------
    if texto1 == "random":
        Max = int(input("Hasta que numero? "))
        n = random.randint(1,Max)
        TextoAlice["text"] = n
    if  texto1 == "fruta":
        frutas = ['peras','manzanas','plátanos','ciruelas','sandias','melones','naranjas','toronjas','kiwis','mangos']
        for i in range(1):
           TextoAlice["text"] = random.choice(frutas)
    if  texto1 == "chiste":
        chiste = ['Chiste1','Chiste2','Chiste3','Chiste4','Chiste5','Chiste6','Chiste7','Chiste8','Chiste9','Chiste10']
        for i in range(1):
            TextoAlice["text"] = random.choice(chiste)
    if texto1 == "hazme una nota":
        nota = input("Claro, ¿Que quieres que diga? ")
        TextoAlice["text"] = "Ok, tu nota es: "+ nota
    if texto1 == "cuenta":
        Max = int(input("Hasta que numero? "))
        for i in range(Max):
            TextoAlice["text"] = i+1
    # PROGRAMAS ---------------------------------------------------------------------------
    if texto1 == "notepad" or texto1 == "abre notepad":
        os.system('notepad.exe')
    if texto1 == "word" or texto1 == "abre word":
        TextoAlice["text"] = "Con gusto"
        os.system('start winword')
        quit()
    if texto1 == "excel"or texto1 == "abre excel":
        TextoAlice["text"] = "Con gusto"
        os.system('start excel')
        quit()
    if texto1 == "powerpoint"or texto1 == "abre powerpoint":
        TextoAlice["text"] = "Con gusto"
        os.system('start powerpnt')
        quit()
    if texto1 == "paint"or texto1 == "abre paint":
        TextoAlice["text"] = "Con gusto"
        os.system('start pbrush')
        quit()

def salir():
    quit()


img1 = ImageTk.PhotoImage(img4)
lbl_img = tkinter.Label(ventana, image= img1)
NameA = tkinter.Label(ventana,text =" ALICE ",font=("COMIC Sans MS",15))
TextoAlice = tkinter.Label(ventana,text= "BIENVENIDO")
CajaTexto = tkinter.Entry(ventana)
boton1 = tkinter.Button(ventana, text="Aceptar", command=TextodeCaja)

lbl_img.pack()
NameA.pack()
TextoAlice.pack(fill=tkinter.X)
CajaTexto.pack(fill=tkinter.X)
boton1.pack(fill=tkinter.X)


ventana.mainloop()


