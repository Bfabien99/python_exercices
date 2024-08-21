import os

# obtenir le chemin du répertoire courant
rep_courant = os.getcwd()

## open()
# on ouvre le fichier en mode écriture, s'il n'existe pas on le crée
# open() prend deux paramètres, le nom du fichier et la méthode d'ouverture
# a : append (ajout des données à la suite)
# w : write (Supprime les anciennes donnée et crée de nouvelles)
obFichier = open('Monfichier', 'a')

## write()
# write() permet d'écrire dans le fichier ouvert
obFichier.write('Bonjour, fichier !')
# les données sont insérées à la suite ( *pas de saut de ligne ou d'espace par défaut)
obFichier.write("Quel beau temps, aujourd'hui !")

## close()
# on ferme le fichier ouvert grace à close()
obFichier.close()

## ouverture du fichier avec open() en mode lecture
# r : read (ouverture du fichier en mode lecture, * Le fichier doit exister)
obFichier = open('Monfichier', 'r')

###################################
## read()
# lecture de tout le contenu du fichier 
t = obFichier.read()
# limiter à un certain nombre de caractères
# limit = obFichier.read(10)


## on ferme le fichier ouvert grace à close()
obFichier.close()

###############
file = open('TonFichier', 'a')

# ajout de saut de ligne grace à (\n)
file.write('Bonjour, fichier !\n')
file.close()

################
file = open('TonFichier', 'r')

## readline()
# affiche le contenue d'une seule ligne
# *s'il n'y a pas de saut de ligne dans le fichier, tout le contenu du fichier contient sur une seule ligne
t = file.readline() 
print(t)

## readlines()
# readlines() transfère toutes les lignes restantes dans une liste de chaînes
'''
Si vous devez traiter de gros fichiers, utilisez plutôt la méthode readline() dans une boucle
'''
p = file.readlines()
print(p)

file.close()