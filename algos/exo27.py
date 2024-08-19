'''
Demander à l’utilisateur qu’il entre un nombre. Afficher ensuite : soit la racine carrée de ce nombre, soit un message indiquant que la racine carrée de ce nombre ne peut être calculée.
'''
import math

nb = int(input("Entrer un nombre : "))

if nb < 0:
    print("La racine carrée de ce nombre n'existe pas!")
else:
    print("La racine carrée de", nb, "est", math.sqrt(nb))