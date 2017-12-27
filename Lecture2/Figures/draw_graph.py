import graph_tool.all as gt

edges = [(0, 1), (0, 2), (1, 2), (0, 3), (0, 4), (3, 4)]

g = gt.Graph(directed = False)
g.add_edge_list(edges)
pos = gt.sfdp_layout(g)
color = g.new_vertex_property('string')
shape = g.new_vertex_property('string')

for v in g.vertices():
    if int(v) < 3:
        color[v] = 'red'
        shape[v] = 'square'
    else:
        color[v] = 'blue'
        shape[v] = 'circle'

gt.graph_draw(g, pos = pos, vertex_color = 'k', output = 'small_graph1.pdf')
gt.graph_draw(g, pos = pos, vertex_fill_color = color, vertex_shape = shape, vertex_color = 'k', output = 'small_graph2.pdf')

