#  Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie 
# par l’utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)
vitesse = float(input("Entrer une vitesse : "))
ms = round((1609 * vitesse) / 3600, 2)
kmh = round((1609 * vitesse / 1000), 2)
print(vitesse, "miles/heures = ", ms, "mètres/seconde et ", kmh, "kilomètre/heure.")

#1 m => 1609/1000 km
