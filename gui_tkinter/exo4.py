# Détection et positionnement d'un clic de souris dans une fenêtre :
from tkinter import *

def cercle(x, y, r):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    cadre.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="white")
    
def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) + ", Y =" + str(event.y))
    cercle(event.x, event.y, 1)
    
fen = Tk()
cadre = Canvas(fen, width =300, height =300, bg="black")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()