# Trouver le maximum et le minimum parmis une string qui contient des nombres

"""
Liste des nombres (split par espace)
Trouver le max & min
Return un string avec min, " ", max
"""
def high_and_low(numbers):
    list = [e for e in numbers.split()]
    return max(list) + " " + min(list)