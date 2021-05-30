import numpy as np

# ndim attribute
arr = np.array([[1, 2, 3, 4, 5],
                [11, 12, 13, 14, 15],
                [21, 22, 23, 24, 25]])
print("The dimension of Array is: ", arr.ndim)

# shape attribute
print("The shape of Array is: ", arr.shape)

# size attribute
print("The size of Array is: ", arr.size)

# dtype attribute
print("The datatype of Array is: ", arr.dtype)

# itemsize attribute
print("The itemsize of Array is: ", arr.itemsize)

# reshape attribute
print("The reshape of Array is:\n", arr.reshape(5, 3))

# numpy.flags
print(arr.flags)
