'''
Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :
le plus grand élément de cette liste a la valeur 75.
'''
liste = [32, 5, 12, 8, 3, 75, 2, 15]

a = liste[0]
for i in liste:
    if i > a:
        a = i
print("le plus grand élément de cette liste a la valeur", a)