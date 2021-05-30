# ----------User Defined Function------------
def product():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    prod = n1*n2
    print(n1, " X ", n2, " = ", prod)


product()

# ------------Return statement--------------


def sum():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter first number: "))
    s = n1+n2
    return s


print("The sum is: ", sum())

# ----------------Lambda Function---------------------


def var(a, b): return (a*b)/2


print("The lambda function evaluated: ", var(3, 5))

# ----------------Factorial Function-------------------


def facto(n):
    if n == 1:
        return 1
    return n*facto(n-1)


num = int(input("Enter a number to find factorial: "))
print("The factorial of", num, "is: ", facto(num))
