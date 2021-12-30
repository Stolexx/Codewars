# Formatter une liste avec des virgules et des & pour la rendre lisible

"""
Mettre tous les noms dans une liste
Formatter les noms avec une virgule entre
Remplacer la dernière virgule par un &
"""
def namelist(names):
    list = [e.get("name") for e in names]
    result = ", ".join(list)
    if len(list) > 1: result = result[:result.rfind(",")] + " &" + result[result.rfind(",")+1:]
    return result