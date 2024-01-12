from argparse import Namespace
from ast import Lambda
from cProfile import label
from cgitb import reset
from email.mime import image
from textwrap import fill
from tokenize import Name
from PIL import Image, ImageTk
import sys
import random
import os
import tkinter
from tkinter import Canvas, Label, PhotoImage, StringVar
import time 

try:
    img2 = Image.open("Alice2.png")
    img3 = Image.open("Alice3.png")
    img4 = Image.open("Alice4.png")
    img5 = Image.open("Alice5.png")
    #img2= Image.open("fondo.png")
    
    
except:
    print("No se pudo cargar la imagen")
    sys.exit(1)

ventana = tkinter.Tk()
ventana.geometry("500x650")
ventana.title("Alice")

size =(500,500)
img2_2 = img2.copy()
img2_2.thumbnail(size) #Mantiene el aspecto, esta es la chida pa reescalar

size =(500,500)
img3_3 = img3.copy()
img3_3.thumbnail(size) 

size =(500,500)
img4_4 = img4.copy()
img4_4.thumbnail(size) 

size =(500,500)
img5_5 = img5.copy()
img5_5.thumbnail(size) 

def TextodeCaja():
    texto1 = CajaTexto.get()
    # TextoAlice["text"] = texto1 #Recibe texto y lo manda al label TextAlice
    # INFORMACION ------------------------------------------------------------------------
    if texto1 == "hola":
        TextoAlice["text"] = "Hola"
    if texto1 == "que puedes hacer" or texto1 == "que puedes hacer?" or texto1 == "help?" or texto1 == "help":
        TextoAlice["text"] = "Puedo ayudarte en tus tareas, abrir programas o \n puedes preguntarme cosas. \n Puedes probar diciendome que abra un programa"
    if texto1 == "como te llamas" or texto1 == "como te llamas?":
        TextoAlice["text"] = "Mi nombre es Alicia"
    if texto1 == "cuantos años tienes" or texto1 == "cuantos años tienes?":
        TextoAlice["text"] = "No estoy segura pero yo diria que naci ayer"
    if texto1 == "adios" or texto1 == "nos vemos":
        TextoAlice["text"] = "Adios"
        quit()
    if texto1 == "gracias" or texto1 == "Gracias":
        TextoAlice["text"] = "Por nada, es un gusto poder ayudarte"
    if texto1 == "" or texto1 == "":
        TextoAlice["text"] = "Por favor escribe algo :)"
    if texto1 == "ropa" or texto1 == "nos vemos":
        TextoAlice["text"] = "Ok"
        ropa = [lbl_img2.pack(),lbl_img3.pack(),lbl_img4.pack(),lbl_img5.pack()]
        for i in range(1):
            random.choice(ropa)
    # EXTRAS ----------------------------------------------------------------------------
    if texto1 == "random":
        TextoAlice["text"] = "¿Hasta que numero lo quieres?"

        Max = int(texto1)
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
    if texto1 == "explorador de archivos"or texto1 == "abre el explorador de archivos":
        TextoAlice["text"] = "Con gusto"
        os.system('start explorer')
        quit()
    if texto1 == "administrador de tareas"or texto1 == "abre el administrador de tareas":
        TextoAlice["text"] = "Con gusto"
        os.system('start taskmgr')
        quit()
#img3 = ImageTk.PhotoImage(img2)
#fondo= tkinter.Label(ventana, image= img3)
img2_22 = ImageTk.PhotoImage(img2_2)
lbl_img2 = tkinter.Label(ventana, image= img2_22)

img3_33 = ImageTk.PhotoImage(img3_3)
lbl_img3 = tkinter.Label(ventana, image= img3_33)

img4_44 = ImageTk.PhotoImage(img4_4)
lbl_img4 = tkinter.Label(ventana, image= img4_44)

img5_55 = ImageTk.PhotoImage(img5_5)
lbl_img5 = tkinter.Label(ventana, image= img5_55)

NameA = tkinter.Label(ventana,text =" ALICE ",font=("COMIC Sans MS",15))
TextoAlice = tkinter.Label(ventana,text= "BIENVENIDO",font=("Arial Black",10), pady = 10)
CajaTexto = tkinter.Entry(ventana, justify='center')
boton1 = tkinter.Button(ventana, text="Aceptar", command=TextodeCaja, pady = 10)


#fondo.pack(fill = tkinter.BOTH, expand = True)
#lbl_fondo=Label(ventana,image=fondo)
#fondo = PhotoImage(file="fondo.png")
#lblFondo= Label(ventana,image=fondo).place(x=0,y=0) MOSTRAR FONDO 
#Alice = PhotoImage(file="Alice2.png")
#lbl_Alice= Label(ventana,image=Alice).place(x=150,y=100) MOSTRAR ALICE SOBRE EL FONDO PERO NO PNG
lbl_img2.pack()
TextoAlice.pack(fill=tkinter.X)
CajaTexto.pack(fill=tkinter.X)
boton1.pack(fill=tkinter.X)
    
ventana.mainloop()
