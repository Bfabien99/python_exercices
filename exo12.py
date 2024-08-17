# Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant.
# Ainsi par exemple, « zorglub » deviendra « bulgroz ».
ch = "zorglub"
reverse = ""
i = len(ch) - 1
while i >= 0:
    reverse += ch[i]
    i -= 1
print("Nouvelle chaîne :", reverse)