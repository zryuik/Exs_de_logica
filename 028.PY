#'escreva um programa que faça o computador (pensar) em um numero inteiro de um a 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador o programa deverá escrever na tela se o usuario venceu ou perdeu
from random import randint #importando a biblioteca random
from time import sleep #importando a biblioteca time
pc = randint(0, 5) #faz o computador pensar em um numero
print('-=-' * 20) #so para deixar bunitinhu
print('Vou pensar em um número de 0 a 5 tente adivinhar.... ')
print('-=-' * 20) # msm coisa q a linha 5
usuario = int(input('Em que número eu pensei? '))#aqui o jogador tenta adivinhar
print('PROCESSANDO... ')
sleep(3)
if usuario == pc:
    print('Parabens voce me venceu!! ')
else:
    print(f'Voce perdeu! eu pensei no numero {pc} e nao no {usuario}! ')