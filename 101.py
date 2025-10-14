#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


from datetime import datetime

def voto(ano_nascimento):
    """
        Determina o tipo de voto de uma pessoa com base no seu ano de nascimento.

        Parâmetros:
        ano_nascimento (int): O ano de nascimento da pessoa.

        Retorna:
        str: Uma mensagem indicando se o voto é NEGADO, OPCIONAL ou OBRIGATÓRIO,
            conforme as regras eleitorais brasileiras:
            - Menores de 16 anos: voto NEGADO
            - De 16 a 17 anos ou acima de 70 anos: voto OPCIONAL
            - De 18 a 70 anos: voto OBRIGATÓRIO

        Exemplo:
        >>> voto(2008)
        'Idade: 17 anos — VOTO OPCIONAL'
        """

    idade = datetime.now().year - ano_nascimento


    if idade < 16:
        return f"Idade {idade} anos, VOTO NEGADO"
    elif idade > 16 and idade == 18:
        return f"Idade {idade} anos, VOTO OPCIONAL"
    else:
        return f"Idade {idade} anos, VOTO OBRIGATORIO"


ano = int(input("Digite o ano em que voce nasceu: "))
print(voto(ano))