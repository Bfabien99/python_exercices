'''
 Soit la liste suivante :
['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
 'Alexandre-Benoît', 'Louise']
Écrivez un script qui affiche chacun de ces noms avec le nombre de caractères correspondant.
'''
noms = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien' ,'Alexandre-Benoît', 'Louise']

for nom in noms:
    print("Le nom, '", nom,"' ", "contient ", len(nom), " caractère(s).", sep="")