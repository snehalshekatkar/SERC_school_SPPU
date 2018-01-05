import numpy as np
import graph_tool.all as gt
from scipy.spatial import ConvexHull as h
import scipy.interpolate
import matplotlib.pyplot as plt
plt.style.use('classic')
plt.switch_backend('cairo')

g = gt.collection.data['karate']

shape = g.new_vertex_property('string')
color = g.new_vertex_property('string')
group = g.new_vertex_property('int')

for v in g.vertices():
    if int(v) in {26, 22, 29, 23, 25, 15, 18, 32, 27, 24, 20, 33, 31, 14, 8, 30, 28}:
        shape[v] = 'square'
        color[v] = 'blue'
        group[v] = 0
    else:
        shape[v] = 'triangle'
        color[v] = 'red'
        group[v] = 1

#print(gt.scalar_assortativity(g, deg = group))
pos = gt.sfdp_layout(g)

pos_np = []
for v in g.vertices():
    pos_np.append(tuple(pos[v]))

points = np.array(pos_np)
print(pos_np)

hull = h(pos_np)

'''Draw loops around communities'''
fig, ax = plt.subplots()
gt.graph_draw(g, pos = pos, mplfig = ax)
for simplex in hull.simplices:
    ax.plot(points[simplex, 0], points[simplex, 1], 'k-')

print("vertices", hull.points)
x = hull.points[:, 0]
y = hull.points[:, 1]

#t = np.arange(x.shape[0], dtype=float)
#t /= t[-1]
#nt = np.linspace(0, 1, 100)
#x1 = scipy.interpolate.spline(t, x, nt)
#y1 = scipy.interpolate.spline(t, y, nt)
##plt.plot(x1, y1, label='range_spline')
#
#t = np.zeros(x.shape)
#t[1:] = np.sqrt((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2)
#t = np.cumsum(t)
#t /= t[-1]

#nt = 
#x2 = scipy.interpolate.spline(t, x, nt)
#y2 = scipy.interpolate.spline(t, y, nt)

tck, u = interpolate.splprep([x, y], s = 0)

ax.plot(x2, y2, label='dist_spline')

#ax.plot(pos_np[hull.vertices, 0], pos_np[hull.vertices, 1], 'r--', lw = 2)
#ax.plot(pos_np[hull.vertices[0], 0], pos_np[hull.vertices[0], 1], 'ro')
plt.savefig('test.pdf')

#pos = gt.radial_tree_layout(g, root = 0)
#pos = gt.arf_layout(g)
#pos = gt.fruchterman_reingold_layout(g)

#gt.graph_draw(g, pos = pos, output = 'karate_raw.pdf')
#gt.graph_draw(g, vertex_shape = shape, vertex_fill_color = color, vertex_color = 'k', pos = pos, output = 'karate_actual.pdf')

color[g.vertex(9)] = 'blue'
group[g.vertex(9)] = 0
#print(gt.scalar_assortativity(g, deg = group))
#gt.graph_draw(g, vertex_shape = shape, vertex_fill_color = color, vertex_color = 'k', pos = pos, output = 'karate_kln.pdf')
