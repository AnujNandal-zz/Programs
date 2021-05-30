# To find square of numbers within the range
num1 = (int(input("Enter a number to start with :\t")))
num2 = (int(input("Enter a number to end with :\t")))

while(num1 <= num2):
    print("The square of ", num1, "is :\t", num1*num1)
    num1 = num1+1
else:
    print("Now the limit is over.")
