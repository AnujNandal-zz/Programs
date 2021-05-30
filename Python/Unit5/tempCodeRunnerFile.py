import numpy as np

# numpy.frombuffer
s = 'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)