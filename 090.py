'''Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionario. No final, mostre o conteúdo da estrutura na tela. '''



# nome_nota = {}

# nome = str(input("Digite o nome do aluno: "))
# nota = float(input("Digite a nota do aluno: "))


# nome_nota[nome] = nota

# if nota >=5 and nota <7:
#     print(f"- Nome é igual a {nome}")
#     print(f"- Nota é igual a {nota}")
#     print(f"- Situação é igual a Recuperação")
# else:
#     if nota < 5:
#         print(f"- Nome é igual a {nome}")
#         print(f"- Nota é igual a {nota}")
#         print(f"- Situação é igual a Reprovado")
#     else:
#         print(f"- Nome é igual a {nome}")
#         print(f"- Nota é igual a {nota}")
#         print(f"- Situação é igual a Aprovado")

aluno = {}

aluno["Nome"] = str(input("Digite o nome do aluno: "))
aluno["Media"] = float(input(f"Digite a média de {aluno['Nome']}: "))

if aluno["Media"] >= 7:
    aluno["Situação"] = "Aprovado"

elif aluno["Media"] > 5 and aluno["Media"] <7:
    aluno["Situação"] = "Recuperação"

else: 
    aluno["Situação"] = "Reprovado"

print("=" * 30)
for chave , key in aluno.items():

    print(f"- {chave} é igual {key}")

print("=" * 30)














