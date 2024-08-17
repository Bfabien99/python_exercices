#  Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des asté-risques entre les caractères.
# Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »
ch = "acldmagnc"
new = ""
for i in range(0, len(ch) - 1):
    new += ch[i] + "*"
print("Nouvelle chaîne :", new+ch[-1])