expr = str(input("Digite uma expressão: "))
pilha = []
for i in expr:
    if i == "(":
        pilha.append("(")
    elif i == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão é inválida!")