num = int(input('Digite um numero: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')   # azul
        total += 1
    else:
        print('\033[m', end='')  #vermelho 
    print(f'{c}', end=' ')
print('\033[m')
print(f'\nO número {num} foi divisivel {total} vezes')
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

#fiquei literalmente 1 hora nesse copdigo porque esqueci um 'n' no codigo