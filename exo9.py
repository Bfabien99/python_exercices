#  Écrivez un script qui détermine si une chaîne contient ou non le caractère « e »
ch = "alldmagnd"
exist = False
for i in range(0, len(ch)):
    if(ch[i] == "e"):
        exist = True

if(exist):
    print("Oui!")
else:
    print("Non!")