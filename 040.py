n1 = float(input("Digite sua primeira nota: "))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print(f'sua média é de {media:.1f}')
if media < 5:
    print('REPROVADO!!! ')
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO!!!')
else:
    print('APROVADO"!!!')