import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

x = np.random.lognormal(10, 1, 100000)
#x = x[(x > 10**4) & (x < 10**6)]
#plt.hist(x, bins = 100, log = 'True')
plt.hist(x, bins = 1000, log = 'True')
plt.xscale('log')
plt.xlabel(r'$k$', fontsize = 20)
plt.ylabel(r'$p(k)$', fontsize = 20)
plt.xlim(xmin = 10**4, xmax = 10**6)
plt.savefig('lognormal.pdf')
