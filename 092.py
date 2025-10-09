''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a ctps for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a dados vai se aposentar. '''

from datetime import datetime

dados = {}

dados["Nome"] = input("Digite seu nome: ")
nasc = int(input("Ano de nascimento: "))
dados["idade"] = (datetime.now().year - nasc)
dados["ctps"] = int(input("Carteira de Trabalho (0 não tem):"))
if dados["ctps"] != 0:
    dados["contratação"] = int(input("Ano de Contratação: "))
    dados["salário"] = float(input("Salário: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)
print("-=" * 30)

for c, k in dados.items():
    print(f"- {c} tem valor {k}")

print("-=" * 30)