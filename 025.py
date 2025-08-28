#crie um programa que leia o nome de uma pessoa e diga se ela tem "silva no nome"
n = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome tem silva? {"Silva" in n.upper()}')