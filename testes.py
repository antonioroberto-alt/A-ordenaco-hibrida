from ordenacao import (
    ordenacao_insercao,
    quicksort,
    quicksort_hibrida,
)


def testar():
    casos = [
        [],
        [1],
        [5, 2, 8, 1, 9, 3],
        [4, 4, 4, 4],
        [9, 8, 7, 6, 5],
        [-3, 0, -10, 5, 2],
    ]

    cortes = [1, 5, 10, 16, 20, 32, 50, 100, 200]

    for lista in casos:
        esperado = sorted(lista)

        assert ordenacao_insercao(lista) == esperado
        assert quicksort(lista) == esperado

        for corte in cortes:
            assert quicksort_hibrida(lista, corte) == esperado

    # Verifica especificamente a equivalência do corte 1.
    lista = [7, 2, 9, 2, 1, 5, 8]

    assert quicksort_hibrida(lista, 1) == quicksort(lista)

    print("Todos os testes passaram!")


if __name__ == "__main__":
    testar()
