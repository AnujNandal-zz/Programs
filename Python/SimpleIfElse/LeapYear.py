year = (int(input("Enter the year to check if it is leap year or not :\t")))
if (year % 4) == 0:
    print("%d is a leap year" % (year))
elif (year % 400) == 0:
    print("%d is a leap year" % (year))
else:
    print("It is not a leap year")
