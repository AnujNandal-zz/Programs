marks = (int(input("Enter your marks :\t")))
if marks > 80:
    print("Your grade is A")
elif marks >= 60 and marks <= 80:
    print("Your grade is B")
elif marks >= 50 and marks < 60:
    print("Your grade is C")
elif marks >= 45 and marks < 50:
    print("Your grade is D")
elif marks >= 25 and marks < 45:
    print("Your grade is E")
elif marks < 25:
    print("Your grade is F")
else:
    print("Enter a valid value")
