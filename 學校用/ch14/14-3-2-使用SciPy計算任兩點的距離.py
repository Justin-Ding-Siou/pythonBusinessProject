import numpy as np
from scipy.spatial.distance import pdist, squareform
x = np.array([[0, 0], [3, 5], [5, 2], [5, 5]])
print(x)
d = squareform(pdist(x, 'euclidean'))
print(d)