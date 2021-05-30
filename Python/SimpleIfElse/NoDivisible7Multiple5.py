n = (int(input("Enter a number between 1500 and 2700 :\t")))
if n >= 1500 and n <= 2700:
    if n % 7 == 0 and n % 5 == 0:
        print("%d is divisible by 7 and a multiple of 5" % (n))
    else:
        print("%d is neither divisible by 7 nor a multiple of 5" % (n))
else:
    print("Please enter a number which is 1500, 2700 or between them")
