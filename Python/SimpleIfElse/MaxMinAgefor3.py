age1 = (int(input("Enter your age :\t")))
age2 = (int(input("Enter your age :\t")))
age3 = (int(input("Enter your age :\t")))
if age1 > age2 and age2 > age3:
    print("%d is the oldest and %d is the youngest" % (age1, age3))
elif age2 > age1 and age1 > age3:
    print("%d is the oldest and %d is the youngest" % (age2, age3))
elif age3 > age2 and age2 > age1:
    print("%d is the oldest and %d is the youngest" % (age3, age1))
elif age1 > age3 and age3 > age2:
    print("%d is the oldest and %d is the youngest" % (age1, age2))
elif age2 > age3 and age3 > age1:
    print("%d is the oldest and %d is the youngest" % (age2, age1))
elif age3 > age1 and age1 > age2:
    print("%d is the oldest and %d is the youngest" % (age3, age2))
else:
    print("Invalid input")
