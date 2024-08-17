# Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3.
# Exemple : 7 14 21 * 28 35 42 * 49
i = 1
while i <= 20:
    prod = i*7
    if(prod)%3 == 0:
        print(prod, "*", end=" ")
    else:
        print(prod, end=" ")
    i+=1