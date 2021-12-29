# Remplacer les caractères qui sont présents plus d'un fois avec ")" et remplacer les autres avec ")"

"""
Split les caractères
Faire une boucle de chaque caractère
Si le caractère est présent une seule fois -> Ajouter "("
Sinon -> Ajouter ")"
Retourner le texte
"""
def duplicate_encode(word):
    result = ""
    chars = [e.lower() for e in word]
    for e in chars:
        if chars.count(e) > 1:
            result += ")"
        else:
            result += "("
    return result