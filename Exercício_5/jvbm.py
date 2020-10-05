# Link para o exercício:
# https://classroom.google.com/u/0/c/MTQyNDYwMzQ1ODY1/a/MTU0NzAzMjgwODYy/details

# Link para estudo sobre o problema:
# https://www.homepages.ucl.ac.uk/~ucahmto/math/2020/05/30/bidirectional-dijkstra.html

# Descrição:
# N = número de vértices
# E = Número de arestas
# u = vértice de origem
# v = vértice de destino
# d = distância

# Estilo da entrada:
# N E
# u v d
# u v d

# Estilo de saída:
# "Path to vertex N: - " (Nesse caso não existe caminho para chegar no vértice 1, portanto o uso do hífen)
# "Path to vertex N: 1 and distance 4" 

# Preferi usar a lógica de matrix de adjacência, pois achei mais fácil de entender o conceito de grafo bidirecionado dessa forma.
# Peço desculpas adiantadas, pois por falta de criatividade usei variáveis em inglês e em português.

class Node:
  
    def __init__(self, data):
        self.data = data
        
       
class Graph:

    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)

    # Começa com none, pois não tenho nós ainda.
    def __init__(self, row, col, nodes = None): 

        # Inicia a matrix de adjacência
        self.adj_mat = [[0] * col for _ in range(row)] # Usei _, pois é uma variável que não irá ser relevante para o resto do código.
        self.nodes = nodes # Variável que foi inicializada com None
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

        # Faz com que o resto do código pegue apenas os índices dos nós para saber qual nó se trata
    def index_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("Erro!!")
        if isinstance(node, int):
            return node
        else:
            return node.index

    # Faz a conexão entre o nó1 (Row) e o nó2 (Col)
    # Row é a partida e a coluna é a chegada dos nós (IMPORTANTE).
    def connect_dir(self, node1, node2, distancia = 1):
        node1, node2 = self.index_node(node1), self.index_node(node2)
        self.adj_mat[node1][node2] = distancia
  
    def connect(self, node1, node2, distancia = 1):
        self.connect_dir(node1, node2, distancia)
        self.connect_dir(node2, node1, distancia)

    # Retorna um array de tuplas que corresponde a de onde vem o nó e a distância que foi percorrida.
    def conexao(self, node):
        node = self.index_node(node)
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if self.adj_mat[node][col_num] != 0]
     
    # Printa apenas o nó que esta na parte horizontal da matrix.
    def print_adj_mat(self):
      for row in self.adj_mat:
          print(row)
  
    def node(self, index):
      return self.nodes[index]


    def dijkstra(self, node):
        # Pega o index do nó.
        nodenum = self.index_node(node)
        # Faz com que o array fique sempre buscando uma disntância menor de nó em nó.
        dist = [None] * len(self.nodes)
        for i in range(len(dist)):
            dist[i] = [float("inf")] # Coloquei como INF, distâncias provisórias até ter uma distância definitiva.
            dist[i].append([self.nodes[nodenum]])
        
        dist[nodenum][0] = 0

        queue = [i for i in range(len(self.nodes))]
        seen = set()

        while len(queue) > 0:
            min_dist = float("inf")
            min_node = None
            for n in queue: 
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n
            
            queue.remove(min_node)
            seen.add(min_node)

            connections = self.conexao(min_node)
           
            for (node, distancia) in connections: 
                tot_dist = distancia + min_dist
                if tot_dist < dist[node.index][0]:
                    dist[node.index][0] = tot_dist
                    dist[node.index][1] = list(dist[min_node][1])
                    dist[node.index][1].append(node)
        return dist  

# Entrada exemplo
# Não tive tempo de terminar o código, mas consegui fazer com entradas previamente dadas.

a = Node("1")
b = Node("2")
c = Node("3")
d = Node("4")
e = Node("5")
f = Node("6")

w_graph = Graph.create_from_nodes([a,b,c,d,e,f])

w_graph.connect(a,b,5)
w_graph.connect(a,c,10)
w_graph.connect(a,e,2)
w_graph.connect(b,c,2)
w_graph.connect(b,d,4)
w_graph.connect(c,d,7)
w_graph.connect(c,f,10)
w_graph.connect(d,e,3)

# w_graph.print_adj_mat() 

print([(distancia, [n.data for n in node]) for (distancia, node) in w_graph.dijkstra(a)])