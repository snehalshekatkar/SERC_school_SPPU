import graph_tool.all as gt
from sklearn.cluster import KMeans
import numpy as np

g = gt.collection.data['karate']

pos = gt.sfdp_layout(g)

points = np.array([tuple(pos[v]) for v in g.vertices()])

kmeans = KMeans(n_clusters = 2, random_state = 0).fit(points)
group = kmeans.predict(points)

color = g.new_vertex_property('string')

for v in g.vertices():
    if group[int(v)] == 0:
        color[v] = 'purple'
    else:
        color[v] = 'red'

gt.graph_draw(g, pos = pos, vertex_fill_color = color)


