#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#ex: ana maria de souza
#primeiro: ana
#último: ana
n = str(input('Digite seu nome completo: ')).strip().upper()
nome = n.split()
print('Muito prazer em te conhecer! ')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')

