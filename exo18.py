'''
Écrivez un programme qui analyse un par un tous les éléments d’une liste de mots (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']) pour générer deux nouvelles listes. L’une contiendra les mots comportant moins de 6 caractères, l’autre les mots comportant 6 caractères ou davantage.
'''
noms = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
t1 = []
t2 = []

for i in noms:
    if len(i) < 6:
        t1.append(i)
    else:
        t2.append(i)

print(t1)
print(t2)