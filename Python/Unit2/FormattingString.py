cstr = "I love Python Programming Language"
print("The original string is : \n", cstr, "\n")

print("----------center() function---------------")

print("The center aligned string is : ")
print(cstr.center(40), "\n")
print("center aligned string with fillchr: ")
print(cstr.center(40, '#'))

print("\n----------rjust() function---------------")

print("The right aligned string is : ")
print(cstr.rjust(40), "\n")
print("Right aligned string with fillchr: ")
print(cstr.rjust(40, '#'))

print("\n----------ljust() function---------------")

print("The left aligned string is : ")
print(cstr.ljust(40), "\n")
print("Left aligned string with fillchr: ")
print(cstr.ljust(40, '#'))
