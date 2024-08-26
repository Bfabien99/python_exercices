'''
Vous disposez d’une liste de nombres entiers quelconques, certains d’entre eux étant présents 
en plusieurs exemplaires. Écrivez un script qui recopie cette liste dans une autre, en omettant 
les doublons. La liste finale devra être triée.
'''
listes = [1,9,5,4,7,4,1,4,7,8,3,4,1,6,8,1,4,5,3,6,9,8,7,4,1,0,1,3,5]

# liste sans doublons
liste = []
for i in listes:
    if i not in liste:
        liste.append(i)
print(liste)

# liste rangé dans l'ordre
ordered = []
for i in range(0, len(liste)):
    ordered.append(min(liste))
    liste.remove(min(liste))
print(ordered)