import math

#  Écrivez un programme qui calcule le périmètre et l’aire d’un triangle quelconque dont l’utilisateur fournit les 3 côtés (en cm).
a = float(input("Entrer la longueur du coté a : "))
b = float(input("Entrer la longueur du coté b : "))
c = float(input("Entrer la longueur du coté c : "))

# calcule du périmètre
P = a + b + c
# déductions du démi-perimètre
d = round(P / 2, 2)

# calcule de l'air
S = round(math.sqrt(d*(d-a)*(d-b)*(d-c)), 2)

print("Le périmètre de ce triangle est P =", P, "cm et son aire est S =", S, "cm2")