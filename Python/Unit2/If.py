print('Enter your age :')
x = int(input())

if(x > 18):
    print("You are Eligible to Vote")
else:
    print("You are not eligible to vote")


num = int(input("\n\nEnter the number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

a = int(input("\n\nEnter a: "))
b = int(input("\nEnter b: "))
c = int(input("\nEnter c: "))
if a > b and a > c:
    print("a is largest")
if b > a and b > c:
    print("a is largest")
if b > a and c > b:
    print("c is largest")
