import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import interpolate
from scipy.spatial import ConvexHull as h
plt.style.use('classic')
plt.switch_backend('cairo')

g = gt.Graph(directed = False)

edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (7, 8), (7, 9), (3, 10), (10, 11), (11, 12), (11, 13), (11, 14), (12, 15)]

g.add_edge_list(edges)

group = g.new_vertex_property('int')

for v in g.vertices():
    group[v] = 3

group[0] = 0

group[1] = 1
group[4] = 1
group[5] = 1

group[2] = 2
group[6] = 2
group[7] = 2
group[8] = 2
group[9] = 2

colors = ['red', 'darkgreen', 'darkorange', 'purple', 'brown', 'aliceblue', 'cyan', 'magenta', 'yellow', 'darkmagenta']

pos = gt.sfdp_layout(g)

fig, ax = plt.subplots()
color = g.new_vertex_property('string')
for v in g.vertices():
    color[v] = colors[group[v]]

gt.graph_draw(g, pos = pos, vertex_fill_color = color, vertex_color = 'black', vertex_size = 10, mplfig = ax)

for ind in range(1, max(group) + 1):

    print(ind, colors[ind])
    print("alpha", ind)
    #try:
    pos_np = []
    for v in g.vertices():
        if group[v] == ind:
            pos_np.append(tuple(pos[v]))
    
    points = np.array(pos_np)

    '''Add four extreme points in 4 directions''' 

    new_point1 = points[np.argmax(points, axis = 0)[0]] + [1, 0]
    new_point2 = points[np.argmax(points, axis = 0)[1]] + [0, 1]
    new_point3 = points[np.argmin(points, axis = 0)[0]] - [1, 0]
    new_point4 = points[np.argmin(points, axis = 0)[1]] - [0, 1]

    points = list(points)
    points.extend([new_point1, new_point2, new_point3, new_point4])
    points = np.array(points)
    
    ''' Calculate the hull for the network '''
    hull = h(points)
    
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
    x1 = scipy.interpolate.spline(t, x, nt, order = 3)
    y1 = scipy.interpolate.spline(t, y, nt, order = 3)
    
    ''' Draw the network and the loop around it '''
    ax.plot(x1, y1, '-', linewidth = 2, color = colors[ind])

    #except:
    #    pass

plt.axis('equal')
plt.axis('off')
plt.savefig('cavity.pdf')
plt.close()

'''Remove the middle vertex'''
g = gt.GraphView(g, vfilt = lambda v : group[v] != 0)
fig, ax = plt.subplots()
color = g.new_vertex_property('string')
for v in g.vertices():
    color[v] = colors[group[v]]

gt.graph_draw(g, pos = pos, vertex_fill_color = color, vertex_color = 'black', vertex_size = 10, mplfig = ax)

for ind in range(1, max(group) + 1):

    print(ind, colors[ind])
    print("alpha", ind)
    #try:
    pos_np = []
    for v in g.vertices():
        if group[v] == ind:
            pos_np.append(tuple(pos[v]))
    
    points = np.array(pos_np)

    '''Add four extreme points in 4 directions''' 

    new_point1 = points[np.argmax(points, axis = 0)[0]] + [1, 0]
    new_point2 = points[np.argmax(points, axis = 0)[1]] + [0, 1]
    new_point3 = points[np.argmin(points, axis = 0)[0]] - [1, 0]
    new_point4 = points[np.argmin(points, axis = 0)[1]] - [0, 1]

    points = list(points)
    points.extend([new_point1, new_point2, new_point3, new_point4])
    points = np.array(points)
    
    ''' Calculate the hull for the network '''
    hull = h(points)
    
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
    x1 = scipy.interpolate.spline(t, x, nt, order = 3)
    y1 = scipy.interpolate.spline(t, y, nt, order = 3)
    
    ''' Draw the network and the loop around it '''
    ax.plot(x1, y1, '-', linewidth = 2, color = colors[ind])

    #except:
    #    pass

plt.axis('equal')
plt.axis('off')
plt.savefig('cavity2.pdf')
plt.close()
