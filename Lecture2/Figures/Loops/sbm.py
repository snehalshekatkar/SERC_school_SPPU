import scipy
from scipy import interpolate
from scipy.spatial import ConvexHull as h
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')
plt.switch_backend('cairo')
import graph_tool.all as gt
from sklearn.cluster import KMeans

'''Generate a graph'''
p_in = 0.99
p_out = 0.005
alpha = 2.8

# Define a function to assign the inter-block probabilities
def edge_probs(s, r):
        global p_in, p_out
        if s == r:
            return p_in
        else:
            return p_out

# Define a function to generate degree values from a approximate power-law distribution
def power_law_int():
        # Specify the minimum degree value
        k_min = 2
        global alpha
        return np.rint(k_min * (1-np.random.random())**(-1/(alpha-1)))

# Specify the number of nodes, the number of blocks and their sizes
N = 500
num_blocks = 4
block_sizes = [0.1, 0.15, 0.25, 0.5]

# Generate the graph
g, block = gt.random_graph(N, deg_sampler = power_law_int, directed = False, block_membership=np.random.choice([i for i in range(num_blocks)], size = N, p = block_sizes), edge_probs = edge_probs, model = 'blockmodel-degree', n_iter = 1000)

#gt.graph_draw(g)

'''Get the largest component'''
#g = gt.Graph(gt.GraphView(g, vfilt = gt.label_largest_component(g)), prune = True)
g = gt.GraphView(g, vfilt = gt.label_largest_component(g))

''' Generate a position for the vertices'''
#pos = gt.sfdp_layout(g)
pos = gt.sfdp_layout(g, C = 0.4) # Repel nodes with higher C value

X = np.array([tuple(pos[v]) for v in g.vertices()])

'''Detect communities'''
#state = gt.minimize_blockmodel_dl(g, deg_corr = True, B_max = 4, B_min = 4)

#block = state.get_blocks()
'''Use k-means clustering to remove overlaps'''
kmeans = KMeans(n_clusters = 4, random_state = 0).fit(X)
group = kmeans.predict(X)
#group = [block[v] for v in g.vertices()]

for v in g.vertices():
    block[v] = group[int(v)]

print(group)

colors = ['red', 'darkgreen', 'darkorange', 'purple', 'brown', 'aliceblue', 'cyan', 'magenta', 'yellow', 'darkmagenta']

'''Draw loops around communities'''
fig, ax = plt.subplots()
color = g.new_vertex_property('string')
for v in g.vertices():
    color[v] = colors[block[v]]

gt.graph_draw(g, pos = pos, vertex_fill_color = color, vertex_color = 'white', mplfig = ax)

for ind in range(max(group) + 1):

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
plt.axis('off')
plt.savefig('test.pdf', bboxinches = 'tight')

