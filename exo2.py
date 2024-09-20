#! Exo 2 (noté sur 3 points)
#! Addition avec des listes
#? Soit deux listes n1 et n2 permettant de coder deux nombre entiers positifs .
#? n1 = [1,2,3]
#? n2 = [7]
#? Le but est de créer une fonction qui fait le total de n1+n2 et de retourner le résultat sous forme de
#? liste, soit :
#? total = [1,3, 0] car 123 + 7 = 130
#? Ne pas utiliser la manipulation de string pour résoudre c'est exercice mais les mathématiques.

#* Exemples :
#* total([8, 4, 0], [8, 3])
#* résultat [9, 2, 3]
#* total([1, 8, 3], [7]))
#* résultat [1, 9, 0]
#* total([1, 2, 3], [0])
#* résultat [1, 2, 3] 

def additionListes(liste1 : list, liste2 : list) -> list:
    return [int(x) for x in str(int(''.join(map(str, liste1))) + int(''.join(map(str, liste2))))]

print(additionListes([8, 4, 0], [8, 3]))
print(additionListes([1, 8, 3], [7]))
print(additionListes([1, 2, 3], [0]))