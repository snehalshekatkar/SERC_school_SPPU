import graph_tool.all as gt

g = gt.load_graph('coauthors.gml')

largest_component = gt.GraphView(g, vfilt = gt.label_largest_component(g))
pos = gt.sfdp_layout(largest_component, C = 0.05, p = 2.5)
gt.graph_draw(largest_component, pos = pos, vertex_fill_color = 'g', vertex_color = 'k', vertex_shape = 'square', output = 'coauthors.pdf')

state = gt.minimize_blockmodel_dl(largest_component)
print(state)
state.draw(vertex_color = 'gray', pos = pos, vertex_shape = 'circle')
group = state.get_blocks()
print(set([group[v] for v in g.vertices()]))
color = g.new_vertex_property('string')
col_dict = {0 : "#2CA02C", 1 : "#D41C12", 2: "#5305CB", 3 : "#0C53F7", 4: ""}
#for v in g.vertices()
#state.draw(vertex_fill_color = "#2CA02C", vertex_color = 'k', pos = pos, vertex_shape = 'square', output = 'coauthors_communities.pdf')
#state.draw(vertex_fill_color = "#2CA02C", vertex_color = 'k', pos = pos, vertex_shape = 'square', output = 'coauthors_communities2.pdf')

#edges = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 5), (3, 7), (4, 5), (4, 6), (5, 7), (6, 8), (6, 9), (6, 10), (7, 8), (7, 10), (7, 11), (8, 9), (8, 10), (9, 11), (10, 11)]
#
#g = gt.Graph(directed = False)
#
#g.add_edge_list(edges)
#
#pos = gt.sfdp_layout(g)
#
#color = g.new_vertex_property('string')
#shape = g.new_vertex_property('string')
#
#for v in g.vertices():
#    if int(v) < 6:
#        shape[v] = 'square'
#        color[v] = 'red'
#    else:
#        shape[v] = 'circle'
#        color[v] = 'blue'
#
#gt.graph_draw(g, pos = pos, vertex_color = 'k', output = 'moderate_sized_network1.pdf')
#gt.graph_draw(g, pos = pos, vertex_color = 'k', vertex_shape = shape, vertex_fill_color = color, output = 'moderate_sized_network2.pdf')
