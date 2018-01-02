import graph_tool.all as gt

g = gt.collection.data['dolphins']

pos = gt.sfdp_layout(g)

gt.graph_draw(g, pos = pos, vertex_fill_color = 'b', vertex_color = 'k', output = 'dolphins1.pdf')

state = gt.minimize_blockmodel_dl(g, deg_corr = True)
state.draw(pos = pos, vertex_shape = state.get_blocks(), vertex_color = 'k', output = 'dolphins2.pdf')
