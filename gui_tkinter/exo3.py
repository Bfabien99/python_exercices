from tkinter import *
import random

# cercle pour les différents pions
def cercle(x, y, r):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="red")

# carré representant le damier
def carre(x1, y1, x2,color="blue"):
    "tracé d'un rectangle"
    can.create_rectangle(x1, y1, x2, y1+20, outline="black", fill=color)

# dessiner les pions
def draw_circle():
    "Ajouter les pions sur le damier"
    # on redessine le damier
    draw_dam()
    
    # initialise le nombre de pion à zéro
    pion = 0
    # ajout d'une limit au nombre de pion sur le plateau
    limit = random.randint(1,61)
    
    # Pour i representant la position y
    for i in range(0, 181, 20):
        # Pour j representant la position x
        for j in range(0, 181, 20):
            # f pour savoir s'il faut générer un pion ou pas
            f = random.randint(0,1)
            # s'il faut générer un pion et que la limite n'est pas atteinte
            # on génère le pions
            if f and pion < limit:
                cercle(j+10, i+10, 5)
                pion += 1
    print("Il y a", pion,"pion(s) sur le damier.")

# dessiner damier
def draw_dam():
    "Afficher le damier"
    # pour alterner la couleur des rectangle
    b = True
    
    # Pour i representant la position y
    for i in range(0, 181, 20):
        # Pour j representant la position x
        for j in range(0, 181, 20):
            # si b est vrai alors la couleur est bleue
            if b:
                carre(j, i, j+20)
            else:
                # sinon la couleur est ivoire
                carre(j, i, j+20, "ivory")
            b = not b
            #print(f"x1 (j) = {j}, y1 (i) = {i}, x2 (j+20) = {j+20}")

# création de la fenêtre
fen = Tk()

# création du canvas
can = Canvas(fen, width =200, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)

# création du boutton pour afficher le damier
btn_square = Button(fen, text="Damier", command=draw_dam)
btn_square.pack(side=LEFT)

# création du boutton pour afficher les pions
btn_circle = Button(fen, text="Pions", command=draw_circle)
btn_circle.pack(side=RIGHT)

fen.mainloop()