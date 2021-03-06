import scipy
from scipy import interpolate
from scipy.spatial import ConvexHull as h
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')
plt.switch_backend('cairo')
import graph_tool.all as gt
from sklearn.cluster import KMeans

'''Load the graph'''
g = gt.load_graph('resolved_sbm.gt')
block = g.vertex_properties['block']

''' Generate a position for the vertices'''
#pos = gt.sfdp_layout(g)
pos = gt.sfdp_layout(g, C = 0.4) # Repel nodes with higher C value

#X = np.array([tuple(pos[v]) for v in g.vertices()])
#'''Use k-means clustering to remove overlaps'''
#kmeans = KMeans(n_clusters = 4, random_state = 0).fit(X)
#group = kmeans.predict(X)
#for v in g.vertices():
#    block[v] = group[int(v)]

colors = ['red', 'darkgreen', 'darkorange', 'purple', 'brown', 'aliceblue', 'cyan', 'magenta', 'yellow', 'darkmagenta']

size = g.new_vertex_property('float')
for v in g.vertices():
    size[v] = 5 * np.sqrt(v.out_degree()) + 4

color = g.new_vertex_property('string')
for v in g.vertices():
    color[v] = colors[block[v]]


'''Draw loops around communities'''
fig, ax = plt.subplots()

gt.graph_draw(g, pos = pos, vertex_shape = block, vertex_size = size, vertex_fill_color = color, vertex_color = 'white', mplfig = ax)

for ind in range(max([block[v] for v in g.vertices()]) + 1):

    print(ind, colors[ind])

    print("alpha", ind)
    try:
        pos_np = []
        for v in g.vertices():
            if block[v] == ind:
                pos_np.append(tuple(pos[v]))
        
        points = np.array(pos_np)

        '''Add four extreme points in 4 directions''' 

        new_point1 = points[np.argmax(points, axis = 0)[0]] + [3, 0]
        new_point2 = points[np.argmax(points, axis = 0)[1]] + [0, 3]
        new_point3 = points[np.argmin(points, axis = 0)[0]] - [3, 0]
        new_point4 = points[np.argmin(points, axis = 0)[1]] - [0, 3]

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
        #ax.plot(new_point1[0], new_point1[1], 's', markersize = 5, color = colors[ind])
        #ax.plot(new_point2[0], new_point2[1], 's', markersize = 5, color = colors[ind])
        #ax.plot(new_point3[0], new_point3[1], 's', markersize = 5, color = colors[ind])
        #ax.plot(new_point4[0], new_point4[1], 's', markersize = 5, color = colors[ind])

    except:
        pass

plt.axis('equal')
#ax.set_aspect(1./ax.get_data_ratio())
plt.axis('off')
plt.savefig('with_loops2.png', transparent = True, bboxinches = 'tight')
plt.close()

fig, ax = plt.subplots()
#gt.graph_draw(g, pos = pos, fit_view = True, vertex_fill_color = color, vertex_aspect = ax.get_data_ratio(), vertex_color = 'white', mplfig = ax)
gt.graph_draw(g, pos = pos, fit_view = True, vertex_fill_color = 'b', vertex_aspect = ax.get_data_ratio(), vertex_color = 'white', mplfig = ax)
#ax.axis('equal')
ax.set_aspect(1./ax.get_data_ratio())
ax.axis('off')
plt.savefig('without_loops2.png', transparent = True, bboxinches = 'tight')
#plt.savefig('without_loops.pdf')
plt.close()
