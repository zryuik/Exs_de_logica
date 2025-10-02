nome_nota = {}

nome = str(input("Digite o nome do aluno: "))
nota = float(input("Digite a nota do aluno: "))


nome_nota[nome] = nota

if nota >=5 and nota <7:
    print(f"- Nome é igual a {nome}")
    print(f"- Nota é igual a {nota}")
    print(f"- Situação é igual a Recuperação")
else:
    if nota < 5:
        print(f"- Nome é igual a {nome}")
        print(f"- Nota é igual a {nota}")
        print(f"- Situação é igual a Reprovado")
    else:
        print(f"- Nome é igual a {nome}")
        print(f"- Nota é igual a {nota}")
        print(f"- Situação é igual a Aprovado")