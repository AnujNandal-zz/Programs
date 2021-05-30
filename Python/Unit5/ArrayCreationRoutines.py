import numpy as np

# numpy.empty
x = np.empty([3, 2], dtype=int)
print(x, "\n")

# numpy.zeros
x = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(x, "\n")

# numpy.ones
x = np.ones(5)
print(x)

x = np.ones([2, 2], dtype=int)
print(x)
