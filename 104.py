#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


def leiaInt(texto=""):
    """
    Lê um número inteiro digitado pelo usuário, validando a entrada.

    Esta função solicita ao usuário que digite um valor e verifica se a entrada 
    é composta apenas por dígitos numéricos. Caso o valor informado não seja 
    um número inteiro válido, o programa exibe uma mensagem de erro e solicita 
    novamente a entrada até que um valor correto seja digitado.

    Parâmetros:
        texto (str): Texto exibido ao solicitar o valor ao usuário.

    Retorna:
        int: O número inteiro digitado pelo usuário.
    """
    ok = False
    valor = 0
    while True:
        numero = str(input(texto))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido\033[m")
        if ok:
            break
    return valor


numero = leiaInt("Digite um valor: ")
print(f"Você acabou de digitar {numero}")




