def aumentar(preço, taxa):
    res  = preço + (preço * taxa / 100)
    return res


def diminuir(preço, taxa):
    res  = preço - (preço * taxa / 100)
    return res

def dobro(n):
    return n * 2


def metade(n):
    return n / 2    