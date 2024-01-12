from tkinter import *

root = Tk()
root.title('My Window')
root.geometry('500x500')

canvas = Canvas(root, bg = 'green', height = 200, width = 500)
# image_file = PhotoImage(file = 'Hilda1.png')
# image = canvas.create_image(250, 0, anchor = 'n', image = image_file)

x0, y0, x1, y1 = 100, 100, 150, 150
oval = canvas.create_oval(x0 + 120, y0 + 50, x1 + 120, y1 + 50, fill='yellow')  # Dibuja un círculo y rellénalo de amarillo
canvas.pack()

def moveup():
    canvas.move(oval, 0, -2)  # Mueva el rectángulo cuadrado (también puede cambiar el nombre de otros gráficos para mover los gráficos y los elementos juntos), y moverse por cada paso (x = 2, y = 2)
def movedown():
    canvas.move(oval, 0, 2)
def moveleft():
    canvas.move(oval, 2, 0)
def moveright():
    canvas.move(oval, -2, 0)

cu = Button(root, text = 'move arriba', command = moveup).pack()
ci = Button(root, text = 'move abajo', command = movedown).pack()
li = Button(root, text = 'move izquierda', command = moveright).pack()
li = Button(root, text = 'move derecha', command = moveleft).pack()

root.mainloop()