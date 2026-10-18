import random

def ordenacao_insercao(lista):
    """Ordena uma lista usando o método de inserção."""
    resultado = lista.copy()

    for i in range(1, len(resultado)):
        atual = resultado[i]
        j = i - 1

        while j >= 0 and resultado[j] > atual:
            resultado[j + 1] = resultado[j]
            j -= 1

        resultado[j + 1] = atual

    return resultado


def quicksort(lista):
    """Quicksort pura com pivô aleatório."""
    if len(lista) <= 1:
        return lista.copy()

    pivo = random.choice(lista)

    menores = []
    iguais = []
    maiores = []

    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento == pivo:
            iguais.append(elemento)
        else:
            maiores.append(elemento)

    return (
        quicksort(menores)
        + iguais
        + quicksort(maiores)
    )


def quicksort_hibrida(lista, corte):
    """
    Quicksort que utiliza inserção quando
    o tamanho do trecho é menor que o corte.
    """
    if corte < 1:
        raise ValueError("O corte deve ser maior ou igual a 1.")

    if len(lista) <= 1:
        return lista.copy()

    if len(lista) < corte:
        return ordenacao_insercao(lista)

    pivo = random.choice(lista)

    menores = []
    iguais = []
    maiores = []

    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento == pivo:
            iguais.append(elemento)
        else:
            maiores.append(elemento)

    return (
        quicksort_hibrida(menores, corte)
        + iguais
        + quicksort_hibrida(maiores, corte)
    )
