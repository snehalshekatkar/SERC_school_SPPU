import graph_tool.all as gt

g = gt.load_graph('coauthors.gml')

largest_component = gt.GraphView(g, vfilt = gt.label_largest_component(g))
pos = gt.sfdp_layout(largest_component, C = 0.05, p = 2.5)
gt.graph_draw(largest_component, pos = pos, vertex_fill_color = 'g', vertex_color = 'k', vertex_shape = 'square', output = 'coauthors.pdf')

#state = gt.minimize_blockmodel_dl(largest_component)
#print(state)
#state.draw(vertex_color = 'k', pos = pos, vertex_shape = 'square', output = 'coauthors_communities.pdf')
