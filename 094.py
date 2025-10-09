''' Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média '''


galera = []

pessoa = {}

mulheres = []

soma = media = 0

while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("Sexo invalido, por favor digite apenas [M/F]: ")
    pessoa["idade"] = int(input("Idade: "))  
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    if pessoa["sexo"] == "F":
            mulheres.append(pessoa["nome"])
    while True:
        resposta = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resposta in "SN":
            break
        print("ERRO! Responda apenas S ou N. ")
    if resposta == "N":
        break


print(f"Ao todo temos {len(galera)} pessoas cadastradas. ")
media = soma / len(galera)
print(f"A média de idade é de {media:5.2f} anos.")

print(f"As mulheres cadastradas foram ", end="")
for p in galera:
    if p["sexo"] == "F":
        print(f"[{p["nome"]}] ", end="")
print()

print("Lista de pessoas que estão acima da média: ", end="")
for p in galera:
    if p["idade"] >= media:
        print("     ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()

print("<< ENCERRADO >>")


