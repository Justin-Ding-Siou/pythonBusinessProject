import numpy as np
x = np.array([[2,3],[1,4]], dtype=np.float64)
y = np.array([[4,2],[1,3]], dtype=np.float64)
print(x + y)
print(np.add(x, y))
print(x - y)
print(np.subtract(x, y))
print(np.dot(x, y))
