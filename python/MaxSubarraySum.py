# Instructions : https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

"""
Boucle avec l'élément de départ
Boucle (2) en ajoutant un élément supplémentaire à la somme
Retourner la valeur maximale
"""
def max_sequence(arr):
    ans = 0
    for f in range(len(arr)):
        max = 0
        for i in arr[f:len(arr)]:
            max += i
            if max > ans:
                ans = max
    return ans
