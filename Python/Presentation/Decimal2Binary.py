n = int(input("Enter the number you want to convert: "))
num = n
a = []
while(n > 0):
    b = n % 2
    a.append(b)
    n = n//2
a.reverse()
print("Binary of", num, "is: ")
for i in a:
    print(i, end=" ")

# Through recursion
'''
    def binary(n):
        if n > 1:
            binary(n//2)
        print(n%2, end = '')

    dec = int(input("Enter an Integer: "))
    binary(dec)
'''
