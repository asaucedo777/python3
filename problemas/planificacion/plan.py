import networkx as nx
import matplotlib.pyplot as plt

N = 10

def heuristicManhattan(a, b):
    # Heurística de distancia Manhattan
    return (a[0] - b[0]) + (a[1] - b[1])
def heuristicChebyshev(a, b):
    # Heurística de distancia Chebyshev
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
def heuristicHilera(a, b):
    # Heurística de la hilera
    return abs(a[0] - b[0])
def heuristicColumna(a, b):
    # Heurística de la columna
    return abs(a[1] - b[1])

def astar(graph, start, end):
    # Implementación del algoritmo A*
    path = nx.astar_path(graph, start, end, heuristic=heuristicChebyshev)
    return path
def crear_grafo_cuadricula(n):
    grafo = nx.Graph()
    for i in range(n):
        for j in range(n):
            nodo = (i, j)
            grafo.add_node(nodo)
            # Conexión con el vecino de arriba
            if i > 0:
                grafo.add_edge(nodo, (i - 1, j))
            # Conexión con el vecino de abajo
            if i < n - 1:
                grafo.add_edge(nodo, (i + 1, j))
            # Conexión con el vecino de la izquierda
            if j > 0:
                grafo.add_edge(nodo, (i, j - 1))
            # Conexión con el vecino de la derecha
            if j < n - 1:
                grafo.add_edge(nodo, (i, j + 1))
    return grafo

# Ejemplo de grafo
graph = crear_grafo_cuadricula(N)

# Define inicio y fin
start = (0, 0)
end =   (4, 6)

# Encuentra el camino
path = astar(graph, start, end)

# Visualiza el grafo y el camino
pos = {(x, y): (x, y) for x in range(N) for y in range(N)}
nx.draw(graph, pos, with_labels=False)
nx.draw_networkx_nodes(graph, pos, nodelist=[start], node_color='green')
nx.draw_networkx_nodes(graph, pos, nodelist=[end], node_color='red')
nx.draw_networkx_edges(graph, pos, edgelist=list(zip(path, path[1:])), edge_color='red', width=2)
plt.show()