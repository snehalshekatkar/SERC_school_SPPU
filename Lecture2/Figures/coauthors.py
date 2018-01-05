import scipy
from scipy import interpolate
from scipy.spatial import ConvexHull as h
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')
plt.switch_backend('cairo')
import graph_tool.all as gt


''' Load a graph '''
#g = gt.load_graph('coauthors.gml')
#g = gt.collection.data['lesmis']
#g = gt.collection.data['dolphins']
#g = gt.collection.data['dolphins']
#g = gt.collection.data['celegansneural']
g = gt.collection.data['polbooks']

'''Get the largest component'''
g = gt.Graph(gt.GraphView(g, vfilt = gt.label_largest_component(g)), prune = True)

''' Generate a position for the vertices'''
pos = gt.sfdp_layout(g)

'''Detect communities'''
state = gt.minimize_blockmodel_dl(g, deg_corr = True)

block = state.get_blocks()
group = [block[v] for v in g.vertices()]
print(group)

colors = ['red', 'green', 'violet', 'brown', 'blue', 'cyan', 'magenta', 'yellow', 'white', 'pink']

'''Draw loops around communities'''
fig, ax = plt.subplots()
color = g.new_vertex_property('string')
for v in g.vertices():
    color[v] = colors[block[v]]

gt.graph_draw(g, pos = pos, vertex_fill_color = color, vertex_color = 'gray', mplfig = ax)


for ind in range(max(group) + 1):

    print("alpha", ind)
    try:
        pos_np = []
        for v in g.vertices():
            if block[v] == ind:
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
        x1 = scipy.interpolate.spline(t, x, nt, order = 3)
        y1 = scipy.interpolate.spline(t, y, nt, order = 3)
        
        ''' Draw the network and the loop around it '''
        ax.plot(x1, y1, '--', linewidth = 2, color = colors[ind])

    except:
        pass

plt.savefig('test.pdf')

