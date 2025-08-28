tot18 = totalhomens = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo not in 'MF':
            print('Opção invalida! digite novamente: ')
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').upper().strip()[0]
        if resp not in 'SN':
            print('Opção invalida! digite novamente: ')
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {tot18} ')
print(f'Ao todo temos {totalhomens} homens cadastrados ')
print(f'E temos {totm20} mulheres com menos de 20 anos')
