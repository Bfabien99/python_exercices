'''
Écrivez un script qui crée automatiquement la liste des sinus des angles de 0° à 90°, par pas de 5°. Attention : la fonction sin() du module math considère que les angles sont fournis en radians 
(360° = 2 π radians).
'''
import math

for i in range(0, 91, 5):
    rad = (i*2*math.pi)/360
    print("Le sin(",i,") en deg est ", math.sin(rad), sep="")
