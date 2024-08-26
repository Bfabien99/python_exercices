'''
 Considérons que vous avez à votre disposition un fichier texte contenant des phrases de diffé-
rentes longueurs. Écrivez un script qui recherche et affiche la phrase la plus longue.
'''
f = open("test", "r")
tab = f.readlines()
long = max(tab)
#long.replace("\n", "")
print(long)