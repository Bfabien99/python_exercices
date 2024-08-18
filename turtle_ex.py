import random
from turtle import *

forward(120)
left(90)
color('red')
forward(80)

reset()
a = 0
while a <12:
    a = a +1
    forward(150)
    left(150)
    write(a)
    color('blue')

'''
reset() => On efface tout et on recommence
goto(x, y) => Aller à l’endroit de coordonnées x, y
forward(distance) => Avancer d’une distance donnée
backward(distance) => Reculer
up() => Relever le crayon (pour pouvoir avancer sans dessiner)
down() => Abaisser le crayon (pour recommencer à dessiner)
color(couleur) => couleur peut être une chaîne prédéfinie (’red’, ’blue’, etc.)
left(angle) => Tourner à gauche d’un angle donné (exprimé en degrés)
right(angle) => Tourner à droite
width(épaisseur) => Choisir l’épaisseur du tracé
fill(1) => Remplir un contour fermé à l’aide de la couleur sélectionnée
write(texte) texte doit être une chaîne de caractères
'''