# Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13, mais n’affiche que ceux qui sont des multiples de 7.
i = 1
while i <= 50:
    prod = i*13
    if(prod)%7 == 0:
        print(prod)
    i+=1