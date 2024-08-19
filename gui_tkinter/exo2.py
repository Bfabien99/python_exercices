'''
a) Créez un court programme qui dessinera les 5 anneaux olympiques dans un rectangle de fond blanc (white). Un bouton « Quitter » doit permettre de fermer la fenêtre.
'''
import time
from tkinter import *

tk = Tk()

def draw_rings():
    global canva
    canva.create_oval(50, 100, 100, 150, width=5, outline="blue")
    canva.create_oval(75, 130, 125, 180, width=5, outline="yellow")
    canva.create_oval(102, 100, 152, 150, width=5, outline="black")
    canva.create_oval(127, 130, 177, 180, width=5, outline="green")
    canva.create_oval(154, 100, 204, 150, width=5, outline="red")

'''
b) Modifiez le programme ci-dessus en y ajoutant 5 boutons. Chacun de ces boutons provoquera le tracé de chacun des 5 anneaux
'''
def draw_ring_blue():
    global canva
    canva.create_oval(50, 100, 100, 150, width=5, outline="blue")

def draw_ring_yellow():
    global canva
    canva.create_oval(75, 130, 125, 180, width=5, outline="yellow")

def draw_ring_black():
    global canva
    canva.create_oval(102, 100, 152, 150, width=5, outline="black")

def draw_ring_green():
    global canva
    canva.create_oval(127, 130, 177, 180, width=5, outline="green")

def draw_ring_red():
    global canva
    canva.create_oval(154, 100, 204, 150, width=5, outline="red")


canva = Canvas(tk,  bg="white", width=250, height=300)
canva.pack()
btn_quit = Button(tk, text="quitter", bg="white", fg="red", command=quit)
btn_quit.pack()

####
## Affichage du cercle olympique
btn_all = Button(tk, text="Olympic rings", bg="pink", fg="white", command=draw_rings)
btn_all.pack()

##### Affichage des différents anneaux au clic
## affichage anneau blue
btn_blue = Button(tk, text="blue", bg="blue", fg="white", command=draw_ring_blue)
btn_blue.pack()
## affichage anneau yellow
btn_yellow = Button(tk, text="yellow", bg="yellow", fg="black", command=draw_ring_yellow)
btn_yellow.pack()
## affichage anneau black
btn_black = Button(tk, text="black", bg="black", fg="white", command=draw_ring_black)
btn_black.pack()
## affichage anneau green
btn_green = Button(tk, text="green", bg="green", fg="white", command=draw_ring_green)
btn_green.pack()
## affichage anneau red
btn_red = Button(tk, text="red", bg="red", fg="white", command=draw_ring_red)
btn_red.pack()

tk.mainloop()
tk.destroy()