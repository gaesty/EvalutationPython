# Eval – Python

# H3 - Hitema

## Consignes

- **Date de rendu maximum** : le 29 Septembre 2024 17h
- **Modalité de rendu** :
    1. créer un dépôt github et réaliser un push de l'ensemble des réponses
    2. remplir le formulaire disponible à l'adresse suivante :
    3. https://forms.gle/ozm9zWCZwmaAei9y
       ou

https://docs.google.com/forms/d/e/1FAIpQLScwt3tBhvJVB9HZXM2p0OaiWJNP5_quQ4tvXVwJt
wbCPyQdZg/viewform

- **Evaluation** : la note de l'exercice est noté à côté de l'énoncé

### --------------------------

```
Vous disposez d'internet, du support et de notes de cours transmise sur github
Il s'agit d'un travail individuel
```

## Exo 1 (noté sur 3 points)

Écrire un script Python permettant de trouver les groupes de 3 éléments dans une liste dont la
somme est égal à 0

**exemple 1 :**
exemple de liste entrée : [2 , 7 , 9 , -9]
exemple de liste sortie : [[2, 7, -9]]

**exemple 2 :**
exemple de liste entrée : [-33, -10, -8, -2, 1, 4, 9, 10]
exemple de liste sortie : [[-10, 1, 9], [-8, -2, 10]]

## Exo 2 (noté sur 3 points)

Addition avec des listes
Soit deux listes n1 et n2 permettant de coder deux nombre entiers positifs.
n1 = [1,2,3]
n2 = [7]

Le but est de créer une fonction qui fait le total de n1+n2 et de retourner le résultat sous forme de
liste, soit :
total = [1,3, 0] car 123 + 7 = 130
Ne pas utiliser la manipulation de string pour résoudre c'est exercice mais les mathématiques.

**Exemples :**
total([8, 4, 0], [8, 3])
résultat [9, 2, 3]

total([1, 8, 3], [7]))
résultat [1, 9, 0]

total([1, 2, 3], [0])
résultat [1, 2, 3]


## Exo 3 (noté sur 3 points)

Écrire une class Python s'appelant Exo disposant d'une méthode appelée puissance implémentant la
fonction pow(x,n)
https://www.w3schools.com/python/ref_func_pow.asp
Vous ne pouvez pas utiliser la fonction builtins pow() de Python ou l'opérateur **, vous devez
utiliser la récursivité pour implémenter cette méthode

**Exemples :**

Exo().puissance(2,3) retourne 8
Exo().puissance(2,1) retourne 2
Exo().puissance(2,0) retourne 1
Exo().puissance(2,-3) retourne 0.

## Exo 4 (noté sur 3 points)

Écrire un script Python permettant de générer une liste de deux listes à partir d'une phrase
La première liste contient la liste des mots de la phrase
La deuxième liste contient les espaces et les virgules qui séparent les mots

**Exemples :**

J'ai découvert Python cette semaine => [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" ", "
", " " ," " , " "]]

J'ai découvert Python, cette semaine => [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" ",
" ", ", " ," " , " "]]

J'ai découvert, Python, cette semaine => [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" ",
", ", ", " ," " , " "]]


## Exo 5 (noté sur 8 points)

Le jeu "plus petit/plus grand" est un exercice de base de l'informatique. Le script génère un nombre
aléatoire et le joueur essaye de le retrouver. À chaque étape, le script indique si le nombre proposé
par le joueur est plus petit ou plus grand que le nombre qu'il a « choisi ».

Ici, l'objectif est de programmer la position inverse : le joueur choisit un nombre (dans sa tête) et le
script essaye de le retrouver. La difficulté du script est de détecter la tricherie du joueur :

**Scénario honnête :**
Mémorisez un nombre entier entre 1 et 100, script va essayer de le retrouver, ne trichez pas :
script propose 52... +, - ou G ?-
script propose 31... +, - ou G ?-
script propose 10... +, - ou G ?+
script propose 22... +, - ou G ?G
script a trouvé 22 en 4 coups !!!

**Scénario tricherie :**
Mémorisez un nombre entier entre 1 et 100, script va essayer de le retrouver, ne trichez pas :
script propose 41... +, - ou G ?-
script propose 28... +, - ou G ?-
script propose 10... +, - ou G ?+
script propose 26... +, - ou G ?+
script propose 27... +, - ou G ?-
Tricheur !!! A la réponse 4 il avait été proposé 26 et répondu "+" - En proposant 27 la réponse ne
peut pas être "-" !!!
J'ai gagné par forfait en 5 coups !!!


