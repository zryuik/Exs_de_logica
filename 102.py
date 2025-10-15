# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(numero, show=False):

    """
    Calcula o fatorial de um número.
    
    Parâmetros:
    num (int): número a ser calculado
    show (bool): mostrar ou não o processo

    Retorna:
    int: resultado do fatorial

    """
    resultado =  1
    for i in range(numero, 0, -1):
        resultado *= i
        if show:
            print(i, end=" x " if i > 1 else " = ")
    return resultado

print(fatorial(5, show=True))

