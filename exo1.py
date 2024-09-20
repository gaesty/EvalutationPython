
#! Exo 1 (noté sur 3 points)
#? Écrire un script Python permettant de trouver les groupes de 3 éléments dans une liste dont la somme est égal à 0
#* exemple 1 :
#* exemple de liste entrée : [2 , 7 , 9 , -9]
#* exemple de liste sortie : [[2, 7, -9]]
#* exemple 2 :
#* exemple de liste entrée : [-33, -10, -8, -2, 1, 4, 9, 10]
#* exemple de liste sortie : [[-10, 1, 9], [-8, -2, 10]]

def trouver_groupes_zero(liste : list) -> list:
    liste.sort()
    groupes : list = list()

    for i in range(len(liste) - 2):
        if i > 0 and liste[i] == liste[i - 1]:
            continue

        gauche : int = i + 1
        droite : int = len(liste) - 1

        while gauche < droite:
            somme : int = liste[i] + liste[gauche] + liste[droite]
            if somme == 0:
                groupes.append([liste[i], liste[gauche], liste[droite]])

                while gauche < droite and liste[gauche] == liste[gauche + 1]:
                    gauche += 1
                while gauche < droite and liste[droite] == liste[droite - 1]:
                    droite -= 1

                gauche += 1
                droite -= 1
            
            elif somme < 0:
                gauche += 1
            else:
                droite -= 1
    return groupes

exemple1 = [2, 7, 9, -9]
exemple2 = [-33, -10, -8, -2, 1, 4, 9, 10]
exemple3 = [23, -17, -6, 9]
print(trouver_groupes_zero(exemple1, exemple2, exemple3)) 
