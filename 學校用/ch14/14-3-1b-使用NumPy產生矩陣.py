import numpy as np
a = np.ones(6, dtype=np.int32)
b = np.linspace(0, np.pi, 6)
print(a)
print(b)
print(a+b)
a = np.random.random((2, 4))
print(a)
print(a.sum(), a.max(), a.min(), a.mean())
b = np.arange(1, 9, 1).reshape(2, 4)
print(b)

