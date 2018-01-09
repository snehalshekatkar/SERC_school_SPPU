import graph_tool.all as gt

n = 10
g = gt.complete_graph(n)

tree = gt.min_spanning_tree(g)
g.set_edge_filter(tree)

# Choose an unconnected vertex pair
dist = gt.shortest_distance(g)
for v in g.vertices():
    print(dist[v])
gt.graph_draw(g, vertex_fill_color = 'b', output = 'tree2.pdf')
