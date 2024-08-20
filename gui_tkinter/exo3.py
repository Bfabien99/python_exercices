from tkinter import *
import random

# cercle pour les différents pions
def cercle(x, y, r):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="red")

def carre(x1, y1, x2,color="blue"):
    can.create_rectangle(x1, y1, x2, y1+20, outline="black", fill=color)

def draw_circle():
    draw_pan()
    for i in range(0, 181, 20):
        for j in range(0, 181, 20):
            f = random.randint(0,1)
            cercle(j+10, i+10, 5) if f else None

def draw_pan():
    # x1 = 0
    # x2 = 20
    # y1 = 0
    b = True
    for i in range(0, 181, 20):
        for j in range(0, 181, 20):
            if b:
                carre(j, i, j+20)
            else:
                carre(j, i, j+20, "ivory")
            b = not b
                
fen = Tk()
can = Canvas(fen, width =200, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)

btn_square = Button(fen, text="Damier", command=draw_pan)
btn_square.pack(side=LEFT)

btn_circle = Button(fen, text="Pions", command=draw_circle)
btn_circle.pack(side=RIGHT)

fen.mainloop()