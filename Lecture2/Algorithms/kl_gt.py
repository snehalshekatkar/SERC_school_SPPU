from itertools import combinations
import numpy as np
import graph_tool.all as gt

#fetch the graph
#g = gt.collection.data['lesmis']
g = gt.collection.data['karate']

# Divide the graph into two parts with sizes n1 and n2 so that the cut size is minimum
n = g.num_vertices()
n1 = 20
n2 = n-n1 

# Make a random division
group = g.new_vertex_property('int')

first_group = np.random.choice(list(g.vertices()), size = n1, replace = False)

for v in g.vertices():
    if v in first_group:
        group[v] = 1
    else:
        group[v] = 2

# Make rounds of KL algorithm        
for _ in range(1):

    for t in range(min(n1, n2)):
        print("time", t)

        first_group = [v for v in g.vertices() if group[v] == 1]
        second_group = [v for v in g.vertices() if group[v] == 2]

        # Calculate the cut size
        cut = 0
        for e in g.edges():
            if group[e.source()] != group[e.target()]:
                cut += 1

        # Find out the pair to be swapped
        for i1 in first_group:
            for i2 in second_group:

                if i1 == 0 and i2 == 0:
                    most_decrease = (i1, i2)
                    least_increase = (i1, i2)
                    tot_increase = g.num_edges()

                # exchange the vertices
                first_group.remove(i1)
                second_group.remove(i2)
                first_group.append(i1)
                second_group.append(i2)

                # reassign the property map's values
                for v in g.vertices():
                    if v in first_group:
                        group[v] = 1
                    else:
                        group[v] = 2

                # calculate the change in the cut size
                cut_new = 0
                for e in g.edges():
                    if group[e.source()] != group[e.target()]:
                        cut_new += 1

                if cut_new < cut:
                    cut = cut_new
                    most_decrease = (i1, i2)
                else:
                    if cut_new - cut < tot_increase:
                        least_increase = (i1, i2)

                    




