'''
Écrivez un script qui permette de créer et de relire aisément un fichier texte. Votre programme demandera d’abord à l’utilisateur d’entrer le nom du fichier. Ensuite il lui proposera le choix, soit d’enregistrer de nouvelles lignes de texte, soit d’afficher le contenu du fichier.
L’utilisateur devra pouvoir entrer ses lignes de texte successives en utilisant simplement la 
touche <Enter> pour les séparer les unes des autres. Pour terminer les entrées, il lui suffira d’entrer une ligne vide (c’est-à-dire utiliser la touche <Enter> seule).
'''
#### DEFINITION DES DIFFERENTES FONCTIONS
## Fonctions utilitaires
# vérifier l'existance d'un fichier
def is_file(fname: str):
    "Vérifier l'existance du fichier"
    try:
        f = open(fname, 'r')
        f.close()
        return 1
    except:
        return 0

# créer un nouveau fichier
def create_file(fname: str):
    "Créer un fichier"
    try:
        f = open(fname, 'w')
        f.close()
        return 1
    except:
        return 0

# inserer du texte dans un fichier
def insert_into(fname: str, content: str):
    "Insertion des données dans le ficier"
    try:
        f = open(fname, "a")
        f.write(content)
        f.close()
        return 1
    except:
        return 0

# obtenir le texte(contenue) d'un fichier
def read_file(fname: str):
    "Lecture du fichier"
    try:
        f = open(fname, "r")
        lecture = ""
        while True:
            text = f.readline()
            if text == '':
                break
            lecture += text
        f.close()
        return lecture
    except:
        return 0

## Fonction structurant la logique (le program)
def program():
    # Message d'accueil
    print('''
              BIENVENUE DANS LA LECTURE
        ''')
    
    #### initialisation d'une boucle pour maintenir le program actif
    while True:
        # Message listant les options disponibles
        print('''
            ** OPTIONS **
            1- Lire un livre
            2- Ajouter du contenu à un livre
            3- Créer un nouveau livre
            0- Fermer
        ''')
        # recupérer le choix de l'utilisateur
        choix = input("Choix (1) ou (2) ou (3) : ")
        
        ## si le choix est 0
        if choix == "0":
            # on quitte le program
            print('''
                -- BYE ! --
            ''')
            break
        ## si le choix est 1
        if choix == "1":
            print('1- LIRE UN LIVRE')
            while True:
                print('''
                    (Lire un livre)
                    Entrer le nom du livre
                    0- pour quitter
                ''')
                choix = input("Nom du livre : ")
                if choix == "0":
                    break
                else:
                    if is_file(choix):
                        print("----- début ------")
                        text = read_file(choix)
                        print(text)
                        print("----- fin ------")
                    else:
                        print("XX Le fichier <", choix, "> n'existe pas... XX")
                    continue
        if choix == "2":
            print('2- Ajouter du contenu à un livre')
            while True:
                print('''
                    (Ajouter du contenu)
                    Entrer le nom du livre
                    0- pour quitter
                ''')
                choix = input("Nom du livre : ")
                if choix == "0":
                    break
                else:
                    if is_file(choix):
                        content = input("> ")
                        while content != "":
                            contenu = f"{content}\n"
                            insert_into(choix, contenu)
                            content = input("> ")
                        print('---- contenu ajouté -----')
                        break
                    else:
                        print("XX Le fichier <", choix, "> n'existe pas... XX")
                    continue     
        if choix == "3":
            print('2- Créer un livre')
            while True:
                print('''
                    (Créer un nouveau livre)
                    Entrer le nom du livre
                    0- pour quitter
                ''')
                choix = input("Nom du livre : ")
                if choix == "0":
                    break
                else:
                    if not is_file(choix):
                        create_file(choix)
                        print('---- Nouveau livre crée -----')
                    else:
                        print("XX Le fichier <", choix, "> existe déjà XX")
                    break
        else :
            continue     
    return

#### Lancement du program
program()