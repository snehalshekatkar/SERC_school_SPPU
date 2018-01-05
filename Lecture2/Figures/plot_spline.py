import scipy
from scipy import interpolate
from scipy.spatial import ConvexHull as h
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')
plt.switch_backend('cairo')
import graph_tool.all as gt


''' Load a graph '''
g = gt.collection.data['karate']

''' Generate a position for the vertices'''
pos = gt.sfdp_layout(g)
pos_np = []
for v in g.vertices():
    pos_np.append(tuple(pos[v]))
points = np.array(pos_np)

''' Calculate the hull for the network '''
hull = h(pos_np)


''' Make lists of x and y cooridinates of corners of the hull '''
f1 = [points[i, 0] for i in hull.vertices]
f2 = [points[i, 1] for i in hull.vertices]

''' Include the initial point so that the loop will close '''
f1.append(points[hull.vertices[0], 0])
f2.append(points[hull.vertices[0], 1])

''' Construct numpy arrays from these coordinate lists '''
x = np.array(f1)
y = np.array(f2)

''' Calculate spline that goes through the corners of the hull'''
t = np.arange(x.shape[0], dtype=float)
t /= t[-1]
nt = np.linspace(0, 1, 100)
x1 = scipy.interpolate.spline(t, x, nt)
y1 = scipy.interpolate.spline(t, y, nt)

''' Draw the network and the loop around it '''
fig, ax = plt.subplots()
gt.graph_draw(g, pos = pos, mplfig = ax)
ax.plot(x1, y1, '--')
plt.savefig('test.pdf')

