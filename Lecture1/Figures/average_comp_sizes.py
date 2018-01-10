import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

x = np.arange(0, 3, 0.01)

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

c_vals = np.array(c_vals)
S_vals = np.array(S_vals)


s = 1/(1-c_vals +c_vals * S_vals)
r = 2/(2-c_vals + c_vals * S_vals)
plt.plot(c_vals, s, linewidth = 2, label = r'$<s>$')
plt.plot(c_vals, r, '--', linewidth = 2, label = r'$R$')
plt.legend()
plt.ylim(ymin = 0, ymax = 8)
plt.xlabel(r"c", fontsize = 20)
plt.ylabel(r"Size", fontsize = 20)
plt.tight_layout()
plt.savefig('average_small_comp.pdf', bbox_inches = 'tight')
