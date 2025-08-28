print('========== BOCA DE FUMO DO Z ==========')
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/pix
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão  ''')
opção = float(input('Qual é a opção? '))
if opção == 1:
    total = compras - (compras * 0.10)
    print(f'O valor da compra com 10% de desconto é R$ {total:.2f}:  ')
elif opção == 2:
    total = compras - (compras * 0.05)
    print(f'O valor da compra com 5% de desconto é R$ {total:.2f} ')
elif opção == 3:
    parcela = compras / 2
    print(f'Pagamento em 2x de R$ {compras:.2f} sem juros. Total: R$ {parcela:.2f}')
elif opção == 4:
    vezes = int(input('Quantas vezes? '))
    total = compras + (compras * 0.20)
    parcela = total / vezes
    print(f'Pagamento em {vezes}x de R$ {parcela:.2f} com juros. Total: R$ {total:.2f}')
else:
    print('Opção invalida')



