'''
Écrivez un script capable d’afficher la liste de tous les jours d’une année imaginaire, laquelle 
commencerait un jeudi. Votre script utilisera lui-même trois listes : une liste des noms de jours de la semaine, une liste des noms des mois, et une liste des nombres de jours que comportent 
chacun des mois (ne pas tenir compte des années bissextiles).
Exemple de sortie :
jeudi 1 janvier vendredi 2 janvier samedi 3 janvier dimanche 4 janvier et ainsi de suite, jusqu’au jeudi 31 décembre.
'''
# Cette liste représente les jours de la semaine. 
# On commence par "jeudi" parce que l'année imaginaire commence un jeudi.
jours = ["jeudi", "vendredi", "samedi", "dimanche", "lundi", "mardi", "mercredi"]

# Initialisation des variables pour les jours (d) et les mois (m).
# On commence avec le premier jour et le premier mois.
d = 1  # Variable pour suivre le jour actuel, commence à 1
m = 1  # Variable pour suivre le mois actuel, commence à 1

# Liste des noms des mois de l'année dans l'ordre.
mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", 
        "aout", "septembre", "octobre", "novembre", "decembre"]

# Cette liste contient le nombre de jours dans chaque mois.
# Par exemple, janvier a 31 jours, février a 28 jours, etc.
# On suppose une année non-bissextile, donc février a toujours 28 jours.
jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Variable pour suivre l'index du jour de la semaine, 
# commencera par le premier jour, c'est-à-dire "jeudi" à l'index 0.
jour_index = 0

# Boucle principale pour parcourir tous les mois de l'année.
# On utilise une boucle "while" qui va continuer tant que le numéro du mois (m) est inférieur ou égal à 12.
while m <= 12:
    # Affiche un en-tête pour chaque mois. Exemple: "#### janvier ####"
    # `mois[m-1]` donne le nom du mois actuel. On utilise `m-1` car les index des listes commencent à 0.
    print(f"#### {mois[m-1]} ####")
    
    # Boucle interne pour parcourir tous les jours du mois en cours.
    # `jours_par_mois[m-1]` donne le nombre de jours dans le mois actuel.
    while d <= jours_par_mois[m-1]:
        # Affiche le jour de la semaine, le numéro du jour et le mois actuel.
        # Exemple: "jeudi 1 janvier"
        print(f"{jours[jour_index]} {d} {mois[m-1]}")
        
        # Incrémente la variable `d` pour passer au jour suivant.
        d += 1
        
        # Incrémente `jour_index` pour passer au jour de la semaine suivant.
        # `% 7` assure que l'index reste entre 0 et 6. 
        # Quand on atteint 6 (mercredi), l'index retourne à 0 (jeudi).
        jour_index = (jour_index + 1) % 7
    
    # Après avoir parcouru tous les jours du mois actuel, réinitialiser `d` à 1 pour le prochain mois.
    d = 1
    
    # Incrémenter `m` pour passer au mois suivant.
    m += 1
    
    # Imprime une ligne de séparation pour indiquer la fin du mois et le début du suivant.
    print('-------')
