total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = (input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'{' FIM DO PROGRAMA ':=^40}')
print(f'O total da compra foi {total:.2f}')
print(f'Temos {totmil} produtos custando mais de mil reais')
print(f'O produto mais barato foi {barato} que custa {preço}')