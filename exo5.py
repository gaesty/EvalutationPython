
#! Exo 5 (noté sur 8 points)
#? Le jeu "plus petit/plus grand" est un exercice de base de l'informatique. Le script génère un nombre
#? aléatoire et le joueur essaye de le retrouver. À chaque étape, le script indique si le nombre proposé
#? par le joueur est plus petit ou plus grand que le nombre qu'il a « choisi ».
#? Ici, l'objectif est de programmer la position inverse : le joueur choisit un nombre (dans sa tête) et le
#? script essaye de le retrouver. La difficulté du script est de détecter la tricherie du joueur :

#* Scénario honnête :
#* Mémorisez un nombre entier entre 1 et 100, script va essayer de le retrouver, ne trichez pas :
#* script propose 52... +, - ou G ?-
#* script propose 31... +, - ou G ?-
#* script propose 10... +, - ou G ?+
#* script propose 22... +, - ou G ?G
#! script a trouvé 22 en 4 coups !!!
#* Scénario tricherie :
#* Mémorisez un nombre entier entre 1 et 100, script va essayer de le retrouver, ne trichez pas :
#* script propose 41... +, - ou G ?-
#* script propose 28... +, - ou G ?-
#* script propose 10... +, - ou G ?+
#* script propose 26... +, - ou G ?+
#* script propose 27... +, - ou G ?-
#! Tricheur !!! A la réponse 4 il avait été proposé 26 et répondu "+" - En proposant 27 la réponse ne
#! peut pas être "-" !!!
#! J'ai gagné par forfait en 5 coups !!!

# Documentation https://www.tutorialspoint.com/higher-lower-game-with-python pour une idée de la logique à mettre en place


import random

def jeu():
    plus_petit_nombre : int = 1
    plus_grand_nombre : int = 99
    nombre_de_coups : int = 1
    nombre_rechercher : int = random.randint(plus_petit_nombre, plus_grand_nombre)
    print("Pensez à un nombre entre 1 et 99")
    reponse : str = ""
    while reponse != "G":
        reponse = input(f"l'ordinateur propose {nombre_rechercher}. Répondez par -, + ou G :")
        if reponse == "-":
            nombre_de_coups += 1
            plus_grand_nombre = nombre_rechercher
            nombre_rechercher = random.randint(plus_petit_nombre, plus_grand_nombre)
        if reponse == "+":
            nombre_de_coups += 1
            plus_petit_nombre = nombre_rechercher
            nombre_rechercher = random.randint(plus_petit_nombre, plus_grand_nombre)
        if reponse == "G":
            return print(f"l'ordinateur a trouvé {nombre_rechercher} en {nombre_de_coups} coups")
jeu()    

