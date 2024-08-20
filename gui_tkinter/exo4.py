# Détection et positionnement d'un clic de souris dans une fenêtre :
from tkinter import *

def cercle(x, y, r):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    cadre.create_oval(x-r, y-r, x+r, y+r, fill="white")
    
def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) + ", Y =" + str(event.y))
    cercle(event.x, event.y, 1)
    
fen = Tk()
cadre = Canvas(fen, width =1000, height =1000, bg="black")
cadre.bind("<Button-1>", pointeur) # au clic
cadre.bind("<B1-Motion>", pointeur) # clic enfoncé
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()