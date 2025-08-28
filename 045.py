from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-=' * 10)
print(f'O computador escolheu {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 10)
if computador == 0: #computador joga pedra
   if jogador == 0:
      print('EMPATE')
   elif jogador == 1:
      print('JOGADOR VENCEU')
   elif jogador == 2:
      print('COMPUTADOR VENCEU')
   else:
      print('JOGADA INVÁLIDA!!! ')
elif computador == 1: #computador joga papel
   if jogador == 0:
      print('CCOMPUTADOR VENCEU')
   elif jogador == 1:
      print('EMPATE')
   elif jogador == 3:
      print('JOGADOR VENCEU')
   else:
      print('JOGADA INVÁLIDA')  
elif computador == 2: #computador joga tesoura
    if jogador == 0:
      print('JOGADOR VENCEU') 
    elif jogador == 1:
       print('COMPUTADOR VENCE')
    elif jogador== 2:
       print('EMPATE')
    else:
       print('JOGADA INVÁLIDA')      