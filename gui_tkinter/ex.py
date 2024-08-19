import tkinter

fenetre1 = tkinter.Tk() 
text1 = tkinter.Label(fenetre1, text="Bonjour", fg='red')
text1.pack()
button1 = tkinter.Button(fenetre1, text="Quitter", command=fenetre1.destroy)
button1.pack()
fenetre1.mainloop()
