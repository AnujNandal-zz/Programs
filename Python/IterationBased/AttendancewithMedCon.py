TC = (int(input("Enter the total number of classes held :\t")))
CA = (int(input("Enter the number of classes you attended :\t")))
Med = (input("You you have any medical cause,(Y/N) :\t"))
PA = (CA/TC)*100
if Med == 'N':
    if PA < 75:
        print("Your attendace is %d percentage, you can't sit in the exam." % (PA))
    else:
        print("You can sit in exam.")
elif Med == 'Y':
    print("You can sit in exam according to your comfort.")
