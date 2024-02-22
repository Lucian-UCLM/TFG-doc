import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

G = nx.Graph() # Se crea un grafo vacío
G.add_node(1) # Se añade un nodo
G.add_nodes_from([2, 3, 4, 5]) # Se añaden varios nodos
G.add_edge(1, 2) # Se añade una arista
G.add_edges_from([(1, 3), (1, 4), (1, 5)]) # Se añaden varias aristas
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
