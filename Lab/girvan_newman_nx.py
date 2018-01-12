import networkx as nx
import matplotlib.pyplot as plt

# Read the graph
g = nx.read_gml('msc.gml')

pos = nx.drawing.layout.spring_layout(g)

for _ in range(g.number_of_edges()):

    # Calculate edge betweenness
    betweenness = nx.edge_betweenness_centrality(g)

    e = max(betweenness, key = betweenness.get)
    print(e)
    g.remove_edge(e[0], e[1])
    nx.draw_networkx(g, pos = pos)
    plt.show()
    



