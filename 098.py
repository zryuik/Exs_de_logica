from time import sleep
def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-' *30)
    print(f"Contagem de {a} ate {b} de {c} em {c}")
    print('-' * 30)
    sleep(2.5)

    if a < b:
        cont = a
        while cont <= b:
            print(f"{cont} ", end="")
            sleep(0.5)
            cont += c
        print("FIM")
    else:
        cont = a
        while cont >= b:
            print(f"{cont} ", end=" ")
            sleep(0.5)
            cont -= c
        print('FIM')

#programa principal
contador(1, 10, 1)
contador(10,0,2)
print("Agora é sua vez de personalizar a contagem! ")
ini = int(input("Ínicio: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))
contador(ini, fim, pas)







