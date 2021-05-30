import numpy as np

# numpy.frombuffer
s = 'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)

x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)

# numpy.asarray
x = [1, 2, 3]
a = np.asarray(x)
print(a)

x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)

x = (1, 2, 3)
a = np.asarray(x)
print(a)

# numpy.fromiter
list = range(5)
print(list)

list = range(5)
it = iter(list)
x = np.fromiter(it, dtype=float)
print(x)
