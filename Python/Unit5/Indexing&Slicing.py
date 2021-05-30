import numpy as np
# Example 1
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s], "\n")

# Example 2
a = np.arange(10)
b = a[2:7:2]
print(b, "\n")

# Example 3
a = np.arange(10)
b = a[5]
print(b, "\n")

# Example 4
a = np.arange(10)
print(a[2:], "\n")

# Example 5
a = np.arange(10)
print(a[2:5], "\n")

# Example 6
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
print('Now we will slice the array from the index a[1:]')
print(a[1:], "\n\n")

# Example 7
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('Our array is:')
print(a)
print('\n')
print('The items in the second column are:')
print(a[..., 1])
print('\n')
print('The items in the second row are:')
print(a[1, ...])
print('\n')
print('The items column 1 onwards are:')
print(a[..., 1:])
