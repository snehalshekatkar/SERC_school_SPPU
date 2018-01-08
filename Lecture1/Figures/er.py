import numpy as np
import graph_tool.all as gt

g = gt.Graph(directed = False)
n = 20
c = 3

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        if np.random.random() < c/n:
            edges.append((i, j))

g.add_edge_list(edges)
#pos = gt.sfdp_layout(g)
#pos = gt.radial_tree_layout(g, root = 0)
pos = gt.arf_layout(g)
gt.graph_draw(g, pos = pos, vertex_fill_color = 'purple', output = 'er1.pdf')

position = np.array([tuple(pos[v]) for v in g.vertices()])
print(position)

for ind in range(3):
    g = gt.Graph(directed = False)
    
    edges = []
    for i in range(n-1):
        for j in range(i+1, n):
            if np.random.random() < c/n:
                edges.append((i, j))
    
    g.add_edge_list(edges)
    pos = g.new_vertex_property('vector<float>')
    for v in g.vertices():  
        pos[v] = position[int(v)]
    gt.graph_draw(g, pos = pos, vertex_fill_color = 'purple', output = 'er{}.pdf'.format(ind))
