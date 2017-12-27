import graph_tool.all as gt
import matplotlib.pyplot as plt
plt.style.use('classic')

g = gt.load_graph('celegans_metabolic.xml.gz')

g = gt.Graph(gt.GraphView(g, vfilt = gt.label_largest_component(g)), prune = True)

print(g)

gt.graph_draw(g, vertex_fill_color = gt.local_clustering(g), vertex_color = 'k', output = 'celegans_metabolic.pdf')
seq = [v.out_degree() for v in g.vertices()]

plt.hist(seq, normed = True, bins = max(seq)//5, log = True)
plt.xlabel(r'$k$', fontsize = 20)
plt.ylabel(r'$p(k)$', fontsize = 20)
plt.xscale('log')

plt.savefig('deg_distri_celegans_metabolic_log.pdf', bboxinches = 'tight')
