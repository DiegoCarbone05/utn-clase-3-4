def potencia(base:int=2, exp:int=2):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)
