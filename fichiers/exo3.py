'''
Écrivez un script qui génère automatiquement un fichier texte contenant les tables de multiplication de 2 à 30 (chacune d’entre elles incluant 20 termes seulement).
'''
f = open('multiply.txt', 'a')
for i in range(2, 31):
    f.write(f'# TABLE DE {i} #\n')
    for j in range(1, 21):
        f.write(f"{i} x {j} = {i*j}\n")
    f.write('---------\n')