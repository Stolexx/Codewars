# Fusionner deux listes en enlevant les doublons

"""
Faire deux boucles des deux listes
Comparer les deux éléments
Si i est dans e -> Ajouter à la nouvelle liste
Retourner la liste
"""
def in_array(array1, array2):
    r = []
    for e in array2:
        for i in array1:
            if i in e:
                r.append(i)
    r = list(dict.fromkeys(r))
    r.sort()
    return r