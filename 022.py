nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print(f'Seu nome em maiúsculo é: {nome.upper()}')
print(f'Seu nome em minúsculo é: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(' ')}')
#print(f'Seu primeiro nome tem {nome.find(' ')} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras' )
#a linha 8 é a msm coisa q a 6 só que mais dificil