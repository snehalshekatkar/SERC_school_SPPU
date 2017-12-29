from copy import copy
import graph_tool.all as gt

g = gt.Graph(directed = False)

edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 7), (2, 3), (2, 4), (2, 5), (3, 4), (3, 7), (5, 6), (5, 8), (6, 8), (6, 10), (6, 11), (7, 8), (8, 9), (9, 10), (9, 11), (10, 11)]

g.add_edge_list(edges)

color = g.new_vertex_property('string')
shape = g.new_vertex_property('string')

pos = gt.sfdp_layout(g)

for v in g.vertices():
    shape[v] = 'circle'
    if int(v) < 6:
        color[v] = 'r'
    else:
        color[v] = 'b'

    if int(v) in {5, 7}:
        shape[v] = 'double_circle'

gt.graph_draw(g, pos = pos, vertex_text = g.vertex_index, vertex_fill_color = color, vertex_color = 'k', vertex_shape = shape, output = 'kl1.pdf')        

z = copy(pos[5])
pos[5] = copy(pos[7])
pos[7] = copy(z)

z = color[5]
color[5] = color[7]
color[7] = z

z = shape[5]
shape[5] = shape[7]
shape[7] = z

gt.graph_draw(g, pos = pos, vertex_text = g.vertex_index, vertex_fill_color = color, vertex_color = 'k', vertex_shape = shape, output = 'kl2.pdf')        
