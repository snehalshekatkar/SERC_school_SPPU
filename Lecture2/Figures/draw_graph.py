import graph_tool.all as gt
import pandas as pd

df = pd.read_csv('edge_list.dat', header = None)

edges = []
for i in range(17):
    edges.append((df.iloc[i][0], df.iloc[i][1]))


#edges = [(0, 2), (0, 3), (1, 2), (1, 3), (2, 5), (3, 4)]

g = gt.Graph(directed = False)
name = g.add_edge_list(edges, hashed = True)
pos = gt.sfdp_layout(g)
#color = g.new_vertex_property('string')
#shape = g.new_vertex_property('string')
#
#for v in g.vertices():
#    if int(v) < 3:
#        color[v] = 'red'
#        shape[v] = 'square'
#    else:
#        color[v] = 'blue'
#        shape[v] = 'circle'

edge_betweenness = gt.betweenness(g)[1]
for e in g.edges():
    edge_betweenness[e] *= 20

g.vertex_properties['name'] = name
g.save('msc.gml')

#gt.graph_draw(g, vertex_text = name, vertex_font_size = 8, vertex_shape = "double_circle", vertex_fill_color = "#729fcf", vertex_pen_width = 3, edge_pen_width = edge_betweenness, output = 'msc3.pdf')
#gt.graph_draw(g, pos = pos, vertex_fill_color = color, vertex_shape = shape, vertex_color = 'k', output = 'small_graph2.pdf')

