'''
 Écrivez un script qui recherche le nombre de mots contenus dans une phrase donnée.
'''
def nb_word(phrase: str):
    tab = phrase.split(' ')
    return len(tab)

print(nb_word("Écrivez un script qui"))