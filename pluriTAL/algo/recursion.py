def long(liste):
    # simple
    if liste == []:
        return 0
    else:
        return 1 + long(liste[1:])


def parity(chiffre):
    # simple
    if chiffre == 1:
        return "impair"
    
    # récursif
    elif chiffre == 0:
        return "pair"
    
    return parity(abs(chiffre-1))


def modulo(x, b):
    # simple
    if x < b:
        return x
    # récursif
    return modulo(x-b, b)
