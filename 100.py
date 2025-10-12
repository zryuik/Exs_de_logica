''' Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. '''

from time import sleep
from random import randint

def sorteia(numeros):
    print("Sorteando 5 valores da lista: ", end="")
    for contador in range(0, 5):
        numero = randint(1, 10)
        numeros.append(numero)
        print(f"{numero} ", end="", flush=True)
        sleep(0.3)
    print(" CONCLUIDO!")

def somapar(numeros):
    soma = 0
    for num in numeros:
        if num % 2  == 0:
            soma += num
    print(f"Foram gerados {len(numeros)} números, e a soma dos números pares é {soma}")

numeros = []
sorteia(numeros)
somapar(numeros)
