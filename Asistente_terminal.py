import random
import os
import tkinter as tk


print("Hola")

for Respuesta in "adios":
    
    Respuesta = input("¡En que puedo ayudarte? ")

# INFORMACION ------------------------------------------------------------------------
    if Respuesta == "hola":
        print("Hola")
    if Respuesta == "que puedes hacer" or Respuesta == "que puedes hacer?" or Respuesta == "help?":
        print("Puedo ayudarte en tus tareas, abrir programas o puedes preguntarme cosas")
        print("Puedes probar diciendome que abra un programa")
    if Respuesta == "como te llamas" or Respuesta == "como te llamas?":
        print("Mi nombre es alice")
    if Respuesta == "adios":
        print("Adios")
        quit()
# EXTRAS ----------------------------------------------------------------------------
    if Respuesta == "random":
        Max = int(input("Hasta que numero? "))
        n = random.randint(1,Max)
        print(n)
    if  Respuesta == "fruta":
        frutas = ['peras','manzanas','plátanos','ciruelas','sandias','melones','naranjas','toronjas','kiwis','mangos']
        for i in range(1):
            print(random.choice(frutas))
    if  Respuesta == "chiste":
        chiste = ['Chiste1','Chiste2','Chiste3','Chiste4','Chiste5','Chiste6','Chiste7','Chiste8','Chiste9','Chiste10']
        for i in range(1):
            print(random.choice(chiste))
    if Respuesta == "hazme una nota":
        nota = input("Que quieres que guarde? ")
        print("Ok, tu nota es: "+nota)
    if Respuesta == "cuenta":
        Max = int(input("Hasta que numero? "))
        for i in range(Max):
            print(i+1)
# PROGRAMAS ---------------------------------------------------------------------------
    if Respuesta == "abre un programa":
        print("claro, dime el nombre del programa")
    if Respuesta == "notepad" or Respuesta == "abre notepad":
        os.system('notepad.exe')
    if Respuesta == "word" or Respuesta == "abre word":
        print("Con gusto")
        os.system('start winword')
        quit()
    if Respuesta == "excel"or Respuesta == "abre excel":
        print("Con gusto")
        os.system('start excel')
        quit()
    if Respuesta == "powerpoint"or Respuesta == "abre powerpoint":
        print("Con gusto")
        os.system('start powerpnt')
        quit()
    if Respuesta == "paint"or Respuesta == "abre paint":
        print("Con gusto")
        os.system('start pbrush')
        quit()