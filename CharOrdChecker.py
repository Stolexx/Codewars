# Compter dans un string le nombre de lettres qui sont au dessus de m dans l'alphabet

"""
Faire une boucle de chaque caractère
Code du caractère
Ajouter 1 au compteur si le code est > à celui de m
Retourner le compteur et la taille de s
"""
def printer_error(s):
    errors = 0
    for e in s:
        if ord(e) > 109:
            errors += 1
    return "%e/%t" % (errors, len(s))