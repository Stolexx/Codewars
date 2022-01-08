# Trouver la première lettre qui ne se répète pas dans le texte

"""
Boucle de chaque caractère
Si le cartactère n'est présent qu'une fois -> Retourner ce caractère
Si aucun caractère n'est présent qu'une fois -> Retourner ""
"""
def first_non_repeating_letter(string):
    for c in string:
        if list(string.lower()).count(c.lower()) == 1:
            return c
    return ""
