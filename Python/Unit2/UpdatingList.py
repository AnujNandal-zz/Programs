l = [1, 2, 3, 4, 5]
'''n = int(input("Enter the number of elements in the list: "))
for i in range(0, n):
    l.append(input("Enter the item: "))
'''
print("\nPrinting the list items..")
for i in l:
    print(i, end=" ")
l.remove(1)
print("Printing the list after removal of first element")
for i in l:
    print(i, end=" ")

print(l[0:6:2])
