num = (int(input("Enter the number till you want the sum: ")))
n = num
sum = 0
a = 0
for a in range(0, n):
    sum = sum + n
    n = n-1


print("The sum of all numbers from 1 to %d is %d" % (num, sum))
