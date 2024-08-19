'''
 Demander à l’utilisateur d’entrer trois longueurs a, b, c. À l’aide de ces trois longueurs, déterminer s’il est possible de construire un triangle. Déterminer ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque. Attention : un triangle rectangle peut être isocèle.
'''
a = int(input("Entrer la longueur du côté a : "))
b = int(input("Entrer la longueur du côté b : "))
c = int(input("Entrer la longueur du côté c : "))
is_iso = False
is_rec = False
is_equ = False

if a > 0 and b > 0 and c > 0 : 
    if a == b and a == c and b == c:
        print("Ce triangle est Equilateral")
        is_equ = True
    elif a == b or a == c or b == c:
        print("Ce triangle est Isocèle")
        is_iso = True
    
    if a > b and a > c:
        if a*a == b*b + c*c:
            print("Ce triangle est rectangle")
            is_rec = True
    elif b > a and b > c:
        if b*b == a*a + c*c:
            print("Ce triangle est rectangle")
            is_rec = True
    elif c > a and c > b:
        if c*c == a*a + b*b:
            print("Ce triangle est rectangle")
            is_rec = True
    
    if not is_rec and not is_equ and not is_iso:
        print("C'est un triangle quelconque")
else:
    print("impossible de construire un triangle avec ces valeurs.")