'''
Demander à l’utilisateur son nom et son sexe (M ou F). En fonction de ces données, afficher « Cher Monsieur » ou « Chère Mademoiselle » suivi du nom de la personne.
'''
nom = input("Entrer votre nom : ")
sexe = input("Quel est votre genre ? Choisir entre M (homme) ou F (femme): ")
if(sexe.lower() == "m"):
    print("Cher Monsieur", nom)
elif(sexe.lower() == "f"):
    print("Chère Mademoiselle", nom)
else:
    print("0-0")