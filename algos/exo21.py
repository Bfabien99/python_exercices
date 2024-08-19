import math
'''
Écrivez un programme qui calcule la période d’un pendule simple de longueur donnée.
La formule qui permet de calculer la période d’un pendule simple est T=2pi*sqrt(l/g),
l représentant la longueur du pendule et g la valeur de l’accélération de la pesanteur au lieu d’expérience.
'''
# accélération de la pesanteur de la terre
g = 9.8

l=float(input("Entrer la longueur : "))

# calcule de la période
T = round(2 * math.pi * math.sqrt(l/g), 2)

print("La période T est", T, "seconde(s)")