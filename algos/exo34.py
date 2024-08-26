'''
 Écrivez une fonction compteCar() qui compte le nombre d’occurrences d’un caractère donné dans une chaîne. Ainsi :
print compteCar("ananas au jus","a")
devra afficher : 4
print compteCar("Gédéon est déjà là","é")
devra afficher : 3.
'''
def compteCar(chaine: str, search: str):
    occ = 0
    for i in chaine:
        if i == search:
            occ += 1
    return occ

print(compteCar("Gédéon est déjà là","é"))