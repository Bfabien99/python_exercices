'''
Tâchez d’écrire une petite fonction trouve() qui fera exactement le contraire de ce que fait l’opé-
rateur d’indexage (c’est-à-dire les crochets [ ]). Au lieu de partir d’un index donné pour retrouver le caractère correspondant, cette fonction devra retrouver l’index correspondant à un caractère donné.
En d’autres termes, il s’agit d’écrire une fonction qui attend deux arguments : le nom de la 
chaîne à traiter et le caractère à trouver. La fonction doit fournir en retour l’index du premier 
caractère de ce type dans la chaîne. Ainsi par exemple, l’instruction :
print trouve("Juliette & Roméo", "&")
devra afficher : 9
'''
def trouve(chaine: str, search: str):
    for i in range(0, len(chaine)):
        if chaine[i] == search:
            return i
    return False

#print(trouve("Juliette & Roméo", "é"))

'''
Améliorez la fonction de l’exercice précédent en lui ajoutant un troisième paramètre : l’index à 
partir duquel la recherche doit s’effectuer dans la chaîne. Ainsi par exemple, l’instruction :
print trouve ("César & Cléopâtre", "r", 5)
devra afficher : 15 (et non 4 !).
'''
def trouve2(chaine: str, search: str, offset: int):
    if offset > (len(chaine) -1):
        return False
    for i in range(offset, len(chaine)):
        if chaine[i] == search:
            return i
    return False

print(trouve2("Juliette & Roméo", "e",5))