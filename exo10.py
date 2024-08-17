#  Écrivez un script qui compte le nombre d’occurrences du caractère « e » dans une chaîne.
ch = "acldmagnc"
occ = 0
for i in range(0, len(ch)):
    if(ch[i] == "c"):
        occ += 1

print("Occurence de 'c' :", occ)