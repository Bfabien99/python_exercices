'''
écrire une fonction qui renvoie le nombre de caractères majuscules contenus dans une phrase donnée en argument.
'''
import string
def nb_maj(phrase: str):
    maj = 0
    for i in phrase:
        if i in string.ascii_uppercase:
            maj += 1
    return maj

print(nb_maj("Je chanterais de Tout Coeur..."))