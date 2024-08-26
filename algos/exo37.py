import string
'''
 Écrivez une fonction chiffre() qui renvoie « vrai » si l’argument transmis est un chiffre.
'''
def chiffre(arg: str):
    if arg in range(0,10):
        return True
    return False

'''
Écrivez une fonction majuscule() qui renvoie « vrai » si l’argument transmis est une majuscule. 
Tâchez de tenir compte des majuscules accentuées !
'''
def majuscule(arg: str):
    if arg in string.ascii_uppercase :
        return True
    return False

'''
 Écrivez une fonction chaineListe() qui convertisse une phrase en une liste de mots
'''
def chaineListe(phrase: str):
    tab = phrase.split(' ')
    return tab

print(chaineListe("Uen petite fille noir!"))