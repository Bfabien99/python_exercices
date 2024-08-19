'''
Convertir une note scolaire N quelconque, entrée par l’utilisateur sous forme de points (par exemple 27 sur 85), en une note standardisée suivant le code suivant :
Note Appréciation
N >= 80 % A
80 % > N >= 60 % B
60 % > N >= 50 % C
50 % > N >= 40 % D
N < 40 % E
'''
note = float(input("Quelle note avez vous obtenue : "))
total = int(input("Quel est le total : "))

# Deduction des notes en fonction du pourcentage donné
A = round(80 * total / 100, 2)
B = round(60 * total / 100, 2)
C = round(50 * total / 100, 2)
D = round(40 * total / 100, 2)
N = round(note * 100 / total, 2)

#############################
print("80% en note = ", A)
print("60% en note = ", B)
print("50% en note = ", C)
print("40% en note = ", D)
print("Note obtenue", note, "en pourcentage = ", N,"%")
#############################

# Affichage l'appréciation correspondante
if note >= A:
    print("Vous avez la note A, c'est bien")
elif note < A and note >= B:
    print("Vous avez la note B, c'est assez bien")
elif note < B and note >= C:    
    print("Vous avez la note C, c'est passable")
elif note < C and note >= D:
    print("Vous avez la note D, peu mieux faire...")
else:
    print("Vous avez la note E, o-o")
    