# Algoritmos de Kruskal e Prim
Implementação dos algoritmos de Kruskal e Prim para obtenção de MSTs.

O trabalho a seguir trata-se da apresentação, implementação e comparação entre os algoritmos de Kruskal e de Prim para obtenção de árvores geradora mínimas (MST's), as quais podem ser aplicadas nos mais diversos casos do dia-a-dia (problemas de otimizações de distâncias, por exemplo) a partir de um determinado grafo ponderado.

A seguir encontram-se as apresentações detalhadas e implementações dos respectivos métodos:

## Algoritmo de Kruskal
Inicialmente, deve-se ter em mente que o objetivo do algoritmo de Kruskal é encontrar a MST resultante de um grafo ponderado G, ou seja, deve ser retornado um novo grafo que contenha todas as arestas presentes em G sem a formação de ciclos e cujo peso seja o menor possível.

De forma genérica, pode-se entender o algoritmo de Kruskal da seguinte maneira: inicialmente, todas as arestas do gráfico inicial dado são listadas e, em seguida, ordenadas de acordo com seus pesos. O passo seguinte trata-se de percorrer tal lista ordenada de modo a adicionar (ou não) a aresta em análise (a, b) ao grafo final da MST. Assim, para tomar tal decisão, deve-se buscar um vértice já presente na MST em formação que esteja relacionado a ambos "a" e "b". Se este vértice existir, significa que, de alguma forma, já há um caminho alternativo entre "a" e "b" e a aresta (a, b) seria causadora de um ciclo (indesejável, como mencionado).

Este processo é repetido até que todas as arestas do grafo inicial estejam conectadas formando um único grafo.

## Algoritmo de Prim
O algoritmo de Prim, assim como o de Kruskal, também utiliza a estratégia gulosa para gerar uma árvore geradora mínima (MST). De forma resumida, sua ideia geral é escolher arbitrariamente uma raiz “r” e, a partir dela, enquanto todos os nós não forem visitados executar a seguinte instrução: adicionar à árvore T a aresta de menor custo com uma extremidade no conjunto “s” dos nós visitados e outra no conjunto “v-s” dos não visitados; e depois, seguir fazendo a comparação de custo com os nós relacionados ao que foi visitado por último (que se encontra na extremidade da aresta citada).
