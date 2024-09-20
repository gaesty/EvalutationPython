
#! Exo 4 (noté sur 3 points)
#? Écrire un script Python permettant de générer une liste de deux listes à partir d'une phrase
#? La première liste contient la liste des mots de la phrase
#? La deuxième liste contient les espaces et les virgules qui séparent les mots

#* Exemples :
#* J'ai découvert Python cette semaine => [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" ", " ", " " ," " , " "]]
#* J'ai découvert Python, cette semaine => [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" ", " ", ", " ," " , " "]]
#* J'ai découvert, Python, cette semaine => [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" "," ", ", ", " ," " , " "]]

# Documentation https://www.geeksforgeeks.org/python-program-convert-string-list/, https://www.codecademy.com/resources/docs/python/regex/findall et chatgpt pour mes erreurs

import re

def fromPhraseToListe(phrase : str) -> list:
    liste_mots : list = list(phrase.split(" "))
    liste_separateurs = re.findall(r'[^\w\']+', phrase)
    return [liste_mots, liste_separateurs]

print(fromPhraseToListe("J'ai découvert Python cette semaine"))
print(fromPhraseToListe("J'ai découvert Python, cette semaine"))
print(fromPhraseToListe("J'ai découvert, Python, cette semaine"))