#! Exo 1 (noté sur 3 points)
#? Écrire un script Python permettant de trouver les groupes de 3 éléments dans une liste dont la somme est égal à 0
#* exemple 1 :
#* exemple de liste entrée : [2 , 7 , 9 , -9]
#* exemple de liste sortie : [[2, 7, -9]]
#* exemple 2 :
#* exemple de liste entrée : [-33, -10, -8, -2, 1, 4, 9, 10]
#* exemple de liste sortie : [[-10, 1, 9], [-8, -2, 10]]

def calcul(liste : list)-> list:
    resultat = 0
    for i in liste:
        resultat = i
        if resultat == 0:
            print("")