import numpy as np
# One dimensional array
arr1 = ['Anuj', 'Ashish', 'Ayush', 'Bhavya']
print("The array of 1 dimension is: ", np.array(arr1))
narr = np.array(arr1)
print("The array of 1 dimension is: ", narr)

# Two dimensional array
arr2 = np.array([['Anuj', 'Ashish', 'Ayush', 'Bhavya'],
                 ['Adarsh', 'Amarjeet', 'Aniket', 'Baldev']])
print("The array of 2 dimension is: ", arr2)
print("The array of 2 dimension is: ", arr2[1][2])
print("The array of 2 dimension is: ", arr2[1, 3])

# Array example
arr = np.array(([1, 2, 3, 4, 5], [2, 3, 1, 5, 1], [9, 8, 7, 6, 5]))
print(arr)

a = np.array([1, 2, 3])
print(a)
print("\n")

b = np.array([[1, 3, 6], [2, 4, 8]])
print(b)
print(b.shape)
print(b.size)
print("\n")

c = np.array([1, 2, 3, 4, 5], dtype=int)
print(b)
print(c.itemsize)
print(c.dtype.name)
print("\n")

d = np.arange(15).reshape(3, 5)
print(d)
print(type(d))
