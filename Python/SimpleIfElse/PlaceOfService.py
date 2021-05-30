age = (int(input("Enter your age :\t")))
sex = (input("Enter your sex(M/F) :\t"))
MS = (input("Enter your marital status(Y/N) :\t"))
if sex == 'F':
    print("You will be working in urban areas.")
elif sex == 'M' and age >= 20 and age < 40:
    print("You can work anywhere.")
elif sex == 'M' and age >= 40 and age < 60:
    print("You will be working in urban areas.")
else:
    print("ERROR!")
