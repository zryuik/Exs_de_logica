print('-=' * 20)
print('     Analisador de Triângulos 2.0 ')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1!= r2!= r3!= r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos não podem formar um triangulo! ')
