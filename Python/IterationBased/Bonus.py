salary = (int(input("Enter your salary :\t")))
YoS = (int(input("Enter your year(s) of service :\t")))
bonus = 0
if YoS > 5:
    bonus = salary*0.5
    print("Your net bonus amount is", bonus)
else:
    print("You don't get bonus for now!")
