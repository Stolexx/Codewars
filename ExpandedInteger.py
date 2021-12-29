"""
Prendre chaque caractère un par un
Si le caractère n'est pas 0 -> Ajouter ce caractère avec x zéros
Retourner le résultat
"""
def expanded_form(num):
    result = ""
    p = len(str(num))
    for i in str(num):
        p -= 1
        if not int(i) == 0:
            result += i + "0" * p + " + "
    return result[:-3]