#esse script cria duas listas dentro de uma lista e no final separa qual é par e qual e impar.


numeros_pares_impares = [[], []]


for i in range(7): #laço com for para perguntar 7 valores

    valores = (int(input(f"Digite o {i+1}º valor: "))) 
    numeros_pares_impares.append(valores)#adicionando os valores perguntados dentro da lista a cima
    if valores % 2  == 0: #verificando se o numero é par ou impar
        numeros_pares_impares[0].append(valores) #aqui, adiciona os numeros pare an lista de indice zero, ou seja na primeira lista
    else:
        numeros_pares_impares[1].append(valores)#aqui faz a mesma coisa so que adiciona os numeros impares na segunda lista

numeros_pares_impares[0].sort() #aqui ordenei os valores se eu quiser na ordem oposta basta usar (reverse=True)
numeros_pares_impares[1].sort()

print("-" * 30)
print(f"Os valores pares digitados foram: {numeros_pares_impares[0]}")
print(f"Os valores ímpares digitados foram: {numeros_pares_impares[1]}")
print("-" * 30)