import random
# Écrivez un programme qui convertit un nombre entier de secondes fourni au départ en un nombre d’années, de mois, de jours, d'heure, de minutes et de secondes (utilisez l’opérateur modulo : %).

# referencement du temps en seconde
one_sec = 1 # une seconde
one_min = 60 * one_sec # 1 minute en seconde
one_hour = 60 * one_min # 1 heure en seconde
one_day = 24 * one_hour # 1 jour en seconde
one_month = 30 * one_day # 1 mois en seconde
one_year = 365 * one_day # 1 année en seconde

rand_sec = random.randint(1, 99999999)

year = rand_sec // one_year
remaining = rand_sec % one_year

month = remaining // one_month
remaining = remaining % one_month

day = remaining // one_day
remaining = remaining % one_day

hour = remaining // one_hour
remaining = remaining % one_hour

min = remaining // one_min
remaining = remaining % one_min

sec = remaining // one_sec
print(rand_sec)
print("Année ", year)
print("Mois ", month)
print("Jours ", day)
print("Heure ", hour)
print("Minutes ", min)
print("Secondes ", sec)

