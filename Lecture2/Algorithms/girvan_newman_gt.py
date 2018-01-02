import graph_tool.all as gt
import pandas as pd

#g = gt.collection.data['karate']

df = pd.read_csv('edge_list.dat', header = None)
edges = []

for i in range(len(df)):
    edges.append((df.iloc[i][0], df.iloc[i][1]))

g = gt.Graph(directed = False)

name = g.add_edge_list(edges, hashed = True)


#gt.graph_draw(g, vertex_text = g.vertex_index)
pos = gt.sfdp_layout(g)

ind = 0
bt = gt.betweenness(g)[1]
max_val = max([bt[e] for e in g.edges()])
for e in g.edges():
    bt[e] = 10 * bt[e]/max_val
    
print(max([bt[e] for e in g.edges()]))
gt.graph_draw(g, pos = pos, vertex_shape = 'double_circle', vertex_text = name, vertex_font_size = 8, vertex_text_position = -2, vertex_fill_color = '#729fcf', vertex_pen_width = 3, edge_pen_width = bt, output = 'gn{}.pdf'.format(ind))

for ind in range(g.num_edges()):

    bt = gt.betweenness(g)[1]
    max_val = max([bt[e] for e in g.edges()])
    for e in g.edges():
        bt[e] = 10 * bt[e]/max_val
    print(max([bt[e] for e in g.edges()]))

    # Calculate edge betweenness
    ebt = gt.betweenness(g)[1]
    d = {e : ebt[e] for e in g.edges()}
    e = max(d, key = d.get)
    g.remove_edge(e)
    gt.graph_draw(g, pos = pos, vertex_shape = 'double_circle', vertex_text = name, vertex_font_size = 8, vertex_text_position = -2, vertex_fill_color = '#729fcf', vertex_pen_width = 3, edge_pen_width = bt, output = 'gn{}.pdf'.format(ind+1))
