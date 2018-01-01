import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

x = np.arange(-1, 3.0, 0.01)
y = 0.988 * x**5 - 4.96 * x**4 + 4.978 * x**3 + 5.015 * x**2 - 6.043 * x - 1

plt.plot(x, y)

plt.savefig('local_minima.pdf')
