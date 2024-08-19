'''
Ajoutez au module de l’exercice précédent une fonction etoile6() capable de dessiner une étoile 
à 6 branches, elle-même constituée de deux triangles équilatéraux imbriqués. Cette nouvelle 
fonction devra faire appel à la fonction triangle() définie précédemment.
'''
from turtle import *

def etoile5(taille):
    i = 0
    color("blue")
    while i < 5:
        forward(taille)
        right(144)
        i += 1
        
def carre(taille):
    c = 0
    while c < 4:
        color("red")
        forward(taille)
        right(90)
        c += 1
    
def triangle(taille, couleur):
    c = 0
    while c < 3:
        color(couleur)
        forward(taille)
        right(120)
        c += 1

def etoile6(taille):
    triangle(taille, "red")
    forward(taille)
    right(180)
    triangle(taille, "blue")
    

taille = 20

etoile6(taille)
etoile6(taille)