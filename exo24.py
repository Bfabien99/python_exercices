'''
Déterminer si une année (dont le millésime est introduit par l’utilisateur) est bissextile ou non. 
Une année A est bissextile si A est divisible par 4. Elle ne l’est cependant pas si A est un multiple de 100, à moins que A ne soit multiple de 400.
'''
A = int(input("Entrer l'année à vérifier : "))

if A % 4 == 0:
    if (A % 100 == 0) and (A % 400 == 0):
        print(A, "est une année bissextile!")
    else:
        print(A, "n'est pas une année bissextile!")
else:
    print(A, "n'est pas une année bissextile!")