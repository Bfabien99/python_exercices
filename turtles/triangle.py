'''
Importez le module turtle pour pouvoir effectuer des dessins simples.
Vous allez dessiner une série de triangles équilatéraux de différentes couleurs.
Pour ce faire, définissez d’abord une fonction triangle() capable de dessiner un triangle d’une couleur bien déterminée (ce qui signifie donc que la définition de votre fonction doit comporter un paramètre pour recevoir le nom de cette couleur).
Utilisez ensuite cette fonction pour reproduire ce même triangle en différents endroits, en changeant de couleur à chaque fois.
'''
import turtle
import random

colors = ['red', 'blue', 'yellow', 'black', 'green', 'pink']
def triangle(x, y, color):
    turtle.color("")
    turtle.goto(x, y)
    turtle.width(5)
    turtle.color(color)
    turtle.forward(100)  
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)

while True:
    color = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    triangle(random.randint(1, 300), random.randint(1, 300), f"#{color}")
    
