import networkx as nx
import pylab as plt    # Importing Matplotlib module pylab

plt.subplot(2, 1, 1)
g=nx.read_graphml("Florentine_PADGM.graphml")
nx.draw(g, with_labels = True)


# Creating dictionary with entries (Label, Position) 
# where Position is the key. The idea is to save the
# original name of the nodes.
d = {}
i = 0
for item in list(dict(g.degree()).keys()):
    d[i] = item
    i = i + 1 
print(d)


plt.subplot(2, 1, 2)
g = nx.configuration_model(list(dict(g.degree()).values()))

# Labeling nodes in configuration model with their original labels
g = nx.relabel_nodes(g, d, copy=True)
nx.draw(g, with_labels = True)
plt.show()

# Writing configuration model to a file
nx.write_graphml(g, "pepito.graphml")


