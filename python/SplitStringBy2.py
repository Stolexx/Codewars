# Diviser un texte en une liste de caractères associés 2 par 2

"""
Diviser le string en liste de caractères deux par deux
Si le dernier string contient un caracètre -> Ajouter un "_"
"""
def solution(s):
    list = []
    for i in range(0, len(s), 2):
        c = s[i:i+2]
        if len(c) == 1:
            c += "_"
        list.append(c)
    return list
