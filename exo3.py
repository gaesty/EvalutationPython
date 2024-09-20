#! Exo 3 (noté sur 3 points)
#? Écrire une class Python s'appelant Exo disposant d'une méthode appelée puissance implémentant la
#? fonction pow(x,n)
#? https://www.w3schools.com/python/ref_func_pow.asp
#? Vous ne pouvez pas utiliser la fonction builtins pow() de Python ou l'opérateur **, vous devez
#? utiliser la récursivité pour implémenter cette méthode

#* Exemples :
#* Exo().puissance(2,3) retourne 8
#* Exo().puissance(2,1) retourne 2
#* Exo().puissance(2,0) retourne 1
#* Exo().puissance(2,-3) retourne 0.125

# Documentation utilisée https://stackoverflow.com/questions/42299891/a-to-the-power-of-b-without-ab-python et chatgpt pour corriger mes erreurs

class Exo:
    def puissance(self, x: int, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.puissance(x, -n)

        # Récursion
        return x * self.puissance(x, n - 1) 

# Exemples d'utilisation
print(Exo().puissance(2, 3))   
print(Exo().puissance(2, 1))   
print(Exo().puissance(2, 0))   
print(Exo().puissance(2, -3))
