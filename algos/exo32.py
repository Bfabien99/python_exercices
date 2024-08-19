import math
'''
Définissez une fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca.
'''
def ligneCar(n, ca):
    print(f"{ca}"*n)

'''
Définissez une fonction surfCercle(R). Cette fonction doit renvoyer la surface (l’aire) d’un cercle dont on lui a fourni le rayon R en argument. Par exemple, l’exécution de l’instruction :
print surfCercle(2.5) doit donner le résultat 19.635.
'''
def surfCercle(R):
    #print("La surface d'un cercle de rayon R =", R, "est :", round(math.pi * R**2, 3))
    return round(math.pi * R**2, 3)

'''
Définissez une fonction volBoite(x1,x2,x3) qui renvoie le volume d’une boîte parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments.
Par exemple, l’exécution de l’instruction :
print volBoite(5.2, 7.7, 3.3) doit donner le résultat : 132.13.
'''
def volBoite(x1, x2, x3):
    #print("Le volume V = L x l x h, V =", round(x1*x2*x3, 2))
    return round(x1*x2*x3, 2)

'''
Définissez une fonction maximum(n1,n2,n3) qui renvoie le plus grand de 3 nombres n1, n2, n3 fournis en arguments. Par exemple, l’exécution de l’instruction :
print maximum(2,5,4) doit donner le résultat : 5.
'''
def maximum(n1, n2, n3):
    a, b, c = n1, n2, n3
    if a > b and a > c:
        return a
    
    if b > a and b > c:
        return b
    else:
        return c
    