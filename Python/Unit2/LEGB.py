# -----------------Built-In Scope-------------
from math import pi


def outer():
    def inner():
        print(pi)
    inner()


outer()


# ------------------Global Scope----------
a = 1


def counter():
    global a
    a = 4
    print(a)


counter()


# ----------------Enclosed Scope---------------


def red():
    num1 = 1

    def blue():
        num2 = 2
        print(num1)
        print(num2)
    blue()
    print(num1)


red()

# ------------------Local Scope-----------


def func(num=2):
    num += 4
    print(num)


func()
