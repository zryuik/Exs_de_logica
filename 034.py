salario = float(input('Qual e o salario do funcionario? R$: '))
if salario <= 1250:
    novo = salario + (salario * 0.15) #aqui eu acrescentei mais 15% de salário
else:
    novo = salario + (salario * 0.10) #aqui acrescentei 10%
print(f'Quem ganhava R${salario} passara a ganhar R${novo:}')