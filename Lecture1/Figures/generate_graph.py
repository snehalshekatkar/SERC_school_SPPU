"""

The following code runs the dynamics on the Karrer-Newman model with a power-law degree distribution
The dynamics of "majority rule" is implemented using a sign function

"""

import graph_tool.all as gt
import numpy as np

#_____________________________________________________________________________________

'''Functions'''

# Define a function to assign the inter-block probabilities
def edge_probs(s, r):
        global p_in, p_out
        if s == r:
            return p_in
        else:
            return p_out

# Define a function to generate degree values from a approximate power-law distribution
def poisson():
        global c # average degree
        return np.random.poisson(c) + 1

#____________________________________________________________________________________________

# Parameters
c = 3
p_in = 0.7
p_out = 0.04


# Specify the number of nodes, the number of blocks and their sizes
N = 500
num_blocks = 2
block_sizes = [0.7, 0.3]

# Generate the graph
g, group = gt.random_graph(N, deg_sampler = poisson, directed = False, block_membership=np.random.choice([i for i in range(num_blocks)], size = N, p = block_sizes), edge_probs = edge_probs, model = 'blockmodel-degree', n_iter = 1000)

color = g.new_vertex_property('string')

for v in g.vertices():
    if group[v] == 0:
        color[v] = 'white'
    elif group[v] == 1:
        color[v] = 'black'
    else:
        color[v] = 'brown'

# Assign similar age values
age = g.new_vertex_property('float')
for e in g.edges():
    a = np.random.choice([9, 10, 11, 12])
    age[e.source()] += a
    age[e.target()] += a

for v in g.vertices():
    age[v] //= v.out_degree()
    
# Filter out the largest component
g = gt.GraphView(g, vfilt=gt.label_largest_component(g))

# Save the graph with the nodes states
g.vertex_properties["group"] = group
g.vertex_properties["age"] = age
g.save('test.gt')

gt.graph_draw(g, vertex_fill_color = color, vertex_color = 'k', output = 'assort_network2.pdf')
print(gt.assortativity(g, deg = group))
print(gt.scalar_assortativity(g, deg = age))
