def contador(inicio, fim, passo):
    """
       This script created by z 
    Realiza uma contagem numérica de um valor inicial até um valor final, 
    exibindo cada número no console com um passo definido entre eles.

    Parâmetros:
        inicio (int): Valor inicial da contagem.
        fim (int): Valor final da contagem.
        passo (int): Intervalo (passo) entre cada número exibido.

    Exemplo:
        >>> contador(1, 10, 2)
        1 3 5 7 9 Cabo

    Observação:
        A função apenas exibe os valores na tela (não retorna lista ou tupla).
    



    """
    c = inicio
    while c <= fim:
        print(f"{c}", end=" ", flush=True)
        c += passo
    print("Cabo")



# inicio = int(input("Digite o inicio "))
# fim = int(input("Digite o final "))
# passo = int(input("Digite o passo "))
# contador(inicio,fim,passo)
contador(5,9,2)
help(contador)