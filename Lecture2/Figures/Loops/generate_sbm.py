import numpy as np
import graph_tool.all as gt

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

print(block)

'''Save the graph'''
g.vertex_properties["block"] = block
g.save('simple_sbm.gt')
