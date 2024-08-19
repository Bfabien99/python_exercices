import turtle

'''
Complétez le module de fonctions graphiques dessins_tortue.py décrit à la page 60. 
Commencez par ajouter un paramètre angle à la fonction carre(), de manière à ce que les carrés 
puissent être tracés dans différentes orientations.
Définissez ensuite une fonction triangle(taille, couleur, angle) capable de dessiner un triangle équilatéral d’une taille, d’une couleur et d’une orientation bien déterminées.
Testez votre module à l’aide d’un programme qui fera appel à ces fonctions à plusieurs reprises, 
avec des arguments variés pour dessiner une série de carrés et de triangles :
'''
def carre(taille, couleur):
    c = 0
    while c < 4:
        turtle.color(couleur)
        turtle.forward(taille)
        turtle.right(90)
        c += 1
    
def triangle(taille, couleur):
    c = 0
    while c < 3:
        turtle.color(couleur)
        turtle.forward(taille)
        turtle.right(120)
        c += 1

i = 0
x = -40
taille = 20
while i < 10:
    turtle.color("")
    turtle.goto(x, 0)
    carre(taille, "red")
    x += taille + 5
    turtle.color("")
    turtle.goto(x, 0)
    triangle(taille, "blue")
    x += taille + 5
    taille += 5