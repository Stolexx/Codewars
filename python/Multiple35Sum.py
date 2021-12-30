# Somme de tous les multiples de 3 et de 5 jusqu'à un certain nombre

"""
Créer une liste de tous les multiples de 3 et de 5
Vérifier que la liste ne contient pas des doublons
Additionner tous les nombres
"""
def solution(number):
    multiples = list(dict.fromkeys([i*3 for i in range(int(number/3)+1) if i*3 < number] + [i*5 for i in range(int(number/5)+1) if i*5 < number]))
    return sum(multiples)