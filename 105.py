def notas(*n, sit=False):
    """
    Calcula estatísticas sobre um conjunto de notas e, opcionalmente, avalia a situação da turma.

    Parâmetros:
        *n (float): Uma ou mais notas dos alunos (quantidade variável de argumentos).
        sit (bool, opcional): Se True, adiciona a situação ('BOA', 'RAZOAVEL' ou 'RUIM') ao resultado.
                              Padrão é False.

    Retorna:
        dict: Um dicionário contendo:
            - 'Total': número de notas fornecidas.
            - 'maior': maior nota.
            - 'menor': menor nota.
            - 'média': média das notas.
            - 'Situação' (opcional): avaliação qualitativa da média geral.

    Exemplo:
        >>> notas(6, 7.5, 8, 5, sit=True)
        {'Total': 4, 'maior': 8, 'menor': 5, 'média': 6.625, 'Situação': 'RAZOAVEL'}
    """
    r = {}
    r["Total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n)/len(n)
    if sit:
        if r["média"] > 7:
            r["Situação"] = "BOA"
        elif r["média"] >= 5:
            r["Situação"] = "RAZOAVEL"
        else:
            r["Situação"] = "RUIM"
    return r

resposta = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resposta)