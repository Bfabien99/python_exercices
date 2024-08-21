'''
En vous inspirant du programme qui détecte les clics de souris dans un canevas, modifiez le 
programme ci-dessus pour y réduire le nombre de boutons : pour déplacer un astre, il suffira de 
le choisir avec un bouton, et ensuite de cliquer sur le canevas pour que cet astre se positionne à 
l’endroit où l’on a cliqué.
'''
import tkinter as tk
import math

# Constantes physiques
G = 6.67430e-11  # Constante gravitationnelle en m^3 kg^-1 s^-2

# Fenêtre principale
root = tk.Tk()
root.title("Simulation de Gravité")

# Variables pour stocker la masse et la sélection d'astre
mass1, mass2 = 5.972e24, 7.348e22  # Exemples : masse de la Terre et de la Lune
selected_astre = None

# Canevas
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Création des astres (cercles)
astre1 = canvas.create_oval(100, 100, 150, 150, fill="blue")
astre2 = canvas.create_oval(200, 200, 250, 250, fill="red")

# Labels pour afficher la distance et la force
distance_label = tk.Label(root, text="Distance: ")
distance_label.pack()
force_label = tk.Label(root, text="Force gravitationnelle: ")
force_label.pack()

# Fonction pour calculer la distance entre deux points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Fonction pour calculer la force gravitationnelle
def calculate_gravitational_force(m1, m2, r):
    if r == 0:  # Éviter la division par zéro
        return float('inf')
    return G * (m1 * m2) / r**2

# Mise à jour des informations sur la distance et la force
def update_info():
    x1, y1, x1_end, y1_end = canvas.coords(astre1)
    x2, y2, x2_end, y2_end = canvas.coords(astre2)

    center1_x = (x1 + x1_end) / 2
    center1_y = (y1 + y1_end) / 2
    center2_x = (x2 + x2_end) / 2
    center2_y = (y2 + y2_end) / 2

    distance = calculate_distance(center1_x, center1_y, center2_x, center2_y)
    force = calculate_gravitational_force(mass1, mass2, distance)

    distance_label.config(text=f"Distance: {distance:.2e} m")
    force_label.config(text=f"Force gravitationnelle: {force:.2e} N")

# Fonction pour sélectionner un astre
def select_astre1():
    global selected_astre
    selected_astre = astre1

def select_astre2():
    global selected_astre
    selected_astre = astre2

# Fonction pour déplacer l'astre sélectionné
def move_astre(event):
    if selected_astre:
        x, y = event.x, event.y
        canvas.coords(selected_astre, x - 25, y - 25, x + 25, y + 25)  # Ajuster les coordonnées pour centrer le cercle
        update_info()

# Boutons de sélection
btn_select_astre1 = tk.Button(root, text="Sélectionner Astre 1", command=select_astre1)
btn_select_astre1.pack(side="left")
btn_select_astre2 = tk.Button(root, text="Sélectionner Astre 2", command=select_astre2)
btn_select_astre2.pack(side="left")

# Binding du clic de souris pour déplacer l'astre sélectionné
canvas.bind("<Button-1>", move_astre)

# Démarrage de la boucle principale
root.mainloop()
