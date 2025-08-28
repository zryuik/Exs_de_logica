from datetime import date
nascimento = int(input('Informe o ano que voce nasceu: '))
sexo =  str(input('Seu sexo e F ou M ? ')).strip().upper()
if sexo == 'F':
    print('Voce nao precisa do alistamento obrigatorio!!!')
    exit()
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}. ')
if idade == 18:
    print('Voce precisa se alistar imediatamente!!!')
elif idade < 18:
    faltam = 18 - idade
    print(f'Ainda faltam {faltam} anos(s) para o alistamento ')
    ano = ano_atual + faltam
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    faltam = idade - 18
    print(f'Voce ja deveria ter se alistado há {faltam} anos. ')
    ano = ano_atual - faltam
    print(f'Seu alistamento foi em {ano}')