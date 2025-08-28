#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado
from time import sleep
cliente = str(input('Olá, o que voce deseja hoje? '))
if cliente.lower() == 'emprestimo':
    print('Só um momento por favor...')
    sleep(3)
    print('so um momento enquanto passo voce para os setores responsaveis...')
    sleep(3)
else:
    print('Nao trabalhamos com esse serviço, tenha um bom dia!')
    exit()
valor_casa = float(input('Digite valor da casa: R$'))
salario_comprador = float(input('Qual é o valor do seu salario? R$'))
anos = int(input('Em quantos anos será pago? '))
prestacao = valor_casa / (anos * 12)
limite = salario_comprador * 0.30
print(f'Para pagar uma casa de R${valor_casa} em {anos}', end='')
print(f' a prestação será de R$ {prestacao:.2f}')
if prestacao > limite:
    print('Emprestimo negado!!')
else:
    print('Emprestimo aprovado, Aproveite!!!')
