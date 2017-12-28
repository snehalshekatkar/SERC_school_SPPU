import numpy as np
import graph_tool.all as gt
import matplotlib.pyplot as plt

g = gt.load_graph('as-22july06.gml')
print(g)

seq = [v.out_degree() for v in g.vertices()]
print(max(seq))

#plt.hist(seq, bins = max(seq))
#plt.hist(seq, bins = max(seq)//5, log = True)
#plt.hist(seq, bins = np.logspace(0, 4, num = 40), log = True)
plt.hist(seq, bins = np.logspace(0, 4, num = 40), cumulative = -1, log = True)
plt.xscale('log')
#plt.xlim([0, 40])
plt.xlabel(r'$k$', fontsize = 20)
plt.xlabel(r'$p(k)$', fontsize = 20)
#plt.savefig('internet_loglog_hist.pdf')
#plt.savefig('internet_loglog_logbin_hist.pdf')
plt.savefig('internet_loglog_logbin_cum_hist.pdf')
