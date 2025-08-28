from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 11)
    soma = jogador + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par Ou Ímpar? ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o pc jogou {pc} total de {soma} ', end ='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Voce perdeu ')
            break

    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            v+=1
        else:
            print('Você PERDEU!')
            break
    print('Lets Play Again: ')
print(f'GAME OVER! Você ganhou {v} vezes.')