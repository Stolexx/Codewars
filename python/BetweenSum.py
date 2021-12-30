# Somme de tous les nombres entre un minimum et un maximum

"""
Trouver le max et le min
Créer une boucle où on ajoute à la variable de calcul le nombre suivant
"""
def get_sum(a,b):
    c = min([a, b])
    d = 0
    while c <= max([a, b]):
        d += c
        c += 1
    return d