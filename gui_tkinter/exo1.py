# Petit exercice utilisant la bibliothèque graphique Tkinter
from tkinter import *
from random import randrange
# --- définition des fonctions gestionnaires d'événements : ---
def drawline( x1, y1, x2, y2):
    "Tracé d'une ligne dans le canevas can1"
    ## 2 - modifier le programme pour que toutes les lignes tracées soient horizontales et parallèles
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    #(x1,y1) : position de départ
    #(x2,y2) : position d'arriver
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1+10

'''
## 4 - Ajoutez une fonction drawline2 qui tracera deux lignes rouges en croix au centre du canevas : 
l’une horizontale et l’autre verticale. Ajoutez également un bouton portant l’indication « viseur ». Un clic sur ce bouton devra provoquer l’affichage de la croix.
'''
def drawline2():
    '''
    ## 5 -
    Reprenez le programme initial. Remplacez la méthode create_line par create_rectangle. Que se passe-t-il ?
    '''
    can1.create_line(250,0,250,650,width=2,fill="red")
    can1.create_rectangle(50,50,150,150,width=2)
    can1.create_arc(50,50,300,300, width=2)
    can1.create_oval(100,10,250,150,width=2)

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    ## 1 - modifier le programme pour ne plus avoir que des lignes de couleur cyan, maroon et green
    pal=['cyan','maroon','green']
    c = randrange(0,3) # => génère un nombre aléatoire de 0 à 3
    coul = pal[c]

#------ Programme principal -------

# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 =  10, 390, 390, 10 # coordonnées de la ligne

coul = 'dark green' # couleur de la ligne

# Création du widget principal ("maître") :
fen1 = Tk()

# création des widgets "esclaves" :
'''
## 3 - 
Agrandissez le canevas de manière à lui donner une largeur de 500 unités et une hauteur de 650. 
Modifiez également la taille des lignes, afin que leurs extrémités se confondent avec les bords du canevas.
'''
can1 = Canvas(fen1,bg='dark grey',height=650,width=500)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
## 4 - Ajout du boutton viseur
bou4 = Button(fen1,text='Viseur',command=drawline2)
bou4.pack()
bou2 = Button(fen1,text='Tracer une ligne',command=drawline(x1, y1, x2, y2))
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()

fen1.mainloop() # démarrage du réceptionnaire d’événements
fen1.destroy() # destruction (fermeture) de la fenêtre