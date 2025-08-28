from random import randint #importando a biblicoteca random com randint para randomizar o numero que o pc vai pensar

pc = randint(0, 10) # definindo o numero que o pc vai pensar
print('SOu seu computador... Acabei de pensar em um numero entre 0 e 10: ')
print('Será que você consegue advinhar qual foi? ')
acertou = False
jogadas = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    jogadas += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez. ')

print(f'Acertou! voce precisou de {jogadas} jogadas para acertar o numero {pc}')