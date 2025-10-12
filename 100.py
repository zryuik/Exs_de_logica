''' Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. '''
from random import randint
numeros = []

def sorteia():
    num = randint(0, 999)
    numeros.append(num)

for _ in range(5):
    sorteia()   
print(numeros)


def somapar():
    soma = 0
    for num in numeros:
        if num % 2  == 0:
            soma += num
    pri