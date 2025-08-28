print('-=-' * 20 )
print('Analisador de triângulos')
print('-=-' * 20 )
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento:'))
if p < s + t and s < p + t and t < p + s:
    print('Os SEGMENTOS a cima podem formar um Triângulo!')
else:
    print('Os SEGMENTOS a cima nao podem formar um Triângulo')