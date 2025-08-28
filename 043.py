peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

IMC = peso / (altura ** 2)
print(f'Seu IMC é {IMC:.1f}')

if IMC < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= IMC <= 25:
    print('PESO IDEAL')
elif 25 <= IMC <= 30:
    print('SOBREPESO')
elif 30 <= IMC <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')

peso_min = 18.5 * (altura ** 2)
peso_max = 24.9 * (altura ** 2)


print(f'\nPara sua altura, o peso ideal está entre {peso_min:.1f} kg e {peso_max:.1f} kg.')