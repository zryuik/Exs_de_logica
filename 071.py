print('=' * 30)
print('{:^30}'.format('Z AGIOTA'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totalced = 0
while True:
    if total >= céd:
        total -= céd
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${céd}')
            if céd == 50:
                céd = 20

            elif céd == 20:
                céd = 10

            elif céd ==10:
                céd = 1


            totalced = 0
            if total == 0:
                break
print('=' * 30)
print('{:^30}'.format('LEMBRANDO QUE SE NAO PAGAR VAI MORRER'))