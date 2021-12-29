# Filtre une liste en gardant que les nombres entiers

"""
Détection des nombres
Ajout des nombres à la nouvelle liste
Return de la liste
"""
def filter_list(l):
    return [e for e in l if type(e) == int]