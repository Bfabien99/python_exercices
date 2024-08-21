import tkinter as tk  # Importation de la bibliothèque Tkinter pour créer l'interface graphique
import math  # Importation de la bibliothèque mathématique pour les calculs

# Constante physique de la gravitation universelle en m^3 kg^-1 s^-2
G = 6.67430e-11

# Création de la fenêtre principale
root = tk.Tk()
root.title("Simulation de Gravité")  # Titre de la fenêtre

# Déclaration des variables pour les masses des deux astres
mass1, mass2 = 5.972e24, 7.348e22  # Exemples : masse de la Terre et de la Lune

# Création d'un canevas dans lequel les astres seront dessinés
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()  # Affichage du canevas dans la fenêtre

# Création des astres sous forme de cercles sur le canevas
astre1 = canvas.create_oval(100, 100, 150, 150, fill="blue")  # Astre 1 en bleu
astre2 = canvas.create_oval(200, 200, 250, 250, fill="red")  # Astre 2 en rouge

# Création d'étiquettes pour afficher la distance et la force gravitationnelle
distance_label = tk.Label(root, text="Distance: ")
distance_label.pack()
force_label = tk.Label(root, text="Force gravitationnelle: ")
force_label.pack()

# Fonction pour calculer la distance entre les centres des deux astres
def calculate_distance(x1, y1, x2, y2):
    # Utilisation du théorème de Pythagore pour calculer la distance
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Fonction pour calculer la force gravitationnelle entre les deux astres
def calculate_gravitational_force(m1, m2, r):
    if r == 0:  # Si la distance est 0, la force devient infinie (éviter division par zéro)
        return float('inf')
    # Formule de la gravitation universelle : F = G * (m1 * m2) / r^2
    return G * (m1 * m2) / r**2

# Fonction pour mettre à jour l'affichage de la distance et de la force
def update_info():
    # Obtenir les coordonnées des coins supérieurs gauches et inférieurs droits des astres
    x1, y1, x1_end, y1_end = canvas.coords(astre1)
    x2, y2, x2_end, y2_end = canvas.coords(astre2)

    # Calculer les coordonnées des centres des astres
    center1_x = (x1 + x1_end) / 2
    center1_y = (y1 + y1_end) / 2
    center2_x = (x2 + x2_end) / 2
    center2_y = (y2 + y2_end) / 2

    # Calculer la distance entre les centres des astres
    distance = calculate_distance(center1_x, center1_y, center2_x, center2_y)
    # Calculer la force gravitationnelle entre les astres
    force = calculate_gravitational_force(mass1, mass2, distance)

    # Mettre à jour les étiquettes avec les nouvelles valeurs
    distance_label.config(text=f"Distance: {distance:.2e} m")
    force_label.config(text=f"Force gravitationnelle: {force:.2e} N")

# Fonction pour déplacer l'astre 1 vers la gauche
def move_astre1_left():
    canvas.move(astre1, -10, 0)  # Déplacer de -10 pixels sur l'axe x
    update_info()  # Mettre à jour les informations de distance et de force

# Fonction pour déplacer l'astre 1 vers la droite
def move_astre1_right():
    canvas.move(astre1, 10, 0)  # Déplacer de 10 pixels sur l'axe x
    update_info()

# Fonction pour déplacer l'astre 1 vers le haut
def move_astre1_up():
    canvas.move(astre1, 0, -10)  # Déplacer de -10 pixels sur l'axe y
    update_info()

# Fonction pour déplacer l'astre 1 vers le bas
def move_astre1_down():
    canvas.move(astre1, 0, 10)  # Déplacer de 10 pixels sur l'axe y
    update_info()

# Fonction pour déplacer l'astre 2 vers la gauche
def move_astre2_left():
    canvas.move(astre2, -10, 0)
    update_info()

# Fonction pour déplacer l'astre 2 vers la droite
def move_astre2_right():
    canvas.move(astre2, 10, 0)
    update_info()

# Fonction pour déplacer l'astre 2 vers le haut
def move_astre2_up():
    canvas.move(astre2, 0, -10)
    update_info()

# Fonction pour déplacer l'astre 2 vers le bas
def move_astre2_down():
    canvas.move(astre2, 0, 10)
    update_info()

# Création des boutons pour déplacer l'astre 1
btn_left1 = tk.Button(root, text="⬅ Astre 1", command=move_astre1_left)
btn_left1.pack(side="left")
btn_right1 = tk.Button(root, text="➡ Astre 1", command=move_astre1_right)
btn_right1.pack(side="left")
btn_up1 = tk.Button(root, text="⬆ Astre 1", command=move_astre1_up)
btn_up1.pack(side="left")
btn_down1 = tk.Button(root, text="⬇ Astre 1", command=move_astre1_down)
btn_down1.pack(side="left")

# Création des boutons pour déplacer l'astre 2
btn_left2 = tk.Button(root, text="⬅ Astre 2", command=move_astre2_left)
btn_left2.pack(side="right")
btn_right2 = tk.Button(root, text="➡ Astre 2", command=move_astre2_right)
btn_right2.pack(side="right")
btn_up2 = tk.Button(root, text="⬆ Astre 2", command=move_astre2_up)
btn_up2.pack(side="right")
btn_down2 = tk.Button(root, text="⬇ Astre 2", command=move_astre2_down)
btn_down2.pack(side="right")

# Démarrage de la boucle principale de la fenêtre
root.mainloop()
