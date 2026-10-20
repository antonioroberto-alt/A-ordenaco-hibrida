Dupla envolvida;
- Antonio Roberto Da Silva Santos
- Amanda Roberta Bandeira Santos

Implementar a ordenação rápida (quicksort) com pivô aleatório e combiná-la com a ordenação por inserção para trechos pequenos. O objetivo é analisar como o valor do parâmetro `corte` influencia o tempo de execução e identificar qual configuração apresenta o melhor desempenho.

 Implementação

A quicksort escolhe um pivô aleatório e separa os elementos em três grupos: menores, iguais e maiores que o pivô. Em seguida, ordena recursivamente os grupos menores e maiores.

Na versão híbrida, quando o tamanho do trecho é menor que o valor de `corte`, a ordenação por inserção é utilizada no lugar de novas chamadas recursivas da quicksort.

Foram implementadas duas versões:

- Quicksort pura: utiliza exclusivamente a estratégia de particionamento da quicksort.
- Quicksort híbrida: utiliza quicksort para trechos maiores e ordenação por inserção para trechos menores que o corte.

Metodologia

O experimento foi realizado com os seguintes parâmetros:

- Quantidade de elementos: 20.000.
- Entrada: números inteiros aleatórios.
- Cortes testados: 1, 5, 10, 16, 20, 32, 50, 100 e 200.
- Métrica: tempo de execução em segundos.
- Comparação: quicksort pura versus quicksort híbrida.

Os tempos apresentados correspondem aos resultados obtidos durante a execução do programa no ambiente de desenvolvimento utilizado.

Resultados

A tabela apresenta os tempos medidos e o ganho percentual de cada configuração em relação à quicksort pura.

| Corte | Híbrida (s) | Quicksort pura (s) | Ganho (%) |
|---:|---:|---:|---:|
| 1 | 0,058952 | 0,050996 | -15,60% |
| 5 | 0,048765 | 0,050996 | +4,37% |
| 10 | 0,052128 | 0,050996 | -2,22% |
| 16 | 0,049406 | 0,050996 | +3,12% |
| 20 | 0,061820 | 0,050996 | -21,22% |
| 32 | 0,055451 | 0,050996 | -8,74% |
| 50 | 0,089398 | 0,050996 | -75,30% |
| 100 | 0,112547 | 0,050996 | -120,70% |
| 200 | 0,252072 | 0,050996 | -394,29% |

 valores positivos indicam que a versão híbrida foi mais rápida. Valores negativos indicam que ela foi mais lenta do que a quicksort pura.

![Gráfico do tempo de ordenação em função do corte](grafico_tempos.png)

O gráfico deve apresentar o tempo da versão híbrida para cada corte e uma linha horizontal representando o tempo da quicksort pura.

 Análise dos resultados

Qual corte apresentou o melhor tempo?
O melhor resultado foi obtido com **corte = 5**, que apresentou tempo de execução de aproximadamente 0,048765 segundos.
A quicksort pura apresentou tempo de 0,050996 segundos. Portanto, o corte igual a 5 proporcionou um ganho de aproximadamente **4,37%** em relação à versão pura.
O corte igual a 16 também apresentou resultado melhor que a quicksort pura, com ganho de aproximadamente 3,12%, mas ficou atrás do corte igual a 5.

O que acontece com cortes grandes demais?
Os resultados mostram que o desempenho piorou significativamente quando o corte aumentou excessivamente.
Com corte igual a 50, o tempo foi de aproximadamente 0,089398 segundos, representando uma piora de 75,30% em relação à quicksort pura.
Com corte igual a 100, o tempo aumentou para 0,112547 segundos, uma piora de 120,70%.
O pior resultado ocorreu com corte igual a 200, cujo tempo foi de 0,252072 segundos, aproximadamente 4,94 vezes o tempo da quicksort pura.
Isso acontece porque a ordenação por inserção pode apresentar custo quadrático, O(n²), em trechos maiores. Embora seja eficiente para listas pequenas, seu custo aumenta quando precisa ordenar trechos maiores, anulando a vantagem de continuar utilizando a quicksort.

O comportamento de corte = 1
Com corte igual a 1, a condição para utilizar a ordenação por inserção não é satisfeita por nenhum trecho não vazio, pois o código utiliza a condição `len(lista) < corte`.
Assim, a versão híbrida mantém o mesmo comportamento algorítmico da quicksort pura.
Entretanto, o experimento registrou 0,058952 segundos para a versão híbrida e 0,050996 segundos para a quicksort pura. A diferença foi de aproximadamente 15,60% a mais no tempo da híbrida.
Essa diferença não significa necessariamente que os algoritmos tenham estratégias diferentes. Como os pivôs são escolhidos aleatoriamente, as chamadas recursivas e o tempo de execução podem variar entre as execuções. Além disso, há pequenas diferenças de sobrecarga entre as funções.
Para confirmar a equivalência de desempenho de maneira mais confiável, seria recomendável repetir as medições várias vezes e comparar as medianas de cada configuração, controlando melhor a aleatoriedade dos pivôs.


O experimento demonstrou que a combinação entre quicksort e ordenação por inserção pode melhorar o desempenho, desde que o valor de corte seja adequado.
Entre os valores testados, o corte igual a 5 apresentou o melhor resultado, com ganho de aproximadamente 4,37% em relação à quicksort pura.
Também foi observado que cortes grandes demais prejudicaram o desempenho, especialmente nos valores 100 e 200, devido ao aumento do trabalho realizado pela ordenação por inserção.
Conclui-se que o valor ideal de corte depende da implementação, dos dados de entrada e do ambiente de execução. Neste experimento, o corte igual a 5 foi a melhor configuração entre as avaliadas.
