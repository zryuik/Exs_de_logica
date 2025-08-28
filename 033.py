#faça um programa que leia 3 numero e mostre qual q o menor e qual e o maior
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < a:
    menor = c
print(f'o menor valor digitado foi {menor}')
#Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior numero digitado foi {maior}')