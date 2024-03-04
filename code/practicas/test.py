import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

G = nx.read_edgelist("code/practicas/test.txt")

# G = nx.Graph()
# G.add_node(1)
# G.add_nodes_from([2, 3, 4, 5]) 
# G.add_edge(1, 2) 
# G.add_edges_from([(1, 3), (1, 4), (1, 5), (5,2), (4,3)]) 
n = G.number_of_nodes()
m = G.number_of_edges()


print("Número de nodos: ", n)
print("Número de aristas: ", m)
print("Nodos: ", G.nodes())
print("Aristas: ", G.edges())
# print("Vecinos del nodo 1: ", list(G.neighbors(1)))
# print("Grado del nodo 1: ", G.degree(1))
print("Matriz de adyacencia: ")
print(nx.adjacency_matrix(G).todense())


node_degrees = dict(G.degree())
print("Grados: ", node_degrees)
degrees = list(node_degrees.values())
print("Solo grados: ", degrees) 
print("Grado medio: ", np.mean(degrees))    
mean = 0.0
for d in degrees:
    mean += d
mean = mean/n
print("Grado medio: ", mean)

print("Betweenness centrality: ", nx.betweenness_centrality(G))
print("Closeness centrality: ", nx.closeness_centrality(G))
print("Degree centrality: ", nx.degree_centrality(G))
print("Eigenvector centrality: ", nx.eigenvector_centrality(G))
print("Katz centrality: ", nx.katz_centrality(G))
print("PageRank: ", nx.pagerank(G))
print("Clustering: ", nx.clustering(G))

nx.draw(G, with_labels=True, font_weight='bold', node_color='lightgreen', node_size=500, edge_color='gray',)
plt.show()
