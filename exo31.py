'''
Écrivez un script qui affiche la valeur de la force de gravitation s’exerçant entre deux masses de 10 000 kg , pour des distances qui augmentent suivant une progression géométrique de raison 2, à partir de 5 cm (0,05 mètre). F= 6.67.10^-11 * (m1 * m2)/d^2
Exemple d’affichage :
d = .05 m : la force vaut 2.668 N
d = .1 m : la force vaut 0.667 N
d = .2 m : la force vaut 0.167 N
d = .4 m : la force vaut 0.0417 N
'''
import math
# Constante de gravitation universelle en N·m²/kg²
G = 6.67e-11

# Les deux masses en kg
m1 = 10000  # en kg
m2 = 10000  # en kg

# distance initiale
i = 0.05
while i < 100:
    print("d =", i,"m : la force vaut", round((G*m1*m2)/math.pow(i, 2), 5), "N")
    i *= 2