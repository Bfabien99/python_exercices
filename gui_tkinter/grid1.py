from tkinter import *
fen1 = Tk()
txt1 = Label(fen1, text = 'Premier champ :')
txt2 = Label(fen1, text = 'Second :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
'''
L’option sticky peut prendre l’une des quatre valeurs N, S, W, E (les quatre points cardinaux en anglais). En fonction de cette valeur, on obtiendra un alignement des widgets par le haut, par le 
bas, par la gauche ou par la droite.
'''
# Label des textes
txt1.grid(row =0, sticky=E)
txt2.grid(row =1, sticky=E)

# champs de saisi
entr1.grid(row =0, column =1)
entr2.grid(row =1, column =1)
fen1.mainloop()