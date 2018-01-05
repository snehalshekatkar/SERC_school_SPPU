import numpy as np

x = np.random.randint(1, 10, size = (10, 2))
print(x)

print(np.argmax(x, axis = 0))
new_point1 = x[np.argmax(x, axis = 0)[0]] + [5, 0]
new_point2 = x[np.argmax(x, axis = 0)[1]] + [0, 5]
new_point3 = x[np.argmin(x, axis = 0)[0]] - [5, 0]
new_point4 = x[np.argmin(x, axis = 0)[1]] - [0, 5]

print(new_point1)
print(new_point2)
print(new_point3)
print(new_point4)

x = list(x)
x.extend([new_point1, new_point2, new_point3, new_point4])
x = np.array(x)
print(x)
