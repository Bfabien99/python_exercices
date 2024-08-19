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
    
def triangle(taille):
    c = 0
    while c < 3:
        color("blue")
        forward(taille)
        right(120)
        c += 1

def etoile6(taille):
    triangle(taille)
    forward(taille)
    up()
    goto(taille, -taille/2)
    down()
    right(180)
    triangle(taille)