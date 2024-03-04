import networkx as nx
# Documentation: 
# networkx.github.io/documentation/stable/tutotial.html
# networkx.github.io/documentation/stable/
# github.com/CambridgeUniversityPress/FirstCourseNetworkScience

G = nx.Graph()
# G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_edge(1,2)

G.add_nodes_from([3,4,5])
G.add_edges_from([(3,4), (4,5), (2,1)])

print("Nodes in the G: ", G.nodes(), " a total of:", G.number_of_nodes())
print("Edges in the G: ", G.edges(), " a total of:", G.number_of_edges())

B = nx.complete_bipartite_graph(4,5)
C = nx.cycle_graph(5)
P = nx.path_graph(4)
S = nx.star_graph(6)

print("Densidad de B: ", nx.density(B))
CG = nx.complete_graph(847)
print("Densidad de CG: ", nx.density(CG)) # 1, the graph is complete
nx.write_graphml(CG, "CG.graphml")

sub = nx.subgraph(CG, (0,1,2))

print("Degree of nodes in G: ", G.degree())
