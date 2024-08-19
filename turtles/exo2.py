'''
Ajoutez au module de l’exercice précédent une fonction etoile5() spécialisée dans le dessin 
d’étoiles à 5 branches. Dans votre programme principal, insérez une boucle qui dessine une 
rangée horizontale de de 9 petites étoiles de tailles variées
'''
from turtle import *
def etoile5(taille):
    i = 0
    color("red")
    while i < 5:
        forward(taille)
        right(144)
        i += 1

i = 0
taille = 10
x = 0
while i <= 10:
    color("")
    goto(x, 0)
    etoile5(taille)
    x += taille + 5
    if i >= 5:
        taille -= 5
    else:
        taille += 5
    
    i += 1