import graph_tool.all as gt

g = gt.collection.data['lesmis']
gt.graph_draw(g, vertex_color = 'k', output = 'lesmis.pdf')
