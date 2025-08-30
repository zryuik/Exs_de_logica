
par = []
impar = []
while True:
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    junta = par + impar
    junta.sort()    
    s = str(input("Quer continuar? [S/N]"))
    if s in "nN":
        break
print(f"A lista completa é {junta}")
print(f"A lista de numeros pares é {par}")
print(f"A Lista de numeros mpares é {impar}")
