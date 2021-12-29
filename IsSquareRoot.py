# Vérifier si un nombre est une racine carrée (nombre entier seulement)

"""
Prendre la valeur de la racine carrée et la convertir en entier
Vérifier que le nombre est positif
Si la valeur entière est la même que la valeur float -> True
Sinon -> False
"""
import math

def is_square(n):
    return n >= 0 and (float(int(math.sqrt(n))) == math.sqrt(n))