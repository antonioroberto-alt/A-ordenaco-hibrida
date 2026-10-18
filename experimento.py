import csv
import random
import statistics
import time

import matplotlib.pyplot as plt

from ordenacao import quicksort, quicksort_hibrida


TAMANHO = 20_000
CORTES = [1, 5, 10, 16, 20, 32, 50, 100, 200]
REPETICOES = 5
SEMENTE = 42


def medir_tempo(funcao, dados):
    """Executa a função e retorna o tempo médio em segundos."""
    tempos = []

    for _ in range(REPETICOES):
        inicio = time.perf_counter()
        resultado = funcao(dados.copy())
        fim = time.perf_counter()

        # Confere se o algoritmo realmente ordenou a lista.
        assert resultado == sorted(dados), "A lista não foi ordenada corretamente!"

        tempos.append(fim - inicio)

    return statistics.median(tempos)


def main():
    random.seed(SEMENTE)

    dados = [
        random.randint(0, 100_000)
        for _ in range(TAMANHO)
    ]

    print(f"Quantidade de elementos: {TAMANHO}")
    print(f"Repetições por configuração: {REPETICOES}")
    print("\nMedindo a quicksort pura...")

    tempo_pura = medir_tempo(quicksort, dados)

    print(f"Quicksort pura: {tempo_pura:.6f} segundos")

    resultados = []

    for corte in CORTES:
        print(f"Testando corte = {corte}...")

        funcao = lambda lista, c=corte: quicksort_hibrida(lista, c)
        tempo_hibrido = medir_tempo(funcao, dados)

        ganho_percentual = (
            (tempo_pura - tempo_hibrido) / tempo_pura
        ) * 100

        resultados.append({
            "corte": corte,
            "tempo_segundos": tempo_hibrido,
            "tempo_quicksort_pura": tempo_pura,
            "ganho_percentual": ganho_percentual,
        })

    # Salva a tabela para consulta e uso no relatório.
    with open(
        "resultados.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        campos = [
            "corte",
            "tempo_segundos",
            "tempo_quicksort_pura",
            "ganho_percentual",
        ]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)

    # Mostra os resultados no terminal.
    print("\nRESULTADOS")
    print("-" * 67)
    print(
        f"{'Corte':>8} {'Híbrida (s)':>16} "
        f"{'Pura (s)':>14} {'Ganho (%)':>13}"
    )
    print("-" * 67)

    for resultado in resultados:
        print(
            f"{resultado['corte']:>8} "
            f"{resultado['tempo_segundos']:>16.6f} "
            f"{tempo_pura:>14.6f} "
            f"{resultado['ganho_percentual']:>12.2f}%"
        )

    melhor = min(resultados, key=lambda item: item["tempo_segundos"])

    print("\nMELHOR RESULTADO")
    print(f"Corte: {melhor['corte']}")
    print(f"Tempo: {melhor['tempo_segundos']:.6f} segundos")
    print(f"Ganho sobre a pura: {melhor['ganho_percentual']:.2f}%")

    # Gera o gráfico dos tempos.
    cortes = [item["corte"] for item in resultados]
    tempos = [item["tempo_segundos"] for item in resultados]

    plt.figure(figsize=(9, 5))
    plt.plot(cortes, tempos, marker="o", label="Quicksort híbrida")
    plt.axhline(
        y=tempo_pura,
        linestyle="--",
        label="Quicksort pura"
    )

    plt.xlabel("Valor do corte")
    plt.ylabel("Tempo (segundos)")
    plt.title("Tempo de ordenação em função do corte")
    plt.xticks(CORTES)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("grafico_tempos.png", dpi=150)
    plt.close()

    print("\nArquivos gerados: resultados.csv e grafico_tempos.png")


if __name__ == "__main__":
    main()
