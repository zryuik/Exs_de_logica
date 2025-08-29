valores = []

for i in range(5):
    val = int(input(f"Digite o {i+1}º valor: "))

    if len(valores)  == 0 or val > valores[-1]:
        valores.append(val)
    else:
        pos = 0
        while pos < len(valores):
            if val <= valores[pos]:
                valores.insert(pos, val)
                break
            pos += 1

print(valores)