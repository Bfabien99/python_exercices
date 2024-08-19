'''
Écrire un programme qui, étant données deux bornes entières a et b, additionne les nombres multiples de 3 et de 5 compris entre ces bornes.
Prendre par exemple a = 0, b = 32 ; le résultat devrait être alors 0 + 15 + 30 = 45.
Modifier légèrement ce programme pour qu’il additionne les nombres multiples de 3 ou de 5 compris entre les bornes a et b. Avec les bornes 0 et 32, le résultat devrait donc être : 0 + 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 30 = 225.
'''

a = int(input("Entrer la valeur de la borne a : "))
b = int(input("Entrer la valeur de la borne b : "))

t1 = []
t2 = []

for i in range(a, (b+1)):
    if (i % 3 == 0) and (i % 5 == 0):
        t1.append(i)
    if (i % 3 == 0) or (i % 5 == 0):
        t2.append(i)
    else:
        print("'", i, "'")
##############################
print("Multiple de 3 et 5 dans l'interval de", a, "à", b)
i=0
while i < len(t1)-1:
    print(t1[i], "+",end=" ")
    i += 1
print(t1[-1], "=", sum(t1))
###############################
print("Multiple de 3 ou 5 dans l'interval de", a, "à", b)
i=0
while i < len(t2)-1:
    print(t2[i], "+",end=" ")
    i += 1
print(t2[-1], "=", sum(t2))
###########################