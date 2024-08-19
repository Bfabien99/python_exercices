'''
Écrire une boucle de programme qui demande à l’utilisateur d’entrer des notes d’élèves. La boucle se terminera seulement si l’utilisateur entre une valeur négative. Avec les notes ainsi entrées, construire progressivement une liste. Après chaque entrée d’une nouvelle note (et donc à chaque itération de la boucle), afficher le nombre de notes entrées, la note la plus élevée, la note la plus basse, la moyenne de toutes les notes.
'''
notes = []
len_notes = len(notes)

while True:
    len_notes += 1
    enter = float(input(f"Entrer la note <{len_notes}> : "))
    if enter < 0:
        len_notes -= 1
        break
    notes.append(enter)

note_max = max(notes)
note_min = min(notes)
moyenne = round(sum(notes)/len_notes, 2)

print("Note entrée :", len_notes)
print("Total :", sum(notes))
print("Note la plus forte :", note_max)
print("Note la plus faible :", note_min)
print("Moyenne :", moyenne)