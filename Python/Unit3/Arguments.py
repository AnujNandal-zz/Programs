# -----Required Argument Function-------
def func(name):
    message = "Hi " + name
    return message


name = input("Enter the name: ")
print(func(name))

# ------Keyword Argument Function-------


def fun(name, message):
    print("\n\nPrinting the message with", name, "and ", message)


fun(name="Anuj", message="Hello")


def simple_interest(p, t, r):
    return (p*t*r)/100


print("\nSimple Interest: ", simple_interest(t=10, r=10, p=1900))


def func(name1, message, name2):
    print("\nPrinting the message with", name1, ",", message, ",and", name2)


func("Ashish", message="hello", name2="Sahil")

# ------------Variable-length Arguments----------


def varlen(*names):
    print("\n\nType of passed argument is ", type(names))
    print("Printing the passed arguments...")
    for name in names:
        print(name)


varlen("anuj", "anshul", "ashish", "sahil")

# --------------Default Arguments----------------


def defarg(name, age=19):
    print("\n\nMy name is", name, "and age is", age)


defarg(name="Anil")


def darg(name, age=22):
    print("\nMy name is", name, "and age is", age)


darg(name="Ravi")
darg(age=10, name="Rohit")
