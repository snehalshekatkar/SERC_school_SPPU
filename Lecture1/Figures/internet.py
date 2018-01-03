import numpy as np
import graph_tool.all as gt
import matplotlib.pyplot as plt
plt.style.use('classic')

g = gt.load_graph('as-22july06.gml')
print(g)

seq = [v.out_degree() for v in g.vertices()]
print(max(seq))

#plt.hist(seq, bins = max(seq))
#plt.hist(seq, bins = max(seq)//5, log = True)
#plt.hist(seq, bins = np.logspace(0, 4, num = 40), log = True)
#plt.hist(seq, bins = np.logspace(0, 4, num = 40), cumulative = -1, log = True)
plt.hist(seq, bins = max(seq), cumulative = -1, log = True, histtype = 'step', normed = True)
plt.xscale('log')
#plt.xlim([0, 40])
plt.xlabel(r'$k$', fontsize = 20)
plt.ylabel(r'$p(k)$', fontsize = 20)
#plt.savefig('internet_loglog_hist.pdf')
#plt.savefig('internet_loglog_logbin_hist.pdf')
#plt.savefig('internet_loglog_logbin_cum_hist.pdf')
plt.ylim(ymin = 10**-4)
plt.savefig('internet_loglog_cum_hist.pdf')


#hist = gt.vertex_hist(g, "out")
#plt.plot(hist[1][:-1], hist[0], marker = "o")

#cumul = [sum([1 for kprime in seq if kprime >= k]) for k in seq]
#seq.sort()
#print(seq)
#cumul = []
#for k in seq:
#    val = 0
#    for kprime in range()
#plt.plot(cumul, marker = "o")
#plt.xscale('log')
#plt.yscale('log')
#plt.xlabel(r'$k$', fontsize = 20)
#plt.ylabel(r'$p(k)$', fontsize = 20)
#plt.savefig('internet_loglog_cum_hist.pdf')
