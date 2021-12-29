# Vérifier si une liste de 10 mouvements sur les axes X et Y fait revenir le joueur à sa position initiale

"""
Compter les mouvements sur l'axe X et Y
Vérifier la longueur du trajet
Retourner la longueur du trajet et X=0 & Yx0
"""
def is_valid_walk(walk):
    x, y = 0, 0
    for e in walk:
        if e == "n":
            y += 1
        elif e == "s":
            y -= 1
        elif e == "e":
            x += 1
        elif e == "w":
            x -= 1
    return len(walk) == 10 and x == 0 and y == 0