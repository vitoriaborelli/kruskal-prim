# Implementação das primitivas que serão utilizadas nos algoritmos
class Grafo:
  parent = {}

# Make_Set(v) é a primitiva responsável por inicializar os vértices como novos grafos de vértice único

  def Make_Set(self, v):

    for i in range(v):
      self.parent[i] = i;

# Find_Set(v) é responsável por retornar a raiz da árvore a qual v pertence 
# recursivamente procura o vértice cujo pai é ele mesmo

  def Find_Set(self, v):

    if self.parent[v] == v:
      return v

    return self.Find_Set(self.parent[v])

# Union(u,v) será a função que irá unir duas árvores a partir de seus vértices raiz

  def Union(self, u, v):

    u_root = self.Find_Set(u)
    v_root = self.Find_Set(v)

    self.parent[u_root] = v_root

################### KRUSKAL ###################

def Kruskal(edges, n):

  # armazenando arestas do MST
  
  MST = [] 

  # inicializando n arestas como conjuntos disjuntos 

  G = Grafo()
  G.Make_Set(n)

  # ordenando as arestas de acordo com seu peso

  edges.sort(key=lambda x: x[2])

  # começa a percorrer a lista ordenada 

  index = 0 # inicialização da variável índice da lista
  while len(MST) != n - 1:

     # percorre as areestas de forma crescente
     # representação das arestas: (vértice fonte, destino, peso)

    (src, dest, weight) = edges[index] 
    index = index + 1
 
    # encontre a raiz de cada um dos vértices dados 
 
    src_root = G.Find_Set(src)
    dest_root = G.Find_Set(dest)
 
    # checa se possuem raiz em comum, em caso negativo, a aresta pode ser incluída no MST sem gerar ciclos
      
    if src_root != dest_root:
        MST.append((src, dest, weight))
        G.Union(src_root, dest_root)
      
  return MST

################### EXEMPLOS KRUSKAL ###################
# EXEMPLO 1

# inicialização do grafo teste 
# número de vértices do grafo
n = 6 

# descrição das arestas (origem, destino, peso)
edges = [
    (0, 1, 4), (0, 2, 4), (1, 2, 2), (1, 0, 4), (2, 0, 4), (2, 1, 2), (2, 3, 3), (2, 5, 2), (2, 4, 4), (3, 2, 3), (3, 4, 3), (4, 2, 4), (4, 3, 3), (5, 2, 2), (5, 4, 3)
]

# chamada do algoritmo e impressão do resultado
MST = Kruskal(edges, n)
print("MST do exemplo 1: ", MST)

# EXEMPLO 2

n = 9
edges = [
    (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 5, 4), (2, 8, 2), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)
]

MST = Kruskal(edges, n)
print("MST do exemplo 2: ", MST)

################### PRIM ###################

import networkx as nx

def Prim(G, root):
    MST = nx.Graph() 
    MST.add_node(root) 

    # Repete o processo até que todos os nós sejam incluídos na MST
    while set(MST.nodes) != set(G.nodes):
        min_weight = float('inf') # atribui valor infinito para a variável que armazenará o menor peso encontrado
        min_edge = None 

        # Encontra a menor aresta conectando a MST a um nó ainda não incluído
        for n1 in MST.nodes: 
            for n2 in G.nodes: 
                if n2 not in MST.nodes: # verifica se o nó não está presente na MST
                    if G.has_edge(n1, n2) and G[n1][n2]['weight'] < min_weight: # verifica se a aresta entre os nós existe e tem menor peso do que o mínimo encontrado até agora
                        min_weight = G[n1][n2]['weight'] # atualiza o valor do menor peso encontrado
                        min_edge = (n1, n2) # armazena a menor aresta encontrada

        # Adiciona a menor aresta à MST e atualiza o custo total
        MST.add_edge(*min_edge, weight=min_weight)

    return MST

################### EXEMPLOS PRIM ###################

#EXEMPLO 1 -
# cria um grafo vazio
G = nx.Graph()

# adiciona os nós
G.add_nodes_from(['A', 'B', 'C', 'D'])

# adiciona as arestas com peso
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=4)
G.add_edge('C', 'D', weight=2)


# escolhe um nó arbitrário como raiz
root = 'A'

MST= Prim(G, root)

#Impressão dos Resultados
print('MST: ', MST.edges)
print('\nPESOS:')
for edge in MST.edges():
  u = edge[0]
  v = edge[1]
  print('O peso da aresta', edge, 'vale', MST[u][v]['weight'])

