from tkinter import *

root = Tk()
root.title('My Window')
root.geometry('500x400')

canvas = Canvas(root, bg = 'green', height = 200, width = 500)
image_file = PhotoImage(file = 'Alice2.png')
image = canvas.create_image(250, 0, anchor = 'n', image = image_file)

x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0 - 50, y0 - 50, x1 - 50, y1 - 50)  # Dibuja una línea recta
oval = canvas.create_oval(x0 + 120, y0 + 50, x1 + 120, y1 + 50, fill='yellow')  # Dibuja un círculo y rellénalo de amarillo
arc = canvas.create_arc(x0, y0 + 50, x1, y1 + 50, start=0, extent=180)  # Dibuja una forma de abanico de 0 grados a 180 grados hasta el final
rect = canvas.create_rectangle(330, 30, 330 + 20, 30 + 20)  # Dibujar un rectángulo cuadrado
canvas.pack()

def moveit():
    canvas.move(rect, 2, 2)  # Mueva el rectángulo cuadrado (también puede cambiar el nombre de otros gráficos para mover los gráficos y los elementos juntos), y moverse por cada paso (x = 2, y = 2)
def moveit1():
    canvas.move(oval, 2, 2)
def moveit2():
    canvas.move(line, 2, 2)

cu = Button(root, text = 'move cuadrado', command = moveit).pack()
ci = Button(root, text = 'move circulo', command = moveit1).pack()
li = Button(root, text = 'move linea', command = moveit2).pack()

root.mainloop()