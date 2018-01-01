import graph_tool.all as gt

g = gt.collection.data['karate']

shape = g.new_vertex_property('string')
color = g.new_vertex_property('string')

for v in g.vertices():
    if int(v) in {26, 22, 29, 23, 25, 15, 18, 32, 27, 24, 20, 33, 31, 14, 8, 30, 28}:
        shape[v] = 'square'
        color[v] = 'blue'
    else:
        shape[v] = 'triangle'
        color[v] = 'red'

pos = gt.sfdp_layout(g)
#pos = gt.radial_tree_layout(g, root = 0)
#pos = gt.arf_layout(g)
#pos = gt.fruchterman_reingold_layout(g)

gt.graph_draw(g, pos = pos, output = 'karate_raw.pdf')
gt.graph_draw(g, vertex_shape = shape, vertex_fill_color = color, vertex_color = 'k', pos = pos, output = 'karate_actual.pdf')

color[g.vertex(9)] = 'blue'
gt.graph_draw(g, vertex_shape = shape, vertex_fill_color = color, vertex_color = 'k', pos = pos, output = 'karate_kln.pdf')
