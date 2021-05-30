TC = (int(input("Enter the total number of classes held :\t")))
CA = (int(input("Enter the number of classes you attended :\t")))
PA = (CA/TC)*100
if PA < 75:
    print("Your attendace is %d percentage, you can't allowed to sit in exam" % (PA))
else:
    print("You can sit in exam.")
