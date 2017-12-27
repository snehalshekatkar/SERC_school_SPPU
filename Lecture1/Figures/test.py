import pandas as pd
import graph_tool.all as gt

#g = gt.collection.data['lesmis']
#g = gt.collection.data['netscience']
#g = gt.collection.data['adjnoun']
#print(g.gp.readme)
#name = g.vertex_properties['name']

#G = gt.GraphView(g, vfilt = gt.label_largest_component(g))

#gt.graph_draw(g, vertex_fill_color = 'r', vertex_color = 'k', output = 'adjnoun.pdf')
#gt.graph_draw(g, vertex_fill_color = 'b', vertex_color = 'k', output = 'netscience.pdf')

df = pd.read_csv('celegans_metabolic.net', sep = r'\s+|\t+', header = None)

print(df.head())

edges = []

for i in range(len(df)):
    edges.append((df.iloc[i][0], df.iloc[i][1]))

g = gt.Graph(directed = False)

g.add_edge_list(edges)
gt.remove_parallel_edges(g)
gt.remove_self_loops(g)

g.save('celegans_metabolic.xml.gz')
