import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.read_graphml("code/practicas/data/Florentine_PADGM.graphml")

nx.draw(G, with_labels=True, font_weight='bold', node_color='lightgreen', node_size=500, edge_color='gray',)
plt.show()