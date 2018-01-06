import graph_tool.all as gt
from sklearn.cluster import KMeans

def most_common(lst):
    return max(set(lst), key = lst.count)

g = gt.load_graph('simple_sbm.gt')
block = g.vertex_properties["block"]
block_old = [block[v] for v in g.vertices()]

'''Start the dynamics'''
block_new = g.new_vertex_property('int')

for t in range(20):
    for v in g.vertices():
        ''' Get neighbours of v'''
        nbrs = list(g.get_out_neighbours(v))
        nbrs.append(int(v))
        nbrs_blocks = [block[v] for v in nbrs]
        '''Find the most common block around the vertex and assign the vertex to it'''
        block_new[v] = most_common(nbrs_blocks)
        
    '''Update the blocks'''
    for v in g.vertices():
        if block[v] != block_new[v]:
            print("Working", int(v))
        block[v] = block_new[v]

# Save the graph
g.vertex_properties['block'] = block
block_new = [block[v] for v in g.vertices()]
print(block_old == block_new)
g.save('resolved_sbm.gt')
        



    
