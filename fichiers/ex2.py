'''
Il va de soi que les boucles de programmation s’imposent lorsque l’on doit traiter un fichier dont on ne connaît pas nécessairement le contenu à l’avance. L’idée de base consistera à lire ce fichier morceau par 
morceau, jusqu’à ce que l’on ait atteint la fin du fichier.
La fonction ci-dessous illustre cette idée. Elle copie l’intégralité d’un fichier, quelle que soit sa taille, en transférant des portions de 50 caractères à la fois :
'''
def copieFichier(source, destination):
    "recopier un fichier en éliminant les lignes de remarques"
    fs = open(source, 'r')
    fd = open(destination, 'w')
    while 1:
        txt = fs.readline()
        if txt =='':
            break
        if txt[0] != '#':
            fd.write(txt)
    fs.close()
    fd.close()
    return

copieFichier('Monfichier','Tonfichier')