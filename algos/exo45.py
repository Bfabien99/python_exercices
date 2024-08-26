'''
Écrivez un script qui recherche le mot le plus long dans une phrase donnée (l’utilisateur du programme doit pouvoir entrer une phrase de son choix). Tâchez de tenir compte des caractères 
accentués.
'''
def long_word(phrase: str):
    tab = phrase.split(' ')
    #print(tab)
    return max(tab, key=len)

while True:
    phrase = input('Entre la phrase : ').strip()
    if phrase == "0":
        break
    if len(phrase) == 0:
        continue
    print(long_word(phrase))
    
    