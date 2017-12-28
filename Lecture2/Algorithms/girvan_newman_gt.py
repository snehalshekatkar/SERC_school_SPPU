import graph_tool.all as gt

g = gt.collection.data['karate']

#gt.graph_draw(g, vertex_text = g.vertex_index)
pos = gt.sfdp_layout(g)

for _ in range(g.num_edges()):
    # Calculate edge betweenness
    ebt = gt.betweenness(g)[1]
    d = {e : ebt[e] for e in g.edges()}
    e = max(d, key = d.get)
    g.remove_edge(e)
    gt.graph_draw(g, pos = pos)
