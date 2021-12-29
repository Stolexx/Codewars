# Réécire un string avec x fois le caractère en fonction de sa position dans le string initial

"""
Faire une boucle de chaque caractère
Faire une seconde boucle en fonction de la position du caractère
Ajouter la valeur à la variable
Retourner la variable
"""
def accum(s):
    result = ""
    p = 1
    for char in s:
        for i in range(p):
            if i == 0:
                result += char.upper()
            else:
                result += char.lower()
        result += "-"
        p += 1
    return result[:-1]