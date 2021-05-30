total = (int(input("Enter the total number of items in the list: ")))
a = 1
output = []
while a < total+1:
    ls = ((int(input("Enter the numbers of the list: "))))
    a += 1
    if ls <= 150:
        if ls % 5 == 0:
            output.append(ls)
    else:
        break

print("The numbers that are divisible in the list are: ", output)
