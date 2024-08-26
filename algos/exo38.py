'''
écrire un script qui puisse extraire d’un texte tous les mots qui commencent par une majuscule.
'''
import string
def extract(phrase: str):
    tab = phrase.split(' ')
    for i in tab:
        if i[0] in string.ascii_uppercase:
            tab.pop(tab.index(i))
    return ' '.join(tab)

print(extract('A la une je Me porterais Bien'))