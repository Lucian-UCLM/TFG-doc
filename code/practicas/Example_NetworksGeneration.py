import networkx as nx
import pylab as plt    # Importing Matplotlib module pylab


plt.figure(figsize=(10,6))  # Figure size in inches

# Using Erdos-Renyi graph
plt.subplot (2, 3, 1)  # Several plots in the same Figure
g = nx.gnm_random_graph(10, 15)
plt.title('Grafo aleatorio \n 10 nodos 15 vertices')
nx.draw(g)  # Drawing to Figure

# Using Erdos-Renyi graph
plt.subplot (2, 3, 2)  # Several plots in the same Figure
g = nx.gnp_random_graph(20, 0.2)
plt.title('Grafo aleatorio \n 20 nodos probabilidad 0.2')
nx.draw(g)  # Drawing to Figure

# Using regular graph
plt.subplot (2, 3, 3)  # Several plots in the same Figure
g = nx.random_regular_graph(3,10)
plt.title('Grafo regular \n 10 nodos con grado 3')
nx.draw(g)  # Drawing to Figure

# Using configuration model
plt.subplot (2, 3, 4)
degrees = [5, 5, 3, 3, 2, 1, 1]
g = nx.configuration_model(degrees)
plt.title("Configuration model")
nx.draw(g) # Drawing to Figure

# Using Barabasi-Albert model
plt.subplot (2, 3, 5)  # Several plots in the same Figure
g = nx.barabasi_albert_graph(10, 3)
plt.title('Barabasi-Albert\n 10 nodos y m=3')
nx.draw(g)  # Drawing to Figure


# The next sentence use matplotlib to draw the network
plt.show() # Visualizing Figure


# Writing a network to file as edge list in csv format (Gephi)
nx.write_edgelist(g, "ejemmm.csv", delimiter = ",", data = False)
with open("ejemmm.csv",'r') as contents:
      save = contents.read()

# Writing edge list in format appropriate for Gephi
with open("ejemmm_Gephi.csv",'w') as contents:
      contents.write("Source Target\n")
      contents.write(save)
