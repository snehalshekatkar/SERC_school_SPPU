import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

x = np.arange(0, 1, 0.01)

#for c in [0.5, 1, 1.5]:
#    y = 1 - np.exp(-c*x)
#    plt.plot(x, y, linewidth = 2, label = "c = " + str(c))
#    plt.legend(loc = 'upper left')
#
#plt.plot(x, x, '--', c = 'k', linewidth = 2)
#plt.ylim(0, 1)
#plt.gca().set_aspect('equal')
#plt.xlabel(r"$S$", fontsize = 20)
#plt.ylabel(r"$1-e^{-cS}$", fontsize = 20)
#plt.savefig('giant_component.pdf')

fig, ax = plt.subplots(1, 2)
for c in [0.5, 1, 1.5]:
    y = 1 - np.exp(-c*x)
    ax[0].plot(x, y, linewidth = 2, label = "c = " + str(c))
    ax[0].legend(loc = 'upper left')

ax[0].plot(x, x, '--', c = 'k', linewidth = 2)
plt.ylim(0, 1)
ax[0].set_aspect('equal')
ax[0].set_xlabel(r"$S$", fontsize = 20)
ax[0].set_ylabel(r"$1-e^{-cS}$", fontsize = 20)


c_vals = np.arange(0, 4, 0.01)
S_vals = []
for c in c_vals:
    
    x_vals = np.arange(0.01, 1, 0.001)
    
    diff = 1
    x0 = 0
    for x in x_vals:
        eps = abs(x-1+np.exp(-c*x))
        if  eps < diff:
            diff = eps 
            x0 = x
    
    S_vals.append(x0)

ax[1].plot(c_vals, S_vals)
ax[1].set_aspect(1/ax[1].get_data_ratio())
ax[1].set_xticks([0, 1, 2, 3, 4])
ax[1].set_xlabel(r"$c$", fontsize = 20)
ax[1].set_ylabel(r"$S$", fontsize = 20)

plt.tight_layout()
plt.savefig('giant_component.pdf', bboxinches = 'tight')
