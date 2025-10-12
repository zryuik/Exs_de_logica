def contador(inicio, fim, passo):
    c = inicio
    while c <= fim:
        print(f"{c}", end=" ", flush=True)
        c += passo
    print("Cabo")



inicio = int(input("Digite o inicio "))
fim = int(input("Digite o final "))
passo = int(input("Digite o passo "))
contador(inicio,fim,passo)
contador(5,9,2)
