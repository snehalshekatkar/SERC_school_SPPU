import numpy as np
import matplotlib.pyplot as plt

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

plt.plot(c_vals, S_vals)
plt.show()




