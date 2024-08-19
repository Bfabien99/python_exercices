# En partant de l’exercice précédent, écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome (c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), comme par exemple « radar » ou « s.o.s ».
ch = "radar"
reverse = ""
i = len(ch) - 1
while i >= 0:
    reverse += ch[i]
    i -= 1

if ch == reverse:
    print("Palindrome")
else:
    print("Non")